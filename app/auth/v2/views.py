from flask_restful import Resource, reqparse
from app.auth.v2.models import UserModel
import json
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
                "status": 404,
                "error": "Invalid Key error. Should be email and password"
            }, 404

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

        auth_token = user_view.generate_token(user_email_exist['email'])

        if not auth_token:
            return {
                "status": 404,
                "error": "Token generation failed"
            }, 404

        for data in user_email_exist:
            response = {
                "id": user_email_exist["userid"],
                "username": user_email_exist["username"],
                "registered": user_email_exist["registered"]
            }

        return{
            "status": 201,
            "data": [{
                "token": auth_token.decode('UTF-8'),
                "user": response
            }
            ]
        }, 201
