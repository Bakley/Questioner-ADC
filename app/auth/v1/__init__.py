from flask import Blueprint
from flask_restful import Api
from app.auth.v1.views import SignupResource

version_1auth = Blueprint('authV1', __name__, url_prefix='/auth/v1')

api = Api(version_1auth)

api.add_resource(SignupResource, '/register')
