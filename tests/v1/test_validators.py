import unittest
from app.utilities.validator_functions import (check_for_empty_string,
                                               check_number_format,
                                               check_name_format,
                                               check_username_format,
                                               check_password_strength,
                                               check_email_format)

from app import create_app


class TestValidators(unittest.TestCase):
    """Test case for the validator"""

    def setUp(self):
        """Initialize app and define test variables."""
        self.app = create_app('testing')
        self.client = self.app.test_client()

        self.empty_string = ""
        self.number = 32
        self.name = 'Barclay'
        self.username = 'Koin@254'
        self.password = 'Hello@254'
        self.email = 'barclay@koin.com'

    def test_if_empty_string_pass(self):
        """Test for empty strings"""
        res = check_for_empty_string(self.empty_string)
        self.assertTrue(res, "")

    def test_if_value_is_a_number(self):
        """Test for integers"""
        res = check_number_format(self.number)
        self.assertIsInstance(res, int)

    def test_name(self):
        """Test if name meets requirements"""
        res = check_name_format(self.name)
        self.assertEqual(res, True)
        self.assertGreater(len(self.name), 5)

    def test_for_username(self):
        """Test if username is awesomely chosen"""
        res = check_username_format(self.username)
        self.assertEqual(res, True)

    def test_username_format(self):
        """Test if username meet standards"""
        res = check_username_format(self.username)
        self.assertEqual(res, True)

    def test_password_format(self):
        """Test if password is strong"""
        res = check_password_strength(self.password)
        self.assertEqual(res, True)
        self.assertGreater(len(self.password), 8)

    def test_email_format(self):
        """Test if email is valid"""
        res = check_email_format(self.email)
        self.assertEqual(res, True)
