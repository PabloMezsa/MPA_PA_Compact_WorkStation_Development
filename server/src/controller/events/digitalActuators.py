from flask_socketio import emit

def digital_actuators(socketio):

    @socketio.on('toggle_device', namespace="/")
    def handle_toggle_device(data):

        state = data['state']

        if state == 'on':
            print("Dispositivo encendido")
            response = {'status': True}
        elif state == 'off':
            print("Dispositivo apagado")
            response = {'status': False}
            
        emit('message_from_server_to_client_labview', response, broadcast=True)
        emit('device_status', response, broadcast=True)