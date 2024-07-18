import socketio

sio = socketio.Client()

def server_connect():
    
    sio.connect('http://localhost:5000')

    @sio.event
    def connect():
         print('connection established')

    return "connection established"

def server_disconnect():

    sio.disconnect()

    @sio.event
    def disconnect():
        print('Disconnected from server')

    return "connection finished"