import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STATIC_FOLDER = f"{os.getenv('APP_FOLDER')}/app/static"
    MEDIA_FOLDER = f"{os.getenv('APP_FOLDER')}/app/media"
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
