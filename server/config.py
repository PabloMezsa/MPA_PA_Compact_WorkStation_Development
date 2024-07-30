from decouple import config

class Config:

    SECRET_KEY = config('MY_SECRECT_KEY')
class DevelopmentConfig(Config):

    DEBUG = True
    SERVER_NAME = 'localhost:5000'
    # HOST = '0.0.0.0'
    # PORT = 5000

config = {

    'development':DevelopmentConfig

}