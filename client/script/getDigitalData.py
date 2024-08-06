from serverStatus import sio

received_message = None

def get_digital_data():

    @sio.event
    def message_from_server_to_client_labview(data):
        global received_message
        received_message = data['status']
        print('Message from server:', data)

def pump():
    global received_message
    return received_message