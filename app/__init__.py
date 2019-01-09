"""Initialize app."""
import os
from flask import Flask

from config import app_config


def create_app(config_name):
    """Create the app with the desired environment."""
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(app_config[config_name])

    return app
