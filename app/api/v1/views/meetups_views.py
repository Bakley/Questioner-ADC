"""Meetup views file"""

from flask import Flask
from flask_restful import Resource, reqparse
from app.api.v1.models import meetups

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
        args = MeetupResource.parser.parse_args()
        location = args.get('location')
        topic = args.get('topic')
        tags = args.get('tags')

        meetup = meetup_view.create_meetup(location=args.get('location'),
                                           topic=args.get('topic'),
                                           tags=args.get('tags'))

        return {
            "status": 201,
            "data": meetup,
            "Message": "meetup successfully created"
        }

    def get(self, meetup_id):
        meetup = meetup_view.get_a_specific_meetup(id=meetup_id)
        if not meetup:
            return {
                "status": 404,
                "error": "Meetup of id {} not found".format(meetup_id)
            }
        return {
            "status": 200,
            "data": meetup
        }

    def delete(self):
        pass
