"""Test the user model file and views functionality"""
import json

from . import BaseClassTest
# from app.api.v1.models import users_models

# user_data = user_models.UserModels()


class TestUserModels(BaseClassTest):
    """Test case for the user model"""

    # def test_if_can_save_a_user(self):
    #     """Test if a user is added to the data structure"""
    #     user = self.user_data.create_user()
    #     self.assertEqual(1, len(user_database))
    #     self.assertTrue(user, list)

    def test_signup(self):
        """"Test if a user can signup"""
        response = self.client.post('/api/v1/auth/user/register',
                                    data=json.dumps(self.user_data),
                                    content_type='application/json')
        result = json.loads(response.data.decode('UTF-8'))
        self.assertEqual(response.status_code, 201)
        self.assertTrue(result["message"], "Successfully registered")
        self.assertNotEqual(response.status_code, 404)

    def test_login(self):
        """Test if a registered user can login"""
        self.client.post('/api/v1/auth/user/register',
                         data=json.dumps(self.user_data),
                         content_type='application/json')
        response = self.client.post('/api/v1/auth/user/login',
                                    data=json.dumps({
                                        "email": "barclay@koin.com",
                                        "password": "Hello@254"
                                    }))

        result = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertTrue(result["message"], "Successfully logged in")
