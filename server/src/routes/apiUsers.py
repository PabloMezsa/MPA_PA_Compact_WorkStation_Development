from flask import Blueprint, jsonify, request
from flask_cors import  cross_origin
from ..controller import Usercontroller

api_user_scope = Blueprint("api_user", __name__)

con_user = Usercontroller()

@api_user_scope.route('/consultUsers', methods=['GET'])
@cross_origin()

def consult_users():
   return con_user.c_consult_users()

@api_user_scope.route('/createUser', methods=['POST'])
@cross_origin() 

def create_user():
   return con_user.c_create_user(request.json)

@api_user_scope.route('/consultUserId', methods=['GET','POST'])
@cross_origin() 

def consult_user_id():
   #info = request.json
   return con_user.c_consult_users_id()

@api_user_scope.route('/updateUser', methods=['POST'])
@cross_origin() 

def update_user():
   info = request.json
   return con_user.c_update_user_id()

@api_user_scope.route('/deleteUser', methods=['POST'])
@cross_origin() 

def delete_user():
   #info = request.json
   return con_user.c_delete_user()