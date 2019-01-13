"""Test the meetup views functionality"""
import json

from . import BaseClassTest
from app.api.v1.models import meetups

meetup_view = meetups.MeetupsModel()
meetup_database = meetups.meetup_models


class TestMeetupRecord(BaseClassTest):
    """Test case for the user model"""

    def test_post_a_meetup(self):
        """Test if the post view works"""
        response = self.client.post('/api/v1/meetups',
                                    data=json.dumps(self.meetup),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_get_a_meetup(self):
        """Test if the we can get a specific meetup"""
        response_get = self.client.get('/api/v1/meetups/1',
                                       content_type='application/json')
        self.assertEqual(response_get.status_code, 200)

    def test_get_all_meetup(self):
        """Test if the we can get all meetup records"""
        response_get_all = self.client.get('/api/v1/meetups/upcoming',
                                           content_type='application/json')
        self.assertEqual(response_get_all.status_code, 200)

    def test_delete_a_meetup(self):
        """Test if a meetup is deleted"""
        # make a record first
        self.client.post('/api/v1/meetups',
                         data=json.dumps(self.meetup),
                         content_type='application/json')

        # Delete the record
        response_delete = self.client.delete('/api/v1/meetups/<int:meetup_id>',
                                             content_type='application/json')
        self.assertEqual(response_delete.status_code, 404)
