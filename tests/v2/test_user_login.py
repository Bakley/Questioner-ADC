import unittest
import json
from tests.v2.basecases import TestBaseCase


class AuthLoginTestCase(TestBaseCase):
    """
    test class for the login endpoint
    """

    def test_for_login(self):
        """Test successful login"""
        # Sign up first
        signup_res = self.client.post('/auth/v2/signup',
                                      data=json.dumps(self.user_one),
                                      content_type='application/json')

        self.assertEqual(signup_res.status_code, 201)

        # Login user
        response = self.client.post('/auth/v2/login',
                                    data=json.dumps(self.user_one_login),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_for_login_with_wrong_password(self):
        """Test if user logins in with wrong password"""
        # sign user first
        signup_res2 = self.client.post('/auth/v2/signup',
                                       data=json.dumps(self.user_one),
                                       content_type='application/json')
        self.assertEqual(signup_res2.status_code, 201)

        # Login with wrong password
        response_1 = self.client.post('/auth/v2/login',
                                      data=json.dumps(self.wrong_password),
                                      content_type='application/json')

        res = json.loads(response_1.data.decode())

        self.assertEqual(response_1.status_code, 400)
        self.assertEqual(
            res["error"],
            "Invalid password. Please provide correct password")

    def test_for_key_error(self):
        """Test for a wrong key"""

        # sign user first
        signup_res2 = self.client.post('/auth/v2/signup',
                                       data=json.dumps(self.user_one),
                                       content_type='application/json')
        self.assertEqual(signup_res2.status_code, 201)

        response_2 = self.client.post('/auth/v2/login',
                                      data=json.dumps(self.wrong_key),
                                      content_type='application/json')

        res = json.loads(response_2.data.decode())
        self.assertEqual(response_2.status_code, 400)
        self.assertEqual(
            res["error"],
            "Invalid Key error. Should be email and password")

    def test_login_for_non_existent_user(self):
        """Test if non existent user can login"""
        response_3 = self.client.post('/auth/v2/login',
                                      data=json.dumps(self.non_existent_user),
                                      content_type='application/json')
        res = json.loads(response_3.data.decode())
        self.assertEqual(res["status"], 404)
        self.assertEqual(
            res["error"],
            "Email needed to login")
