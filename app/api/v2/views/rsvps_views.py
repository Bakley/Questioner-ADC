"""RSPVS views file"""
import json
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from app.api.v2.models import rsvps_models, meetup_models
from app.utilities.validator_file import (
    check_for_empty_string, check_number_format)

meetup_views = meetup_models.MeetupsModel()
repv_views = rsvps_models.RsvpsModel()


class RspvsResources(Resource):
    """Rspvs class view"""
    parser = reqparse.RequestParser()
    parser.add_argument('response', required=True,
                        help='Response cannot be blank', type=str)
    parser.add_argument('createdBy', required=True,
                        help='created by cannot be blank', type=int)
    parser.add_argument('meetupId', required=True,
                        help='Meetup Id cannot be blank', type=int)

    @jwt_required
    def post(self, meetup_id):
        """Method to create an RSPV"""
        try:
            meetup_id = int(meetup_id)
        except Exception:
            return {
                "status": 404,
                "error": "Resource Identifier need an integer"
            }, 404

        try:
            args = RspvsResources.parser.parse_args()
            response = args.get('response')
            createdBy = args.get('createdBy')
            meetupId = args.get('meetupId')
        except Exception:
            return {
                "status": 400,
                "error":
                "Invalid Key field. Missing or wrongly spelled Keys"
            }, 400

        matchers = ["Yes", "No", "Maybe"]

        matching = [
            value for value in response if any(index in response for index in matchers)]

        if not matching:
            return {
                "status": 400,
                "error": "Status, can only take Yes, No or Maybe"
            }, 400

        # Check meetup
        passed_meetup = meetup_views.get_a_specific_meetup_id(args['meetupId'])
        print("Passed meetup", passed_meetup)
        if not passed_meetup:
            return {
                "status": 404,
                "error": "The meetup you entered is not found. Please pass same meetup on your URL"
            }, 404

        # check if meetup url and passed url are equal
        if args['meetupId'] != meetup_id:
            return {
                "status": 404,
                "error": "Meetup of id do not match"
            }, 404

        if check_for_empty_string(response):
            return {
                "status": 400,
                "error":
                "Please provide a response for the Meetup"
            }, 400

        rspvs = repv_views.create_a_rspvs(
            response=args.get('response'),
            createdBy=args.get('createdBy'),
            meetupId=args.get('meetupId')
        )

        return {
            "status": 201,
            "data": rspvs,
            "Message": "RSPV successfully created"
        }, 201


class GetRspvs(Resource):
    """Class to get all RSPVS"""

    @jwt_required
    def get(self, rspv_id):
        """Method to get all the RSPVS created"""
        try:
            rspv_id = int(rspv_id)
        except Exception:
            return {
                "status": 404,
                "error": "Url need an integer"
            }, 404

        new_rspv = repv_views.get_a_specific_rspvs(id=rspv_id)

        if not new_rspv:
            return {
                "status": 404,
                "error": "RSPV of id {} not found".format(rspv_id)
            }, 404
        return {
            "status": 200,
            "data": new_rspv
        }, 200
