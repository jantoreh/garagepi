from picamera import PiCamera
import numpy as np
import io
from fastapi.responses import StreamingResponse

camera = PiCamera()
camera.resolution = (320, 240)
camera.start_preview()


def capture():
    stream = io.BytesIO()
    for _ in camera.capture_continuous(stream, format="png", use_video_port=True):
        stream.truncate()
        stream.seek(0)
        return stream

async def video()
    stream = io.BytesIO()
    count = 0
    for _ in camera.capture_continuous(stream, format="png", use_video_port=True):
        stream.truncate()
        stream.seek(0)
        yield stream
        count += 1
        if count >= 100:
            break