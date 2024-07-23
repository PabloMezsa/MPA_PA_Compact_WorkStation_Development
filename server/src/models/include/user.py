from werkzeug.security import check_password_hash, generate_password_hash
from .. import User_model

mod_create_user = User_model()

class Users():

    def __init__(self, userName, name, lastName, number, email, identification, profile, password):
        
        self.__userName = userName
        self.__name = name
        self.__lastName = lastName
        self.__number = number
        self.__email = email
        self.__identification = identification
        self.__profile = profile
        self.__password = self.__create_password(password)

    def __create_password(self, password):

        return generate_password_hash(password)

    @classmethod
    def  build_user_info(cls, info):
        return cls(
            userName=info['userName'],
            name=info['name'],
            lastName=info['lastName'],
            number=info['number'],
            email=info['email'],
            identification=info['identification'],
            profile=info['profileId'],
            password=info['userPassword']
        )      

    def postUser(self):
   
        return mod_create_user.m_create_user(self.__userName, self.__name, self.__lastName, self.__number, self.__email, self.__identification, self.__profile, self.__password)  
    