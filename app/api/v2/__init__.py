from flask import Blueprint
from flask_restful import Api
from app.api.v2.views.meetups_views import (MeetupViewsResource,
                                            SpecificMeetup,
                                            UpcomingMeetups)

from app.api.v2.views.question_views import (QuestionViewsResource,
                                             UpvoteResource)

version_2 = Blueprint('version2', __name__, url_prefix='/api/v2')

api = Api(version_2, catch_all_404s=True)

api.add_resource(MeetupViewsResource, '/meetups')
api.add_resource(SpecificMeetup, '/meetups/<meetup_id>')
api.add_resource(UpcomingMeetups, '/meetups/upcoming')
api.add_resource(QuestionViewsResource, '/meetups/<meetup_id>/questions')
api.add_resource(UpvoteResource, '/questions/<questions_id>/upvote')
