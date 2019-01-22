"""Meetup views file"""
from flask_restful import Resource, reqparse
from datetime import datetime
from app.utilities.auth_token_generator import token_required, admin_required
from app.api.v2.models import meetup_models
from app.utilities.validator_file import (check_for_empty_string)

meetup_views = meetup_models.MeetupsModel()


class MeetupViewsResource(Resource):
    """Create and Delete a meetup"""
    parser = reqparse.RequestParser()
    parser.add_argument('location', required=True,
                        help='Location cannot be blank', type=str)
    parser.add_argument('topic', required=True,
                        help='topic cannot be blank', type=str)
    parser.add_argument('tags',
                        help='Tags cannot be blank', action='append')
    # @admin_required

    def post(self):
        """Admin create a meetup"""
        try:
            # userid = current_user['email']
            args = MeetupViewsResource.parser.parse_args()
            location = args.get('location')
            topic = args.get('topic')
            tags = args.get('tags')
            happeninon = args.get('happeningon')
        except Exception:
            return {
                "status": 400,
                "error":
                "Invalid Key field. Missing or wrongly spelled Keys, should be location, topic tags and happeningon"
            }, 400

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

        meetup = meetup_views.create_meetup(
            userid=args.get('userid'),
            location=args.get('location'),
            topic=args.get('topic'),
            tags=args.get('tags'),
            happeningon=args.get('happeningon'))

        return {
            "status": 201,
            "data": meetup,
            "Message": "meetup successfully created"
        }, 201


class SpecificMeetup(Resource):
    """Get a specific meetup"""

    def get(self, meetup_id):
        """Method to get a specific meetup"""
        try:
            meetup_id = int(meetup_id)
        except Exception:
            return {
                "status": 404,
                "error": "Url need an integer"
            }, 404
        new_meetup = meetup_views.get_a_specific_meetup(id=meetup_id)
        if not new_meetup:
            return {
                "status": 404,
                "error": "Meetup of id {} not found".format(meetup_id)
            }, 404
        return {
            "status": 200,
            "data": new_meetup
        }, 200
