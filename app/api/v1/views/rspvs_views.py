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
                                     createdBy=args.get(
            'createdBy')
        )
        print(rspv)
        if not rspv:
            return {
                "status": 404,
                "error": "No meetup found to RSPV for"
            }, 404

        return {
            "status": 201,
            "data": rspv,
            "Message": "rspv successfully created"
        }, 201


class GetRspvs(Resource):
    """Class to get all RSPVS"""

    def get(self):
        """Method to get all the RSPVS created"""
        rspv = rspv_view.get_all_rspvs()
        if not rspv:
            return {
                "status": 404,
                "error": "No upcoming rspv yet"
            }, 404
        return {
            "status": 200,
            "data": rspv
        }, 200
