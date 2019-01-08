"""The project configuration files."""
import os


class Config():
    """Parent configuration."""

    DEBUG = False
    TESTING = False
    CSRF_ENABLE = True
    SECRET_KEY = os.getenv('SECRET_KEY')


class Development(Config):
    """Development environment config."""

    DEBUG = True
    TESTING = True


class Production(Config):
    """Production environment config."""

    DEBUG = False
    TESTING = False


class Testing(Config):
    """Testing environment config."""

    DEBUG = True
    TESTING = True


app_config = {
    'development': Development,
    'testing': Testing,
    'production"': Production
}
