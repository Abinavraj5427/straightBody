import eel
import cv2
import base64
from camera import VideoCamera

# Set web files folder
eel.init('webpage')

def gen(camera):
    while True:
        frame = camera.get_frame()
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

eel.start('index.html', size=(300, 200))  # Start