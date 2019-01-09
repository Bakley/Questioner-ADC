from flask import Blueprint
from flask_restful import Api
from app.auth.views import SignupResource

auth = Blueprint('authV1', __name__, url_prefix='/auth/v1')

api = Api(auth)

api.add_resource(SignupResource, '/register')
