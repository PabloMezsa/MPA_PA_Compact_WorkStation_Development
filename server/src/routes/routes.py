from flask import Blueprint, render_template

home_scope = Blueprint("Home",__name__ )

@home_scope.route('/')

def home():

    
    return render_template('index.html')