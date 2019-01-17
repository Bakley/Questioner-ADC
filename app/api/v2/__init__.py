from flask import Blueprint
from flask_restful import Api


version_2 = Blueprint('version2', __name__, url_prefix='/api/v2')

api = Api(version_2, catch_all_404s=True)