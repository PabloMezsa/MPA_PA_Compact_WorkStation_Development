from flask import Blueprint, jsonify
from flask_cors import  cross_origin

api_user_scope = Blueprint("api_user", __name__)

@api_user_scope.route('/listausuarios', methods=['GET'])
@cross_origin()  
def listausuarios():
   return "hello"