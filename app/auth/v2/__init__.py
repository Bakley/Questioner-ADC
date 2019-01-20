from flask import Blueprint
from flask_restful import Api
from app.auth.v2.views import UserRegister

version_2auth = Blueprint('authV2', __name__, url_prefix='/auth/v2')

api = Api(version_2auth)
api.add_resource(UserRegister, '/signup')
