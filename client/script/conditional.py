from serverStatus import sio

received_message = "None"
received_message_2 = "Stop"

def condition():

    @sio.on('changes')
    def message_from_server_to_client_labview(data):

        global received_message
        received_message = data['status']
        print('Message from server:', data)

def change():
    global received_message
    return received_message

def condition_2():

    @sio.on('changes_2')
    def message_from_server_to_client_labview(data):

        global received_message_2
        received_message_2 = data['status']
        print('Message from server:', data)

def change_2():
    global received_message_2
    return received_message_2