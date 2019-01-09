from datetime import datetime, timedelta
from flask import current_app
import jwt
from werkzeug.security import generate_password_hash, check_password_hash


class MockDb():
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


class User():
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
        database.users.update({self.isAdmin: self})
        return self.vie

    def view(self):
        """Method to jsonify user objects"""
        keys = ["firstname", "lastname", "othername",
                "email", "phoneNumber", "username"]
        return {key: getattr(self, keys) for key in keys}
