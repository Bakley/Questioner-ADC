"""Initialize app."""
import os
from flask import Flask
from dotenv import load_dotenv
from app.auth.v2 import version_2auth
from app.api.v2 import version_2
from app.api.v2.dbmodel import QuestionerDb
from config import app_config
from flask_jwt_extended import JWTManager
from datetime import timedelta


def create_app(config_name):
    """Create the app with the desired environment."""
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(app_config[config_name])
    app.config['BUNDLE_ERRORS'] = True

    with app.app_context():
        QuestionerDb().init_db(app.config['DATABASE_URI'])
        QuestionerDb().build_all()

    app.register_blueprint(version_2auth)
    app.register_blueprint(version_2)
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=6)
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')

    jwt = JWTManager(app)

    return app


# refers to application_top
APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)
