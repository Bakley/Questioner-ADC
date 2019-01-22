from flask import Blueprint
from flask_restful import Api
from app.api.v2.views.meetups_views import MeetupViewsResource, SpecificMeetup

version_2 = Blueprint('version2', __name__, url_prefix='/api/v2')

api = Api(version_2, catch_all_404s=True)
api.add_resource(MeetupViewsResource, '/meetups')
api.add_resource(SpecificMeetup, '/meetups/<meetup_id>')
