"""Test the user model file and views functionality"""
import json

from . import BaseClassTest
from app.auth.v1.models import database, User

# user_data = user_models.UserModels()


class TestUserModels(BaseClassTest):
    """Test case for the user model"""

    def test_if_can_save_a_user(self):
        """Test if a user is added to the data structure"""
        user = self.user1.save_user()
        self.assertEqual(1, len(database.users))
        self.assertTrue(user, dict)

    def test_can_delete_user(self):
        """Test successful deletion of user"""
        self.user1.save_user()
        self.assertEqual(1, len(database.users))
        user = User.get_user_by_id(id=1)
        user.delete_user()
        self.assertEqual(0, len(database.users))

    def test_signup(self):
        """"Test if a user can signup"""
        response = self.client.post('/auth/v1/register',
                                    data=json.dumps(self.user_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)
