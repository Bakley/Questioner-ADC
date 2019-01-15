"""Initialize app."""
import os
from flask import Flask
from app.auth.v1 import version_1auth
from app.api.v1 import version_1

from config import app_config

from flask import jsonify


class ApiError(Exception):
    def __init__(self, message, payload=None, status_code=400):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code
        self.payload = payload or ()

    def get_response(self):
        ret = dict(self.payload)
        ret['message'] = self.message
        return jsonify(ret), self.status_code


def create_app(config_name):
    """Create the app with the desired environment."""
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(app_config[config_name])
    app.config['BUNDLE_ERRORS'] = True

    app.register_blueprint(version_1auth)
    app.register_blueprint(version_1)

    @app.errorhandler(ApiError)
    def handle_api_error(error):
        return error.get_response()

    return app
