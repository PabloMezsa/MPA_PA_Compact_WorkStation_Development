from decouple import config

class Config:

    SECRET_KEY = config('MY_SECRECT_KEY')
    # MYSQL_USER = config('MYSQL_USER')
    # MYSQL_HOST = config('MYSQL_HOST')
    # MYSQL_PASSWORD = config('MYSQL_PASSWORD')
    # MYSQL_DB = config('MYSQL_DB')
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:{}@localhost/{}'.format(MYSQL_PASSWORD, MYSQL_DB)
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):

    DEBUG = True
    SERVER_NAME = 'localhost:5000'

config = {

    'development':DevelopmentConfig

}