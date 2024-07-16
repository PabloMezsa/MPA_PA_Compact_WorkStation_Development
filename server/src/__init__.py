from flask import Flask
from .controller import socketio
from .routes import dashBoard_scope, home_scope, error_scope

app = Flask(__name__, template_folder="views/templates", static_folder='views/static')

def init__app(config):

    # blueprint
    app.register_blueprint(dashBoard_scope, url_prefix="/dashBoard")
    app.register_blueprint(home_scope, url_prefix="/")
    app.register_blueprint(error_scope, url_prefix="/errors")

    # configuration
    app.config.from_object(config)

    # flask-socket.IO configuration
    socketio.init_app(app)

    return app