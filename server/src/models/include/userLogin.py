from werkzeug.security import check_password_hash
from ..login_model import Login_model

mod_login_user = Login_model()

class User_login():


    def __init__(self, username, password):

        self.__username = username 
        self.__password = password

    @classmethod
    def  build_user_info(cls, info):
        return cls(
            username=info['username'],
            password=info['password']
        )   

    def authenticate(self):

        verify = mod_login_user.m_check_user_authentication(self.__username)

        return verify

    def verify_password(self, check):

        return check_password_hash(check[4], self.__password)


