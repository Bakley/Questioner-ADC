"""Base test class"""
import unittest
import json
from app import create_app
from app.api.v2.dbmodel import QuestionerDb


class TestBaseCase(unittest.TestCase):
    """Base Testing Class."""

    def setUp(self):
        app = create_app('testing')
        app.app_context().push()

        self.client = app.test_client()
        self.client.testing = True
        with app.app_context():
            QuestionerDb().init_db(app.config['DATABASE_URI'])
            QuestionerDb().build_all()

        self.user_one = {
            "firstname": "Barclay",
            "lastname": "Koins",
            "othername": "Sofware Dev",
            "phoneNumber": "0703912965",
            "username": "3333333@B",
            "email": "barcls@mails.com",
            "userpassword": "paSsword@2"
        }

        self.user_one_name_format = {
            "firstname": "Barclay",
            "lastname": "Koin",
            "othername": "Sofware@2Dev",
            "phoneNumber": "0703912965",
            "username": "Koin253",
            "email": "barclay@koin.com",
            "userpassword": "password"
        }

        self.user_two = {
            "firstname": "Derrick",
            "lastname": "Koins",
            "othername": "3333333@C",
            "phoneNumber": "0703912965",
            "username": "Koin254",
            "email": "derrickkoin.com",
            "userpassword": "pA@5word"
        }

        self.user_three = {
            "firstname": "Derrick",
            "lastname": "Koins",
            "othername": "3333333@C",
            "phoneNumber": "0703912965",
            "username": "3333333@B",
            "email": "derrickkoin.com",
            "userpassword": "pA@5word"
        }

        self.user_four = {
            "firstname": "Barclay",
            "lastname": "Koins",
            "othername": "Sofware Dev",
            "phoneNumber": "0703912965",
            "username": "3333333@B",
            "email": "barcls@mails.com",
            "userpassword": "paSswo"
        }
        self.user_one_login = {
            "email": "barcls@mails.com",
            "userpassword": "paSsword@2"
        }

        self.admin_log = {
            "email": "super@admin.com",
            "userpassword": "Admin@254"
        }

        self.non_existent_user = {
            "email": "bar@clay.com",
            "userpassword": "password"
        }

        self.wrong_password = {
            "email": "barcls@mails.com",
            "userpassword": "paSsword@245"
        }

        self.wrong_key = {
            "emal": "barclay@koin.com",
            #  should be email
            "userpassword": "password"
        }

    def admin_login(self):
        """login sample admin"""
        feedback = self.app.post('api/v2/auth/login',
                                 data=json.dumps(self.admin_log),
                                 content_type='application/json')
        res = json.loads(feedback.data)
        auth_token = res['auth']
        print(auth_token)
        return auth_token

    def tearDown(self):
        QuestionerDb.drop_all()
