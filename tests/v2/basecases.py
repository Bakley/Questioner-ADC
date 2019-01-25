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

        self.admin_one = {
            "firstname": "Barclay",
            "lastname": "Koins",
            "othername": "Sofware Dev",
            "phoneNumber": "0703912965",
            "username": "3333333@B",
            "email": "barcls@mails.com",
            "userpassword": "paSsword@2",
            "isAdmin": "true"
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

        self.meetup_one = {
            "location": "Ihub",
            "topic": "Google I/O",
            "tags": ["goggle", "Ihub"]
        }

        self.question_one = {
            "title": "While the be food?",
            "body": "It will be a long day",
            "userId": "3",
            "meetupId": 6
        }

        self.comment_one = {
            "comment": "I love chapati",
            "question": "1"
        }

        self.rspv_one = {
            "response": "No",
            "createdBy": 1,
            "meetupId": 4
        }

        self.rspv_two = {
            "response": "No",
            "createdBy": 1,
            "meetupId": 1
        }

    def admin_login(self):
        """login sample admin"""
        feedback = self.client.post('/auth/v2/login',
                                    data=json.dumps(self.admin_login),
                                    content_type='application/json')
        res = json.loads(feedback.data)
        import pdb
        pdb.set_trace()

        auth_token = res['Token']
        return auth_token

    def user_login(self):
        """login sample user"""
        feedback = self.client.post('/auth/v2/signup',
                                    data=json.dumps(self.user_one),
                                    content_type='application/json')
        res = json.loads(feedback.data)

        auth_token = res['Token']
        return auth_token

    def tearDown(self):
        QuestionerDb.drop_all()
