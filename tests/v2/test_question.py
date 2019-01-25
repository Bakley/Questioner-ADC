import unittest
import json
from tests.v2.basecases import TestBaseCase


class QuestionTestCase(TestBaseCase):
    """
    test class for the question endpoint
    """

    def test_user_posting_a_question_with_str(self):
        """Test user posting a question to no meetup"""
        auth_token = self.user_login()

        response = self.client.post('/api/v2/meetups/<meetup_id>/questions',
                                    data=json.dumps(self.question_one),
                                    headers=dict(
                                        Authorization="Bearer " + auth_token),
                                    content_type='application/json')
        res = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            res["error"],
            "Resource Identifier need an integer")

    def test_user_getting_a_none_question(self):
        """Test user posting a question to no meetup"""
        auth_token = self.user_login()

        response = self.client.post('/api/v2/meetups/1/questions',
                                    data=json.dumps(self.question_one),
                                    headers=dict(
                                        Authorization="Bearer " + auth_token),
                                    content_type='application/json')
        res = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            res["error"],
            "Meetup of id 1 not found")

    def test_user_patch_a_none_question(self):
        """Test user upvote"""
        auth_token = self.user_login()

        response = self.client.patch('/api/v2/questions/1/upvote',
                                     data=json.dumps(self.question_one),
                                     headers=dict(
                                         Authorization="Bearer " + auth_token),
                                     content_type='application/json')
        res = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            res["error"],
            "No question found")

    def test_downvote_patch_a_none_question(self):
        """Test user downvote"""
        auth_token = self.user_login()

        response = self.client.patch('/api/v2/questions/1/downvote',
                                     data=json.dumps(self.question_one),
                                     headers=dict(
                                         Authorization="Bearer " + auth_token),
                                     content_type='application/json')
        res = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            res["error"],
            "No question found")
