from flask_socketio import emit

def control_process_data(socketio):

    @socketio.on('process_data', namespace="/")
    def handle_message(message):
        print(message['process_value'], message['control_value'])
    
    
    @socketio.on('pid_values', namespace="/")
    def handle_pid_values(data):
        # set_point: setPoint,
        # proportional: proportional,
        # integral: integral,
        # derivative: derivative
        response = {'sp':int(data['set_point']), 'p':data['proportional'], 'i':data['integral'], 'd':data['derivative']}
        #print(response)
        emit('pid_data', response, broadcast=True)