import os

basedir = os.path.abspath(os.path.abspath(__file__))


class Config:
    DEBUG = True
    TESTING = True
    CSRF_ENABLED = True
    SECRET_KEY = True
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class ProductionConfig(Config):
    DEBUG = True


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
