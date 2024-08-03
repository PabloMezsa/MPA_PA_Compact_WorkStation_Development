from flask import Blueprint, render_template, request, jsonify, session
from flask_cors import  cross_origin
from ..controller import Login_controller

home_scope = Blueprint("Home",__name__ )

con_login = Login_controller()

@home_scope.route('/')
@cross_origin()

def home(title='WebSocket Example U'):
   
    return render_template('index.html', title=title)


@home_scope.route('/measuringAndControl')
@cross_origin()

def measuring_and_control():

    return render_template('index_2.html')

@home_scope.route('/closedLoopControl')
@cross_origin()

def closed_loop_control():

    pass

@home_scope.route('/setUp')
@cross_origin()

def set_up():

    return "hello world"

@home_scope.route('/language')
@cross_origin()

def lenguage():

    pass

@home_scope.route('/information')
@cross_origin()

def information():

    pass

@home_scope.route('/login', methods=['POST'])
@cross_origin()

def login():

    return con_login.con_authenticate_user(request.json)

@home_scope.route('/logout', methods=['GET'])
@cross_origin()

def logout():

    user = session['userName']
    session.pop('rolSA', None)
    session.pop('userName', None)

    print(f"Message User {user} get off session")

    return jsonify({"Message":f"User {user} get off session"})