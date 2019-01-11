"""User model views"""
from flask_restful import Resource, reqparse
from app.auth.v1.models import User


class SignupResource(Resource):
    """User registration resource"""
    parser = reqparse.RequestParser()
    parser.add_argument('firstname', required=True,
                        help='First Name cannot be blank', type=str)
    parser.add_argument('lastname', required=True,
                        help='Last Name cannot be blank', type=str)
    parser.add_argument('othername', required=True,
                        help='Other Name cannot be blank', type=str)
    parser.add_argument('phoneNumber', required=True,
                        help='Phone Number cannot be blank', type=int)
    parser.add_argument('username', required=True,
                        help='Username cannot be blank', type=str)
    parser.add_argument('email', required=True,
                        help='Email cannot be blank', type=str)
    parser.add_argument('password', required=True,
                        help='Password cannot be blank', type=str)

    def post(self):
        args = SignupResource.parser.parse_args()
        firstname = args.get('firstname')
        lastname = args.get('lastname')
        othername = args.get('othername')
        phoneNumber = args.get('phoneNumber')
        username = args.get('username')
        email = args.get('email')
        password = args.get('password')

        email_exists = User.get_user_by_email(email=args['email'])

        if email_exists:
            return {
                "error": "A user with that email already exists.",
                "status": 409,
            }, 409

        user = User(firstname=args.get('firstname'),
                    lastname=args.get('lastname'),
                    othername=args.get('othername'),
                    phoneNumber=args.get('phoneNumber'),
                    username=args.get('username'),
                    email=args.get('email'),
                    password=password)
        user = user.save_user()
        print(user.__dict__)

        return {
            "status": 201,
            "data": {
                "message": "Successfully registered",
                "user": user.__dict__
            }
        }, 201

    def get(self, id):
        pass

    def delete(self):
        pass
