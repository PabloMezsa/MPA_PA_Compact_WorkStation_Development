from flask import Blueprint, jsonify

dashBoard_scope = Blueprint("dashboard",__name__)

# dashBoard route

@dashBoard_scope.route('/')

def dashBoard():

    return jsonify({'Message':'Welcome to DashBoard'})