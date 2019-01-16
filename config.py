import os

basedir = os.path.abspath(os.path.pathdir(__file__))


class Config:
    DEBUG = True
    TESTING = True
    CSRF_ENABLED = True
    SECRET_KEY = True


class ProductionConfig(Config):
    DEBUG = True


class StaggingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
