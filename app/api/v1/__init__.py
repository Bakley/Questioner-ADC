from flask import Blueprint
from flask_restful import Api
from app.api.v1.views.meetups_views import AllMeetupResource, MeetupResource
from app.api.v1.views.questions_views import QuestionResource


version_1 = Blueprint('version1', __name__, url_prefix='/api/v1')

api = Api(version_1)


api.add_resource(MeetupResource, '/meetups', '/meetups/<int:meetup_id>')
api.add_resource(AllMeetupResource, '/meetups/upcoming')
api.add_resource(QuestionResource, '/questions')
