import unittest
import json
from tests.v2.basecases import TestBaseCase


class AuthLoginTestCase(TestBaseCase):
  """
  test class for the login endpoint
  """

  def test_for_login(self):
    """Test successful login"""
    response = self.client.post('/auth/v2/login',
                                data=json.dumps(self.user_one_login),
                                content_type='application/json')
    self.assertEqual(response.status_code, 201)

  def test_for_login_with_wrong_password(self):
    """Test if user logins in with wrong password"""
    response_1 = self.client.post('/auth/v2/login',
                                  data=json.dumps(self.wrong_password),
                                  content_type='application/json')
    self.assertEqual(response_1.status_code, 400)

  def test_for_key_error(self):
    """Test for a wrong key"""
    response_2 = self.client.post('/auth/v2/login',
                                  data=json.dumps(self.wrong_key),
                                  content_type='application/json')
    self.assertEqual(response_2.status_code, 400)

  def test_login_for_non_existent_user(self):
    """Test if non existent user can login"""
    response_3 = self.client.post('/auth/v2/login',
                                  data=json.dumps(self.non_existent_user),
                                  content_type='application/json')
    self.assertEqual(response_3, 404)
