import unittest

from flask import current_app

from app import create_app


class TestDevelopmentConfig(unittest.TestCase):
    def creation_of_app(self):
        app = create_app('development')
        return app

    def test_app_is_development(self):
        self.assertTrue('DEBUG')
        self.assertFalse(current_app is None)


class TestTestingConfig(unittest.TestCase):
    def creation_of_app(self):
        app = create_app('testing')
        return app

    def test_app_is_testing(self):
        self.assertTrue('DEBUG')


class TestProductionConfig(unittest.TestCase):
    def creation_of_app(self):
        app = create_app('production')
        return app

    def test_app_is_production(self):
        self.assertTrue('DEBUG')


if __name__ == '__main__':
    unittest.main()
