from flask_socketio import emit

def digital_actuators(socketio):

    @socketio.on('rotary_valve', namespace="/")
    def handle_toggle_device(data):

        state = data['state']

        if state == 'on':
            print("Dispositivo encendido")
            response = {'status': True}
        elif state == 'off':
            print("Dispositivo apagado")
            response = {'status': False}
            
        emit('toggle_device', response, broadcast=True)
        emit('device_status', response, broadcast=True)

    @socketio.on('thermal_resistance', namespace="/")
    def handle_toggle_device(data):

        state = data['state']

        if state == 'on':
            print("Dispositivo encendido")
            response = {'status': True}
        elif state == 'off':
            print("Dispositivo apagado")
            response = {'status': False}
            
        emit('toggle_device_2', response, broadcast=True)
        emit('device_status', response, broadcast=True)
    
    @socketio.on('constant_K1', namespace="/")
    def handle_toggle_device(data):

        state = data['state']

        if state == 'on':
            print("Dispositivo encendido")
            response = {'status': True}
        elif state == 'off':
            print("Dispositivo apagado")
            response = {'status': False}
            
        emit('toggle_device_3', response, broadcast=True)
        emit('device_status', response, broadcast=True)
    
    @socketio.on('pump', namespace="/")
    def handle_toggle_device(data):

        state = data['state']

        if state == 'on':
            print("Dispositivo encendido")
            response = {'status': True}
        elif state == 'off':
            print("Dispositivo apagado")
            response = {'status': False}
            
        emit('toggle_device_4', response, broadcast=True)
        emit('device_status', response, broadcast=True)

    @socketio.on('proportional_valve', namespace="/")
    def handle_toggle_device(data):

        state = data['state']

        if state == 'on':
            print("Dispositivo encendido")
            response = {'status': True}
        elif state == 'off':
            print("Dispositivo apagado")
            response = {'status': False}
            
        emit('toggle_device_5', response, broadcast=True)
        emit('device_status', response, broadcast=True)

    @socketio.on('cooler', namespace="/")
    def handle_toggle_device(data):

        state = data['state']

        if state == 'on':
            print("Dispositivo encendido")
            response = {'status': True}
        elif state == 'off':
            print("Dispositivo apagado")
            response = {'status': False}
            
        emit('toggle_device_7', response, broadcast=True)
        emit('device_status', response, broadcast=True)