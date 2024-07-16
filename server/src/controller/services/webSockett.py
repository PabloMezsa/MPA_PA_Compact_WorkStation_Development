from flask_socketio import SocketIO, emit
from ...utils import SENSOR_VARIABLES

socketio = SocketIO()

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    

@socketio.on('message_from_client_labview')
def handle_message(message):
    print(SENSOR_VARIABLES.format(message[0],message[1], message[2], message[3]))

@socketio.on('message_from_client_web_site')
def handle_message(message):
    print('Received message from client', message)
    response = {'status': True}
    emit('message_from_server_to_client_labview', response, broadcast=True)

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')