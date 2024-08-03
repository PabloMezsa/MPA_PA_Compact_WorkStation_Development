from flask_socketio import emit
from ...utils import SENSOR_VARIABLES

def analog_sensors(socketio):

    @socketio.on('message_from_client_labview', namespace="/")
    def handle_message(message):
        print(SENSOR_VARIABLES.format(message['level'],message['flow'], message['pressure'], message['temperature'], message['time']))