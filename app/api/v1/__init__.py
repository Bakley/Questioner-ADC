from flask import Blueprint
from flask_restful import Api
from app.api.v1.views.meetups_views import AllMeetupResource, MeetupResource
from app.api.v1.views.questions_views import (QuestionResource,
                                              UpvoteResource,
                                              DownvoteResource)
from app.api.v1.views.rspvs_views import RspvsResource


version_1 = Blueprint('version1', __name__, url_prefix='/api/v1')

api = Api(version_1)


api.add_resource(MeetupResource, '/meetups', '/meetups/upcoming')
api.add_resource(AllMeetupResource, '/meetups/<int:meetup_id>',
                 '/meetups/<int:meetup_id>/rspv')
api.add_resource(QuestionResource, '/questions')
api.add_resource(RspvsResource, '/meetups/<int:meetup_id>/rspvs')
api.add_resource(UpvoteResource, '/questions/<int:questions_id>/upvote')
api.add_resource(DownvoteResource, '/questions/<int:questions_id>/downvote')
