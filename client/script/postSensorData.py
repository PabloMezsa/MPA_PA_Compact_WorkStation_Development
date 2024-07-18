from serverStatus import sio

def post_analog_data(level, flow, pressure, temperature):

    if level is None or flow is None or pressure is None or temperature is None:
        pass
    else:
        sensor_variables={'level':level, 'flow':flow, 'pressure':pressure, 'temperature':temperature}
        sio.emit('message_from_client_labview', sensor_variables)