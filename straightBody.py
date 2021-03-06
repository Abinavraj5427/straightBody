import eel
import cv2
import base64
import firebase_setup
import Notif as n
from firebase_admin import credentials
from firebase_admin import firestore


from camera import VideoCamera


# cred = credentials.Certificate('./serviceAccount/straightbody-4dec9-firebase-adminsdk-nawot-ce763cf334.json')
# firebase_admin.initialize_app(cred)

# Set web files folder
eel.init('webpage')

def gen(camera):
    while True:
        frame = camera.get_special_frame()
        yield frame

@eel.expose
def get_video():
    camera = VideoCamera()
    byte_data = gen(camera)
    for each in byte_data:
        # Convert bytes to base64 encoded str, as we can only pass json to frontend
        blob = base64.b64encode(each)
        blob = blob.decode("utf-8")
        eel.updateImageSrc(blob)()
        # time.sleep(0.1)

@eel.expose
def get_screen_time():
    return n.get_screen_time()

@eel.expose
def get_break():
    return n.get_break()

eel.start('index.html', size=(900, 700))  # Start
