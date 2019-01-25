import json
from tests.v2.basecases import TestBaseCase


class RSpvsTestCase(TestBaseCase):
    """
    test class for the comment endpoint
    """

    def test_rspv_created_with_str(self):
        """Test if a comment is posted"""
        auth_token = self.user_login()

        response = self.client.post('/api/v2/meetups/<meetup_id>/rspv',
                                    data=json.dumps(self.rspv_one),
                                    headers=dict(
                                        Authorization="Bearer " + auth_token),
                                    content_type='application/json')
        res = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            res["error"],
            "Resource Identifier need an integer")

    def test_rspv_created_with_none_meetup(self):
        """Test if a rspv is posted"""
        auth_token = self.user_login()

        response = self.client.post('/api/v2/meetups/1/rspv',
                                    data=json.dumps(self.rspv_one),
                                    headers=dict(
                                        Authorization="Bearer " + auth_token),
                                    content_type='application/json')
        res = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            res["error"],
            "The meetup you entered is not found. Please pass same meetup on your URL")

    def test_get_rspv_with_str(self):
        """Test if you get an rspv is posted"""
        auth_token = self.user_login()

        response = self.client.get('/api/v2/rspv/<rspv_id>',
                                   headers=dict(
                                       Authorization="Bearer " + auth_token),
                                   content_type='application/json')
        res = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            res["error"],
            "Url need an integer")

    def test_get_rspv(self):
        """Test if you get an rspv is posted"""
        auth_token = self.user_login()

        response = self.client.get('/api/v2/rspv/1',
                                   headers=dict(
                                       Authorization="Bearer " + auth_token),
                                   content_type='application/json')
        res = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            res["error"],
            "RSPV of id 1 not found")
