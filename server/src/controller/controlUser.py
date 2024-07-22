from flask import jsonify, request
from ..models import Users, User_model

class Usercontroller():
    
    def c_consult_users(self):
        query = "mod_usuario.m_consultar_usuarios()"
        return query

    def c_create_user(self, info):
       
        post = Users(userName=info['userName'],
                         name=info['name'],
                         lastName=info['lastName'],
                         number=info['number'],
                         email=info['email'],
                         identification=info['identification'],
                         profile=info['profileId'],
                         password=info['userPassword'])
        
        query = post.postUser()
                                      
        return query

    def c_consult_users_id(self):
        query = "mod_usuario.m_consultar_usuario_id()"
        return query

    def c_update_user_id(self):
        query = "mod_usuario.m_actualizar_usuario()"
        return query

    def c_delete_user(self):
        query = "mod_usuario.m_bajar_usuario()"
        return query