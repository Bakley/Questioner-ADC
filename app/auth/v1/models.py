from datetime import datetime, timedelta
from flask import current_app
import jwt
from werkzeug.security import generate_password_hash, check_password_hash


class MockDb:
    """Data structure database"""

    def __init__(self):
        """Initializes the mock database"""
        self.users = {}
        self.meetups = {}
        self.questions = {}
        self.user_count = 0
        self.meetups_count = 0
        self.questions_count = 0

    def drop(self):
        self.__init__()


database = MockDb()


class User:
    """User class model"""

    def __init__(self, firstname, lastname, othername, email,
                 phoneNumber, username, password):
        """Initializes the user details"""
        self.id = None
        self.firstname = firstname
        self.lastname = lastname
        self.othername = othername
        self.email = email
        self.phoneNumber = phoneNumber
        self.username = username
        self.password = generate_password_hash(password)
        self.registered = datetime.utcnow().isoformat()
        self.isAdmin = False

    def save_user(self):
        """Method to save user to the database"""
        setattr(self, 'id', database.user_count + 1)
        database.users.update({self.id: self})
        database.user_count += 1
        return self.view

    def save_admin(self):
        """Method to register an Admin"""
        setattr(self, 'isAdmin', True)
        setattr(self, 'id', database.user_count + 1)
        database.users.update({self.isAdmin: self})
        database.users.update({self.id: self})
        database.user_count += 1
        return self.view

    def view(self):
        """Method to jsonify user objects"""
        keys = ["id", "firstname", "lastname", "othername",
                "email", "phoneNumber", "username", "isAdmin"]
        return {key: getattr(self, keys) for key in keys}

    def validate_password(self, password):
        """Method for validating password"""
        if check_password_hash(self.password, password):
            return True
        return False

    def delete_user(self):
        """Method for deleting a user"""
        del database.users[self.id]

    @classmethod
    def get_user_by_id(cls, id):
        """Method for getting user by id"""
        user = database.users.get(id)
        if not user:
            return {'message': 'User does not exist.'}
        return user

    @classmethod
    def get_user_by_email(cls, email):
        """Method for getting user by email"""
        for id_ in database.users:
            user = database.users.get(id_)
            if user.email == email:
                return user
        return None

    def generate_token(self):
        """Method for generating token upon login"""
        try:
            payload = {
                'exp': datetime.utcnow() + timedelta(minutes=5),
                'iat': datetime.utcnow(),
                'id': self.id
            }
            token = jwt.encode(
                payload,
                current_app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
            return token
        except Exception as err:
            return str(err)

    @staticmethod
    def decode_token(token):
        """Method for decoding token generated"""
        payload = jwt.decode(token, str(
            current_app.config.get('SECRET')), algorithms=['HS256'])
        return payload
