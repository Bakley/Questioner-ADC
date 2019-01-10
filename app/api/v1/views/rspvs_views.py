from flask_restful import Resource, reqparse
from app.api.v1.models import rspvs

rspv_view = rspvs.RspvsModel()


class RspvsResource(Resource):
    """Rspvs class"""
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
        args = RspvsResource.parser.parse_args()

        rspv = rspv_view.create_question(status=args.get('status'),
                                         topic=args.get('topic'),
                                         meetup=args.get('meetup'),
                                         createdBy=args.get(
            'createdBy')
        )

        return {
            "status": 201,
            "data": rspv,
            "Message": "rspv successfully created"
        }
