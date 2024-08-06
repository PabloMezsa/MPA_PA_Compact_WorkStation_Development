from serverStatus import sio

pid_data = {'sp': 0, 'p': 0, 'i': 0, 'd': 0}

def process_value(set_point, process_value, control_value):

    if set_point is None or process_value is None or control_value is None:
        pass
    else:
        pid_variables={'process_value':process_value, 'control_value':control_value}
        sio.emit('process_data', pid_variables)

def pid_controller():

    @sio.on('pid_data')
    def message_from_server_to_client_labview(data):
        global pid_data
        pid_data['sp']=data['sp']
        pid_data['p']=data['p']
        pid_data['i']=data['i']
        pid_data['d']=data['d']
        print('pid_data', pid_data)

def pid():
    global pid_data
    return [pid_data['sp'],pid_data['p'],pid_data['i'],pid_data['d']]