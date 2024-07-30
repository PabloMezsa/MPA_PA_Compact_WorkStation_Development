from werkzeug.security import check_password_hash
from ..login_model import Login_model

mod_login_user = Login_model()

class User_login():


    def __init__(self, userName, email, password):

        self.__userName = userName 
        self.__email = email
        self.__password = password

    @classmethod
    def  build_user_info(cls, info):
        return cls(
            userName=info['userName'],
            email=info['email'],
            password=info['userPassword']
        )   

    def authenticate(self):

        verify = mod_login_user.m_check_user_authentication(self.__userName, self.__email)

        return verify

    def verify_password(self, check):

        return check_password_hash(check[8], self.__password)


