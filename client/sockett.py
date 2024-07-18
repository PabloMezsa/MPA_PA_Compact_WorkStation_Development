import socketio

sio = socketio.Client()

received_message = False

def instant():
    
    sio.connect('http://localhost:5000')
    return "Establecida"

def main():
  
    @sio.event
    def connect():
         print('connection established')

    return 'connection established'

def main_2():
    
    @sio.event
    def message_from_server_to_client_labview(data):
        nonlocal received_message
        received_message = data['status']
        print('Message from server:', data)
    
    return received_message

# def main_5():
#     return received_message

# def main_6():
#     global received_message
#     received_message = False

def main_3(level, flow, pressure, temperature):

    if level is None or flow is None or pressure is None or temperature is None:
        pass
    else:
        sensor_variables=[level, flow, pressure, temperature]
        sio.emit('message_from_client_labview', sensor_variables)

def main_4():

    sio.disconnect()

    @sio.event
    def disconnect():
        print('Disconnected from server')
    
    return 'Disconnected Client'