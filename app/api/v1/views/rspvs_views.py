from flask_restful import Resource, reqparse
from app.api.v1.models import rspvs
from app.api.v1.models import meetups

rspv_view = rspvs.RspvsModel()
meetup_rsvp_view = meetups.MeetupsModel()


class RspvsResource(Resource):
    """Rspvs class view"""
    parser = reqparse.RequestParser()
    parser.add_argument('status', required=True,
                        help='status cannot be blank', type=str)
    parser.add_argument('createdBy', required=True,
                        help='created by cannot be blank', type=int)

    def post(self, meetup_id):
        """Method to create an RSPV"""

        # Get a meetup

        meetup = meetup_rsvp_view.get_a_specific_meetup(id=meetup_id)
        print(meetup)
        if not meetup:
            return {
                "status": 404,
                "error":
                "No meetup of id {} found to RSPV for".format(meetup_id)
            }, 404

        args = RspvsResource.parser.parse_args()
        status = args.get('status')

        matchers = ["Yes", "No", "Maybe"]

        matching = [
            value for value in status if any(index in status for index in matchers)]

        if not matching:
            return {
                "status": 400,
                "error": "Status, can only take Yes, No or Maybe"
            }, 400

        rspv = rspv_view.create_rspv(status=args.get('status'),
                                     createdBy=args.get(
            'createdBy')
        )
        # Get the required output
        for values in rspv and meetup:
            r = [{
                 "meetup": meetup[0]["id"],
                 "status": rspv["status"],
                 "topic": meetup[0]["topic"]
                 }]

        return {
            "status": 201,
            "data": r,
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
