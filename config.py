import os

class Config():
    """
    Base configuration class with minimal settings
    """
    DEBUG = False
    TESTING = False
    JWT_KEY = os.getenv('SECRET_KEY')

class Development(Config):
    """
    Developer class to set variable for debugging
    """
    DEBUG = True
    DATABASE_URI = os.getenv('DEV_DB_URI')

class Testing(Config):
    """
    Set ups conditions for testing
    """
    TESTING = True
    DEBUG = True
    DATABASE_URI = os.getenv('TEST_DB_URI')

class Production(Config):
    """
    Flags development and testing variables to FALSE to run in a production environment
    """
    DEBUG = False
    TESTING = False

app_config = {
    "TestConfig": Testing,
    "DevConfig" : Development,
    "ProdConfig" : Production
}

