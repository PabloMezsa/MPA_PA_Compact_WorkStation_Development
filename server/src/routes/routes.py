from flask import Blueprint, render_template

home_scope = Blueprint("Home",__name__ )

@home_scope.route('/')

def home(title='WebSocket Example U'):

    
    return render_template('index.html', title=title)


@home_scope.route('/measuringAndControl')

def measuring_and_control():

    pass

@home_scope.route('/closedLoopControl')

def closed_loop_control():

    pass

@home_scope.route('/setUp')

def set_up():

    return "hello world"

@home_scope.route('/language')

def lenguage():

    pass

@home_scope.route('/information')

def information():

    pass

@home_scope.route('/login')

def login():

    pass