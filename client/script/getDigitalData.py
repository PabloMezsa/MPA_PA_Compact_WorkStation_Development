from serverStatus import sio

received_message = False
received_message_2 = False
received_message_3 = False
received_message_4 = False
received_message_5 = False
received_message_7 = False

def get_digital_data():

    @sio.on('toggle_device')
    def message_from_server_to_client_labview(data):
        global received_message
        received_message = data['status']
        print('Message from server:', data)

def get_digital_data_2():

    @sio.on('toggle_device_2')
    def message_from_server_to_client_labview(data):
        global received_message_2
        received_message_2 = data['status']
        print('Message from server:', data)

def get_digital_data_3():

    @sio.on('toggle_device_3')
    def message_from_server_to_client_labview(data):
        global received_message_3
        received_message_3 = data['status']
        print('Message from server:', data)

def get_digital_data_4():

    @sio.on('toggle_device_4')
    def message_from_server_to_client_labview(data):
        global received_message_4
        received_message_4 = data['status']
        print('Message from server:', data)

def get_digital_data_5():

    @sio.on('toggle_devic_5')
    def message_from_server_to_client_labview(data):
        global received_message_5
        received_message_5 = data['status']
        print('Message from server:', data)

def get_digital_data_7():

    @sio.on('toggle_device_7')
    def message_from_server_to_client_labview(data):
        global received_message_7
        received_message_7 = data['status']
        print('Message from server:', data)


def rotary_valve():
    global received_message
    return received_message

def thermal_resistance():
    global received_message_2
    return received_message_2

def constant_K1():
    global received_message_3
    return received_message_3

def pump():
    global received_message_4
    return received_message_4

def proportional_valve():
    global received_message_5
    return received_message_5

def cooler():
    global received_message_7
    return received_message_7