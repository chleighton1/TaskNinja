import os


class Config:
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True


    # SECRET_KEY = '3324aabb83f14c3cf5450caef74e8770'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    # MAIL_USERNAME = 'taskninja11@gmail.com'
    # MAIL_PASSWORD = 'msgpgorygwthudlz'