from flask import Blueprint

dashBoard_scope = Blueprint("dashBoard",__name__)

# dashBoard route

@dashBoard_scope.route('/dashBoard')

def dashBoard():

    return ""