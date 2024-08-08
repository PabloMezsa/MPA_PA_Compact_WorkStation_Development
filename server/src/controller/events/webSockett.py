from flask_socketio import SocketIO, emit
from .digitalActuators import digital_actuators
from .videoCamera import camera
from .analogSensors import analog_sensors
from .statusChange import status_change
from .pidData import control_process_data
from .analogActuators import analog_actuators

socketio = SocketIO()

@socketio.on('connect', namespace="/")
def handle_connect():
    print('Client connected')

@socketio.on('disconnect', namespace="/")
def test_disconnect():
    print('Client disconnected')

digital_actuators(socketio)
analog_actuators(socketio)
analog_sensors(socketio)
status_change(socketio)
control_process_data(socketio)
camera(socketio)