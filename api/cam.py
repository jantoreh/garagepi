import io
from PIL import Image
import numpy as np
import cv2

cam = cv2.VideoCapture(0)


def get_single_image():
    _, img = cam.read()
    return img


def convert_numpy_image_to_bytes(array: np.ndarray):
    image = Image.fromarray(array)
    byte_io = io.BytesIO()
    image.save(byte_io, "png")
    byte_io.seek(0)
    return byte_io
