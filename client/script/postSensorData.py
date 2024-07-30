from serverStatus import sio

def post_analog_data(level, flow, pressure, temperature, time):

    if level is None or flow is None or pressure is None or temperature is None or time is None:
        pass
    else:
        sensor_variables={'level':level, 'flow':flow, 'pressure':pressure, 'temperature':temperature, 'time':time}
        sio.emit('message_from_client_labview', sensor_variables)