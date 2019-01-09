"""Initialize app."""
import os
from flask import Flask
from app.auth.v1 import version_1auth
from app.api.v1 import version_1

from config import app_config


def create_app(config_name):
    """Create the app with the desired environment."""
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(app_config[config_name])
    app.config['BUNDLE_ERRORS'] = True

    app.register_blueprint(version_1auth)
    app.register_blueprint(version_1)

    return app
