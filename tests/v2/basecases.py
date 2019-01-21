"""Base test class"""
import unittest
import json
from app import create_app
from app.api.v2.dbmodel import QuestionerDb


class TestBaseCase(unittest.TestCase):
    """Base Testing Class."""

    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.client.testing = True

        self.user_one = {
            "firstname": "Barclay",
            "lastname": "Koin",
            "othername": "Sofware Dev",
            "phoneNumber": "0703912965",
            "username": "Koin253",
            "email": "barclay@koin.com",
            "userpassword": "password"
        }

        self.user_two = {
            "firstname": "Derrick",
            "lastname": "Koin",
            "othername": "Software Dev",
            "phoneNumber": "0703912965",
            "username": "Koin254",
            "email": "derrick@koin.com",
            "userpassword": "password"
        }

        self.user_one_login = {
            "email": "barclay@koin.com",
            "userpassword": "password"
        }

        self.non_existent_user = {
            "email": "bar@clay.com",
            "userpassword": "password"
        }

        self.wrong_password = {
            "email": "barclay@koin.com",
            "userpassword": "password123"
        }

        self.wrong_key = {
            "emal": "barclay@koin.com",
            #  should be email
            "userpassword": "password"
        }

    def tearDown(self):
        QuestionerDb.drop_all()
