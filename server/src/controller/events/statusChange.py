from flask_socketio import emit

def status_change(socketio):

    @socketio.on('Control_loop', namespace="/")
    def handle_control_loop(data):

        state = data['state']

        if state == 'clc':
            print("Close_loop_control")
            response = {'status': 'clc'}
        elif state == 'olc':
            print("Open_loop_control")
            response = {'status': 'olc'}
            
        emit('changes', response, broadcast=True)
        emit('device_status', response, broadcast=True)
    
    @socketio.on('Control_level', namespace="/")
    def handle_control_leveñ(data):

        state = data['state']

        if state == 'Start':
            print("Start_Process")
            response = {'status': 'Start'}
        elif state == 'Stop':
            print("Stop_Process")
            response = {'status': 'Stop'}

        emit('changes_2', response, broadcast=True)
        emit('device_status', response, broadcast=True)