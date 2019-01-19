"""Meetup views file"""

from flask_restful import Resource, reqparse
from app.api.v1.models import meetups
from app.utilities.validator_functions import (check_for_empty_string)


meetup_view = meetups.MeetupsModel()


class MeetupResource(Resource):
    """Meetup class view"""
    parser = reqparse.RequestParser()
    parser.add_argument('location', required=True,
                        help='Location cannot be blank', type=str)
    parser.add_argument('topic', required=True,
                        help='topic cannot be blank', type=str)
    parser.add_argument('tags',
                        help='Tags cannot be blank', action='append')

    def post(self):
        """Creation of a meetup POST"""
        try:
            args = MeetupResource.parser.parse_args()
            location = args.get('location')
            topic = args.get('topic')
            tags = args.get('tags')
        except Exception:
            return {
                "status": 400,
                "error": "Invalid Key field. Missing or wrongly spelled Keys, should be location, topic and tags"
            }, 400

        # Check if user values inputted are empty

        if check_for_empty_string(location):
            return {
                "status": 400,
                "error":
                "Please provide a location for the meetup"
            }, 400

        if check_for_empty_string(topic):
            return {
                "status": 400,
                "error":
                "Please provide a topic for the Meetup"
            }, 400

        # check if a location already exist

        location_exists = meetup_view.get_a_meetup_by_loaction(
            location=args['location'])

        if location_exists:
            return {
                "error": "A meetup with that location already exists.",
                "status": 400,
            }, 400
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


class AllMeetupResource(Resource):
    """Class to get a meetups created"""

    def get(self, meetup_id):
        """Method to get a specific meetup"""
        try:
            meetup_id = int(meetup_id)
        except Exception:
            return {
                "status": 404,
                "error": "Url need an integer"
            }, 404

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

    def delete(self, meetup_id):
        """Method to delete a meetup"""
        meetup = meetup_view.get_a_specific_meetup(id=meetup_id)
        if not meetup:
            return {
                "status": 404,
                "error": "Meetup of id {} not found".format(meetup_id)
            }, 404

        meetups.meetup_models.remove(meetup)
        return {
            "status": 404,
            "Message":
            "Successfully delete meetup with meetup_id of {}".format(meetup_id)
        }, 204
