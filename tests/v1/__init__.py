"""Test base class"""
import unittest
import json

from app import create_app
from app.auth.v1.models import database, User
from app.api.v1.models.meetups import MeetupsModel


# from app.api.v1.models.question_models import QuestionModels
# from app.api.v1.models.comments_models import CommentsModels
# from app.api.v1.models.meetups_models import MeetupsModels
# from app.api.v1.models.users_models import UsersModels
# from app.api.v1.models.rsvp_models import RsvpModels


class BaseClassTest(unittest.TestCase):
    """This is the base class for test cases."""

    def setUp(self):
        """Initialize app and define test variables."""
        self.app = create_app('testing')
        self.client = self.app.test_client()

        self.admin_data = {
            "id": 1,
            "firstname": "Jared",
            "lastname": "Koin",
            "othername": "Software-coder",
            "email": "barclay@koin.com",
            "phoneNumber": "0712345678",
            "username": "Koin254",
            "registered": "Date",
            "isAdmin": True,
            "password": "Hello@254"
        }

        self.user_data = {
            "id": 2,
            "firstname": "Barclay",
            "lastname": "Koin",
            "othername": "Software-coder",
            "email": "barclay@koin.com",
            "phoneNumber": "0712345678",
            "username": "Koin254",
            "registered": "Date",
            "isAdmin": False,
            "password": "Hello@254"
        }

        self.user1 = User(
            firstname="Derrick",
            lastname="Jones",
            othername="Jupiter",
            email="derick@jones.com",
            phoneNumber="078",
            username="JonesD",
            password="Hello@254"
        )

        self.meetup1 = MeetupsModel().create_meetup(
            location="Ihub",
            topic="Google I/O",
            tags=["Ihub", "Google"]
        )

        self.meetup = {
            "id": 1,
            "createdOn": "Date",
            "location": "Dedan",
            "topic": "Google I/O",
            "happeningOn": "Date",
            "Tags": ["python", "Ihub"],

        }


        self.meetup_1 = {
            "id": 2,
            "createdOn": "Date",
            "location": "Nyeri",
            "topic": "Google I/O",
            "happeningOn": "Date",
            "Tags": ["python", "Ihub"],

        }

        self.meetup_2 = {
            "id": 3,
            "createdOn": "Date",
            "location": "Nakuru",
            "topic": "Google I/O",
            "happeningOn": "Date",
            "Tags": ["python", "Ihub"],

        }

        self.key_error_meetup = {
            "id": 1,
            "createdOn": "Date",
            "location": "Ihub",
            "to": "Google I/O",  # topic
            "happeningOn": "Date",
            "Tags": ["python", "Ihub"],

        }

    def log_in_user(self):
        """Create a user then log in the user"""
        self.client.post('/api/v1/auth/user/register',
                         data=json.dumps(self.user_data),
                         content_type='application/json')
        response = self.client.post('/api/v1/auth/user/login',
                                    data=json.dumps({
                                        "email": "barclay@koin.com",
                                        "password": "Hello@254"
                                    }))
        return response
