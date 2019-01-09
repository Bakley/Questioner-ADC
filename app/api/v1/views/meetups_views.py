"""Meetup views file"""

from flask import Flask
from flask_restful import Resource, reqparse
from app.api.vi.models import meetups


class MeetupResource(Resource):
    """Meetup class"""
    parser = reqparse.RequestParser()
    parser.add_argument('location', required=True,
                        help='Location cannot be blank', type=str)
    parser.add_argument('topic', required=True,
                        help='topic cannot be blank', type=str)
    parser.add_argument('tags', required=True,
                        help='Tags cannot be blank', type=int, action='append')

    def post(self):
        args = MeetupResource.parser.parse_args()
        location = args.get('location')
        topic = args.get('topic')
        tags = args.get('tags')

        meetup = meetups.MeetupModels(location=args.get('firstname'),
                                      topic=args.get('topic'), tags=args.get('tags'))
        meetup = meetups.create_meetup()

        return {
            "status": 201,
            "data": {
                "message": "meetup successfully created",
                "meetup": meetup
            }
        }

    def get(self):
        pass

    def delete(self):
        pass
