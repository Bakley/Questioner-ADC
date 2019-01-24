import unittest
import json
from tests.v2.basecases import TestBaseCase


class AuthTestCase(TestBaseCase):
    """
    test class for the registration endpoint
    """

    def setUp(self):
        TestBaseCase.setUp(self)

    def test_signup(self):
        """Test if a user can signup"""
        response = self.client.post('/auth/v2/signup',
                                    data=json.dumps(self.user_one),
                                    content_type='application/json')

        self.assertEqual(response.status_code, 201)

    def test_signup_with_wrong_name_format(self):
        """Test if a user can signup"""
        response2 = self.client.post('/auth/v2/signup',
                                     data=json.dumps(
                                         self.user_one_name_format),
                                     content_type='application/json')
        res = json.loads(response2.data.decode())

        self.assertEqual(response2.status_code, 400)
        self.assertEqual(
            res["message"],
            "Name should be 5 character, and contain an Uppercase character")

    def test_for_dupicate_registery(self):
        """Test if a user can register twice"""
        response1 = self.client.post('/auth/v2/signup',
                                     data=json.dumps(self.user_one),
                                     content_type='application/json')

        self.assertEqual(response1.status_code, 201)

        duplicate_signup = self.client.post('/auth/v2/signup',
                                            data=json.dumps(self.user_one),
                                            content_type='application/json')
        res = json.loads(duplicate_signup.data.decode())
        self.assertEqual(duplicate_signup.status_code, 409)
        self.assertEqual(
            res["error"], "duplicate key value violates unique constraint")

    def test_signup_with_wrong_username_format(self):
        """Test if a user can signup"""
        response3 = self.client.post('/auth/v2/signup',
                                     data=json.dumps(self.user_two),
                                     content_type='application/json')
        res = json.loads(response3.data.decode())
        self.assertEqual(response3.status_code, 400)
        self.assertEqual(
            res["message"],
            "Username should be 8 character, and contain an Uppercase character, Integer and a special character")

    def test_signup_password_strength(self):
        """Test if a user can signup"""
        response4 = self.client.post('/auth/v2/signup',
                                     data=json.dumps(self.user_four),
                                     content_type='application/json')
        res = json.loads(response4.data.decode())

        self.assertEqual(response4.status_code, 400)
        self.assertEqual(res["message"],
                         "Password should be 8 character long. Contain special character. Has an Integer. Has a capital letter")

    def test_email_format(self):
        """Test if a user can signup"""
        response5 = self.client.post('/auth/v2/signup',
                                     data=json.dumps(self.user_three),
                                     content_type='application/json')
        res = json.loads(response5.data.decode())

        self.assertEqual(response5.status_code, 400)
        self.assertEqual(
            res["message"], "Email should be of format")
        self.assertEqual(
            res["Email Format"], "name@company.[com|org|edu]")


if __name__ == "__main__":
    unittest.main()
