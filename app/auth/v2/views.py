from flask_restful import Resource, reqparse
from app.auth.v2.models import UserModel
from flask_jwt_extended import create_access_token, create_refresh_token
from app.utilities.validator_file import *

user_view = UserModel()


class UserRegister(Resource):
    """User class view to register"""
    parser = reqparse.RequestParser()
    parser.add_argument('firstname', required=True,
                        help='First Name cannot be blank', type=str)
    parser.add_argument('lastname', required=True,
                        help='Last Name cannot be blank', type=str)
    parser.add_argument('othername', required=True,
                        help='Other Name cannot be blank', type=str)
    parser.add_argument('username', required=True,
                        help='Username cannot be blank', type=str)
    parser.add_argument('userpassword', required=True,
                        help='Password cannot be blank', type=str)
    parser.add_argument('email', required=True,
                        help='Email cannot be blank', type=str)
    parser.add_argument('phoneNumber', required=True,
                        help='Phone Number cannot be blank', type=int)

    def post(self):
        """HTTP method to post a user"""
        try:
            args = UserRegister.parser.parse_args()
            firstname = args.get('firstname')
            lastname = args.get('lastname')
            othername = args.get('othername')
            phoneNumber = args.get('phoneNumber')
            username = args.get('username')
            email = args.get('email')
            userpassword = args.get('userpassword')
        except Exception as e:
            return {
                "status": 400,
                "error": "Invalid Key error {}".format(e)
            }, 400

        for values in firstname, lastname, othername:
            if not check_name_format(values):
                return {
                    "status": 400,
                    "message":
                    "Name should be 5 character, and contain an Uppercase character"
                }, 400

        if not check_username_format(username):
            return {
                "status": 400,
                "message":
                "Username should be 8 character, and contain an Uppercase character, Integer and a special character"
            }, 400

        if not check_email_format(email):
            return {
                "status": 400,
                "message":
                "Email should be of format",
                "Email Format": "name@company.[com|org|edu]"
            }, 400

        if not check_password_strength(userpassword):
            return {
                "status": 400,
                "message":
                "Password should be 8 character long. Contain special character. Has an Integer. Has a capital letter"
            }, 400

        access_token = create_access_token(identity=args.get('email'))
        renewal_token = create_refresh_token(identity=args.get('email'))

        new_user = user_view.create_user(firstname=args.get('firstname'),
                                         lastname=args.get('lastname'),
                                         othername=args.get('othername'),
                                         phoneNumber=args.get('phoneNumber'),
                                         username=args.get('username'),
                                         email=args.get('email'),
                                         userpassword=userpassword)

        if not new_user:
            return {
                "status": 409,
                "error":
                "duplicate key value violates unique constraint",
                "detail":
                "Key (email) = ({}) already exists.".format(args['email'])
            }, 409

        return {
            "status": 201,
            "Token": access_token,
            "Refresh Token": renewal_token,
            "data": new_user
        }, 201


class UserLogin(Resource):
    """User should be able to login"""

    parser = reqparse.RequestParser()
    parser.add_argument("email", type=str, required=True,
                        help="please input a username")
    parser.add_argument("userpassword", type=str, required=True,
                        help="please input a userpassword")

    def post(self):
        """POST method to login a user"""
        try:
            args = UserLogin.parser.parse_args()
            email = args.get('email')
            userpassword = args.get('userpassword')
        except Exception:
            return {
                "status": 400,
                "error": "Invalid Key error. Should be email and password"
            }, 400

        user_email_exist = user_view.get_user_by_email(email)
        # Returns the user info in a dictionary model

        if not user_email_exist:
            return {
                "status": 404,
                "error": "Email needed to login"
            }, 404

        check_user_password = user_view.validate_password(userpassword, email)

        if not check_user_password:
            return{
                "status": 400,
                "error": "Invalid password. Please provide correct password"
            }, 400

        for data in user_email_exist:
            response = {
                "id": user_email_exist["userid"],
                "username": user_email_exist["username"],
                "is_admin": user_email_exist["isadmin"]
            }

        return{
            "status": 201,
            "data": [{
                "Token": create_access_token(identity=args.get('email')),
                "user": response
            }
            ]
        }, 201
