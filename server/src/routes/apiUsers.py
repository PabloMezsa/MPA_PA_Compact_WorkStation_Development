from flask import Blueprint, jsonify, request
from flask_cors import  cross_origin
from ..controller import User_controller

api_user_scope = Blueprint("api_user", __name__)

con_user = User_controller()

@api_user_scope.route('/consultUsers', methods=['GET'])
@cross_origin()

def consult_users():
   return con_user.c_consult_users()

@api_user_scope.route('/createUser', methods=['POST'])
@cross_origin() 

def create_user():
   return con_user.c_create_user(request.json)

@api_user_scope.route('/consultUserId/<_id>', methods=['GET'])
@cross_origin() 

def consult_user_id(_id):
   return con_user.c_consult_users_id(_id)

@api_user_scope.route('/updateUser/<_id>', methods=['PUT'])
@cross_origin() 

def update_user(_id):
   return con_user.c_update_user_id(_id, request.json)

@api_user_scope.route('/deleteUser/<_id>', methods=['DELETE'])
@cross_origin() 

def delete_user(_id):
   return con_user.c_delete_user(_id)