from flask import Blueprint
from flask_restful import Api

version_2auth = Blueprint('authV2', __name__, url_prefix='/auth/v2')

api = Api(version_2auth)
