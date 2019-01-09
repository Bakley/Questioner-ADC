from flask import Blueprint
from flask_restful import Api
from app.api.v1.views.meetups_views import MeetupResource

version_1 = Blueprint('version1', __name__, url_prefix='/api/v1')

api = Api(version_1)


api.add_resource(MeetupResource, '/meetups', '/meetups/<int:meetup_id>')
