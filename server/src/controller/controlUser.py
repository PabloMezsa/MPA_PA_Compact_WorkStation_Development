from flask import jsonify, request
from ..models import Users, User_model

get_users = User_model()

class User_controller():
    
    def c_consult_users(self):

        query = get_users.m_consult_users()

        if not query:
            return jsonify({'Message':'There is not register'})
        elif isinstance(query,BaseException):
            return jsonify({"information": str(query)}), 500
        else:
            return jsonify({'Users':query}), 201

    def c_create_user(self, info):
       
        post_user = Users.build_user_info(info)
        query = post_user.postUser()                             
        return query

    def c_consult_users_id(self, _id):

        query = get_users.m_consult_user_id(_id)

        if query is None:
            return jsonify({'Message':'There is not register'})
        elif isinstance(query,BaseException):
            return jsonify({"information": str(query)}), 500
        else:
            return jsonify({'User':query}), 201

    def c_update_user_id(self, _id, info):

        verify = get_users.m_consult_user_id(_id)
        
        if verify is not None:
            update_user = Users.build_user_info(info)
            query = update_user.updateUser() 
            return query
        else:
            return jsonify({'Message':'Unregistered user'}), 404

    def c_delete_user(self, _id):

        verify = get_users.m_consult_user_id(_id)
        
        if verify is None:
            return jsonify({'Message':'Unregistered user'}), 404
        else:
            query = get_users.m_delete_user(_id)
            return query     