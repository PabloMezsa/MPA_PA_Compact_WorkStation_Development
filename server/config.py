from decouple import config

class Config:

    SECRET_KEY = config('MY_SECRECT_KEY')
    MYSQL_USER = config('MYSQL_USER')
    MYSQL_HOST = config('MYSQL_HOST')
    MYSQL_PASSWORD = config('MYSQL_PASSWORD')
    MYSQL_DB = config('MYSQL_DB')
class DevelopmentConfig(Config):

    DEBUG = True
    SERVER_NAME = 'localhost:5000'

config = {

    'development':DevelopmentConfig

}