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
        response2 = self.client.post('/auth/v2/signup',
                                     data=json.dumps(self.user_one),
                                     content_type='application/json')
        self.assertEqual(response2.status_code, 201)

    def test_for_dupicate_registery(self):
        """Test if a user can register twice"""
        response1 = self.client.post('/auth/v2/signup',
                                     data=json.dumps(self.user_two),
                                     content_type='application/json')
        self.assertEqual(response1.status_code, 201)

        duplicate_signup = self.client.post('/auth/v2/signup',
                                            data=json.dumps(self.user_two),
                                            content_type='application/json')
        self.assertEqual(duplicate_signup.status_code, 409)


if __name__ == "__main__":
    unittest.main()
