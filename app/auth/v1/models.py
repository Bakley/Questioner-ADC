from datatime import datatime, timedelta
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
        self.comments = {}
        self.rspvs = {}

    def drop(self):
        self.__init__()


database = MockDb()
