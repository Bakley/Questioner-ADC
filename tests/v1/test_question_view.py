"""Test the views functionality"""
import unittest
import json

from app import create_app
from app.api.v1.models.questions import QuestionsModel, questions


class TestQuestionRecordViews(unittest.TestCase):
    """Test case for the user model"""

    def setUp(self):
        """Initialize app and define test variables."""
        self.app = create_app('testing')
        self.client = self.app.test_client()

        self.question = {
            "id": 1,
            "createdOn": "Date",
            "createdBy": 1,
            "title": "Food",
            "body": "Will there be food?",
            "votes": 0

        }

        self.question__missing_key = {
            "id": 1,
            "createdOn": "Date",
            "createdBy": 1,
            "title": "Food",
            "body": "",
            "votes": 0

        }

        self.question_wrong_key = {
            "id": 1,
            "createdOn": "Date",
            "createBy": 1,  # should be createdBy
            "title": "Food",
            "body": "Will there be food?",
            "votes": 0
        }

        self.meetup_1 = {
            "id": 2,
            "createdOn": "Date",
            "location": "Nyeri",
            "topic": "Google I/O",
            "happeningOn": "Date",
            "Tags": ["python", "Ihub"],

        }

    def test_post_a_question(self):
        """Test if the post view works"""

        response = self.client.post('/api/v1/meetups',
                                    data=json.dumps(self.meetup_1),
                                    content_type='application/json')
        response = self.client.post('/meetups/1/questions',
                                    data=json.dumps(self.question),
                                    content_type='application/json')
        print(response)
        self.assertEqual(response.status_code, 404)

    def test_post_a_question_with_wrong_key(self):
        """Test if the post view will return error if a key is misspelled"""
        response = self.client.post('/meetups/1/questions',
                                    data=json.dumps(self.question_wrong_key),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_question_post_with_missing_value(self):
        """Test if missing value will output an error"""
        response = self.client.post('/meetups/1/questions',
                                    data=json.dumps(
                                        self.question__missing_key),
                                    content_type='application/json')

        self.assertEqual(response.status_code, 404)

    def test_get_a_question(self):
        """Test if the we can get a specific meetup"""
        response = self.client.get('/api/v1/questions/1',
                                   content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_get_all_question(self):
        """Test if the we can get all question records"""
        response = self.client.get('/api/v1/questions/upcoming',
                                   content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_patch_upvote(self):
        """Test if the upvote patch works"""
        response_patch_upvote = self.client.patch(
            '/api/v1/questions/1/upvote',)
        res_data = json.loads(response_patch_upvote.data.decode())
        self.assertEqual(response_patch_upvote.status_code, 200)

    def test_patch_downvote(self):
        """Test if the downvote patch works"""
        response_patch_downvote = self.client.patch(
            '/api/v1/questions/1/downvote',)
        res_data = json.loads(response_patch_downvote.data.decode())

        self.assertEqual(response_patch_downvote.status_code, 200)
