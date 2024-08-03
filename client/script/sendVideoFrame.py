from serverStatus import sio
import cv2
import base64

def send_frame(image_path):

    frame = cv2.imread(image_path)
    ret, buffer = cv2.imencode('.jpg', frame)
    frame = buffer.tobytes()
    frame_base64 = base64.b64encode(frame).decode('utf-8')
    sio.emit('video_frame', frame_base64)

    return "Camara On"