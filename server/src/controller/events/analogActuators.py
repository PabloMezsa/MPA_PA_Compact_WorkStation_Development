from flask_socketio import emit

def analog_actuators(socketio):

    @socketio.on('analog_values', namespace="/")
    def handle_pid_values(data):

        response = {'sp':int(data['set_point']), 'p':data['proportional']}
        #print(response)
        emit('analog_data', response, broadcast=True)