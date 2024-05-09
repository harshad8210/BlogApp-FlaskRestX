import os
from dotenv import load_dotenv, find_dotenv
from datetime import timedelta

load_dotenv(find_dotenv())


class BaseConfig:
    MAIL_USE_TLS = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=5)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(hours=8)


class Config(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = int(os.getenv('MAIL_PORT'))
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')


class Production(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = int(os.getenv('MAIL_PORT'))
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')


app_config = {
    'development': Config,
    'production': Production
}
