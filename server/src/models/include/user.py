from werkzeug.security import check_password_hash, generate_password_hash
from ..user_model import User_model

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

    def postUser(self):
   
        return mod_create_user.m_create_user(self.__userName, self.__name, self.__lastName, self.__number, self.__email, self.__identification, self.__profile, self.__password)  
    
    # def verify_password(self, password):

    #     return check_password_hash(self.password, password)

    # def get_user_data(self):
    #     return {
    #         'id': self.id,
    #         'usuario': self.usuario,
    #         'contrasena': self.contrasena,
    #         'nombre': self.nombre,
    #         'apellido': self.apellido,
    #         'identificacion': self.identificacion,
    #         'correo': self.correo,
    #         'telefono': self.telefono,
    #         'perfil': self.perfil
    #     }