from flask import Blueprint
from flask_restful import Api
from app.api.v1.views.meetups_views import AllMeetupResource, MeetupResource
from app.api.v1.views.questions_views import (QuestionResource,
                                              UpvoteResource,
                                              DownvoteResource)
from app.api.v1.views.rspvs_views import RspvsResource, GetRspvs


version_1 = Blueprint('version1', __name__, url_prefix='/api/v1')

api = Api(version_1, catch_all_404s=True)


api.add_resource(MeetupResource, '/meetups', '/meetups/upcoming')
api.add_resource(AllMeetupResource, '/meetups/<meetup_id>')
api.add_resource(QuestionResource, '/meetups/<meetup_id>/questions')
api.add_resource(UpvoteResource, '/questions/<questions_id>/upvote')
api.add_resource(DownvoteResource, '/questions/<questions_id>/downvote')
api.add_resource(RspvsResource, '/meetups/<meetup_id>/rspvs', '/rspvs')
api.add_resource(GetRspvs, '/rspvs')
