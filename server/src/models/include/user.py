from werkzeug.security import check_password_hash, generate_password_hash
from .. import User_model

mod_create_user = User_model()

class Users():

    def __init__(self, username, email, profile, password):
        
        self.__username = username
        self.__email = email
        self.__profile = profile
        self.__password = self.__create_password(password)

    def __create_password(self, password):

        return generate_password_hash(password)

    @classmethod
    def  build_user_info(cls, info):
        return cls(
            username=info['username'],
            email=info['email'],
            profile=info['profileId'],
            password=info['password']
        )      

    def postUser(self):
   
        return mod_create_user.m_create_user(self.__username, self.__email, self.__profile, self.__password)  
    
    def updateUser(self):
   
        return mod_create_user.m_uptade_user(self.__username, self.__email, self.__profile, self.__password)
    