from flask_restful import Resource, reqparse
from app.api.v1.models import rspvs
from app.utilities.validator_functions import (check_for_empty_string)

rspv_view = rspvs.RspvsModel()


class RspvsResource(Resource):
    """Rspvs class view"""
    parser = reqparse.RequestParser()
    parser.add_argument('status', required=True,
                        help='status cannot be blank', type=str)
    parser.add_argument('topic', required=True,
                        help='topic cannot be blank', type=str)
    parser.add_argument('createdBy', required=True,
                        help='created by cannot be blank', type=int)
    parser.add_argument('meetup', required=True,
                        help='meetup cannot be blank', type=int)

    def post(self, meetup_id):
        """Method to create an RSPV"""
        try:
            args = RspvsResource.parser.parse_args()
            status = args.get('status')
            topic = args.get('topic')
        except Exception:
            return {
                "status": 400,
                "error": "Invalid key error"
            }, 400

        matchers = ["Yes", "No", "Maybe"]

        matching = [
            value for value in status if any(xs in status for xs in matchers)]

        if not matching:
            return {
                "status": 400,
                "error": "Status, can only take Yes, No or Maybe"
            }, 400

        rspv = rspv_view.create_rspv(status=args.get('status'),
                                     topic=args.get('topic'),
                                     meetup=args.get('meetup'),
                                     createdBy=args.get(
            'createdBy')
        )

        return {
            "status": 201,
            "data": rspv,
            "Message": "rspv successfully created"
        }, 201
