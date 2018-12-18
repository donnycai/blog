import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp@163.com'
    MAIL_PORT = '25'
    # MAIL_SERVER = '127.0.0.1'
    MAIL_USE_TLS = False
    MAIL_USERNAME = 'donny'
    MAIL_PASSWORD = '1qaz2wsx3edc'
    ADMINS = ['490026468@qq.com']

    POSTS_PER_PAGE = 10
