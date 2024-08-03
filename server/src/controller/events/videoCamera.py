from flask_socketio import emit

def camera(socketio):
    #print("Camera")
    @socketio.on('video_frame', namespace="/")
    def handle_video_frame(data):
        #print('frame')
        emit('video_frame', data, broadcast=True)