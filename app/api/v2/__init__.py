from flask import Blueprint
from flask_restful import Api
from app.api.v2.views.meetups_views import (MeetupViewsResource,
                                            SpecificMeetup,
                                            UpcomingMeetups)

from app.api.v2.views.question_views import (QuestionViewsResource,
                                             UpvoteResource,
                                             DownvoteResource,
                                             SpecificQuestion)

from app.api.v2.views.comment_views import CommentViewsResource
from app.api.v2.views.rsvps_views import RspvsResources, GetRspvs

version_2 = Blueprint('version2', __name__, url_prefix='/api/v2')

api = Api(version_2, catch_all_404s=True)

api.add_resource(MeetupViewsResource, '/meetups')
api.add_resource(SpecificMeetup, '/meetups/<meetup_id>')
api.add_resource(UpcomingMeetups, '/meetups/upcoming')
api.add_resource(QuestionViewsResource, '/meetups/<meetup_id>/questions')
api.add_resource(UpvoteResource, '/questions/<questions_id>/upvote')
api.add_resource(DownvoteResource, '/questions/<questions_id>/downvote')
api.add_resource(SpecificQuestion, '/questions/<questions_id>')
api.add_resource(CommentViewsResource, '/comment')
api.add_resource(RspvsResources, '/meetups/<meetup_id>/rspv')
api.add_resource(GetRspvs, '/rspv/<rspv_id>')
