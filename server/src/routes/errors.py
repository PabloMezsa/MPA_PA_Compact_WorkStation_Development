from flask import Blueprint, jsonify

error_scope = Blueprint("Page_Not_Found",__name__)

# Error 404

@error_scope.app_errorhandler(404)

def Page_Not_Found(e):

    #error = {"mesage":"error"}
    return jsonify(error=str(e)), 404

# Error 405

@error_scope.app_errorhandler(405)

def Method_Not_Allowed(e):

    #error = {"mesage":"error"}
    return jsonify(error=str(e)), 405

# Error 500

@error_scope.app_errorhandler(500)

def Internal_Server_PError(e):

    #error = {"mesage":"error"}
    return jsonify(error=str(e)), 500