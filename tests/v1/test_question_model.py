"""Test the user model file and views functionality"""
import unittest

from app import create_app
from app.api.v1.models.questions import QuestionsModel, questions


class TestQuestionRecord(unittest.TestCase):
    """Test case for the user model"""

    def setUp(self):
        """Initialize app and define test variables."""
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.question1 = QuestionsModel().create_question(
            createdBy="1",
            meetup=1,
            title="food",
            body="will there be food"
        )

    def test_if_can_save_question_record(self):
        """Test if question record is being saved"""
        self.question1
        self.assertEqual(2, len(questions))

    def test_get_all_question_model(self):
        """Test if the get_all_questions method works"""
        pass
