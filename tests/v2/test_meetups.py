import unittest
import json
from tests.v2.basecases import TestBaseCase


class MeetupTestCase(TestBaseCase):
    """
    test class for the meetup endpoint
    """

    def test_user_create_a_meetup(self):
        """Test user getting a meetup"""
        auth_token = self.user_login()

        response = self.client.post('/api/v2/meetups',
                                    data=json.dumps(self.meetup_one),
                                    headers=dict(
                                        Authorization="Bearer " + auth_token),
                                    content_type='application/json')
        res = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 403)
        self.assertEqual(
            res["message"],
            "You are not authorized to create a meetup")

    def test_user_delete_a_meetup(self):
        """Test user deleting a meetup"""
        auth_token = self.user_login()

        response = self.client.delete('/api/v2/meetups/<meetup_id>',
                                      data=json.dumps(self.meetup_one),
                                      headers=dict(
                                          Authorization="Bearer " + auth_token),
                                      content_type='application/json')
        res = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 403)
        self.assertEqual(
            res["message"],
            "You are not authorized to delete a meetup")

    def test_user_getting_a_meetup(self):
        """Test user deleting a meetup"""
        auth_token = self.user_login()

        response = self.client.get('/api/v2/meetups/1',
                                   data=json.dumps(self.meetup_one),
                                   headers=dict(
                                       Authorization="Bearer " + auth_token),
                                   content_type='application/json')
        res = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            res["error"],
            "Meetup of id 1 not found")

    def test_user_getting_a_meetup_with_str(self):
        """Test user deleting a meetup"""
        auth_token = self.user_login()

        response = self.client.get('/api/v2/meetups/g',
                                   data=json.dumps(self.meetup_one),
                                   headers=dict(
                                       Authorization="Bearer " + auth_token),
                                   content_type='application/json')
        res = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            res["error"],
            "Resource Identifier need an integer")
