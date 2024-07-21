from flask import Flask
from .controller import socketio
from .routes import dashBoard_scope, home_scope, error_scope, api_user_scope
from .database import mysql_connect_db

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

    # mysql-connect configuration and connection
    mysql_connect_db(app)

    return app