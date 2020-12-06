from picamera import PiCamera, PiRGBArray
from PIL import Image
import numpy as np
import io


def capture():
    stream = io.BytesIO()
    camera = PiCamera()
    camera.resolution = (320,240)
    rawCapture = PiRGBArray(camera.size = (320,240))
    for foo in camera.capture_continuous(stream, format='png', use_video_port=True):
        stream.truncate()
        stream.seek(0)
        array = np.asarray(Image.open(stream))
