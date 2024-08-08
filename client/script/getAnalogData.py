from serverStatus import sio

analog_data = {'pump': 0, 'valve': 0}

def analog_controller():

    @sio.on('analog_data')
    def message_from_server_to_client_labview(data):
        global analog_data
        analog_data['pump']=data['sp']
        analog_data['valve']=data['p']
        print('pid_data', analog_data)

def buttons_analog():
    global analog_data
    return [analog_data['pump'],analog_data['valve']]