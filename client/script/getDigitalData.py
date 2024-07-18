from serverStatus import sio

def get_digital_data():

    received_message = False

    @sio.event
    def message_from_server_to_client_labview(data):
        nonlocal received_message
        received_message = data['status']
        print('Message from server:', data)
    
    while not received_message:
        sio.sleep(0.1)
    
    return received_message