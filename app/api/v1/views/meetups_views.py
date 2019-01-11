"""Meetup views file"""

from flask_restful import Resource, reqparse
from app.api.v1.models import meetups
from app.utilities.validator_functions import (check_number_format,
                                               check_name_format,
                                               check_username_format,
                                               check_password_strength,
                                               check_email_format,
                                               check_for_empty_string)


meetup_view = meetups.MeetupsModel()


class MeetupResource(Resource):
    """Meetup class"""
    parser = reqparse.RequestParser()
    parser.add_argument('location', required=True,
                        help='Location cannot be blank', type=str)
    parser.add_argument('topic', required=True,
                        help='topic cannot be blank', type=str)
    parser.add_argument('tags',
                        help='Tags cannot be blank', action='append')

    def post(self):
        try:
            args = MeetupResource.parser.parse_args()
            location = args.get('location')
            topic = args.get('topic')
            tags = args.get('tags')
        except Exception as e:
            return {
                "status": 404,
                "error": "Invalid Key field"
            }, 404

        meetup = meetup_view.create_meetup(location=args.get('location'),
                                           topic=args.get('topic'),
                                           tags=args.get('tags'))

        return {
            "status": 201,
            "data": meetup,
            "Message": "meetup successfully created"
        }, 201

    def get(self):
        """Method to get all upcoming meetups"""
        meetup = meetup_view.get_all_meetups()
        if not meetup:
            return {
                "status": 404,
                "error": "No upcoming meetup yet"
            }, 404
        return {
            "status": 200,
            "data": meetup
        }, 200

    def delete(self):
        pass


class AllMeetupResource(Resource):
    """Class to get all meetups created"""

    def get(self, meetup_id):
        """Method to get a specific meetup"""
        meetup = meetup_view.get_a_specific_meetup(id=meetup_id)
        if not meetup:
            return {
                "status": 404,
                "error": "Meetup of id {} not found".format(meetup_id)
            }, 404
        return {
            "status": 200,
            "data": meetup
        }, 200
