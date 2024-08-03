from flask_socketio import emit

def status_change(socketio):

    @socketio.on('closed_loop_control', namespace="/")
    def handle_closed_loop_control(data):

        state = data['state']

        if state == 'clc':
            print("Close_loop_control")
            response = {'status': True}
        elif state == 'olc':
            print("Open_loop_control")
            response = {'status': False}
            
        emit('message_from_server_to_client_labview', response, broadcast=True)
        emit('device_status', response, broadcast=True)