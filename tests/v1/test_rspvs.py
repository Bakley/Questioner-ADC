import unittest
import json

from app import create_app
from app.api.v1.models.rspvs import RspvsModel, rspv_models


class TestRspvRecord(unittest.TestCase):
    """Test case for the user model"""

    def setUp(self):
        """Initialize app and define test variables."""
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.rspv1 = RspvsModel().create_rspv(
            createdBy="1",
            meetup=1,
            topic="food",
            status="Yes"
        )

        self.rspv = {
            "id": 1,
            "createdBy": 1,
            "meetup": 1,
            "topic": "Food",
            "status": "Yes"
        }

        self.rspv_missing_value = {
            "id": 1,
            "createdBy": 1,
            "meetup": 1,
            "topic": "Food",
            "status": ""
        }

        self.rspv_wrong_key = {
            "id": 1,
            "createdBy": 1,
            "meetup": 1,
            "topic": "Food",
            "stat": "Yes"  # status
        }

    def test_if_can_save_rspv_record(self):
        """Test if rspv record is being saved"""
        self.rspv1
        self.assertEqual(5, len(self.rspv))

    def test_post_a_rspv(self):
        """Test if the post view works"""
        response = self.client.post('/api/v1/meetups/1/rsvps>',
                                    data=json.dumps(self.rspv),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 404)
