from flask import Flask
from .controller import socketio
from .routes import dashBoard_scope, home_scope, error_scope, api_user_scope
from flask_cors import CORS
#from .database import Connector

app = Flask(__name__, template_folder="views/templates", static_folder='views/static')

def init__app(config):

    # blueprint
    app.register_blueprint(dashBoard_scope, url_prefix="/dashboard")
    app.register_blueprint(home_scope, url_prefix="/")
    app.register_blueprint(error_scope, url_prefix="/errors")
    app.register_blueprint(api_user_scope, url_prefix="/users")

    # configuration
    app.config.from_object(config)

    # flask-socket.IO configuration
    socketio.init_app(app)

    # CORS configuration
    CORS(app, resources={r"/*": {"origins": "*"}})  
    #CORS(app, resources={r"/*": {"origins": "http://172.16.19.114:5173"}})

    return app