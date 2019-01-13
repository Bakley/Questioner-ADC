"""Test the user model file and views functionality"""

from . import BaseClassTest
from app.api.v1.models import meetups

meetup_view = meetups.MeetupsModel()
meetup_database = meetups.meetup_models


class TestMeetupRecord(BaseClassTest):
    """Test case for the user model"""

    def test_if_can_save_meetup_record(self):
        """Test if meetup record is being saved"""
        self.meetup1
        self.assertEqual(1, len(meetup_database))
