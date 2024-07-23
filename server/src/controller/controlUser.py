from flask import jsonify, request
from ..models import Users, User_model

get_users = User_model()

class Usercontroller():
    
    def c_consult_users(self):

        query = get_users.m_consult_users()
        return query

    def c_create_user(self, info):
       
        post_user = Users.build_user_info(info)
        query = post_user.postUser()                             
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