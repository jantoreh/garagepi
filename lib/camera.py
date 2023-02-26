import cv2
from datetime import datetime

camera = cv2.VideoCapture(0)

def capture_image(filename: str, path="/home/pi/www"):
    _, image = camera.read()
    resize = cv2.resize(image, (1080, 720))
    timestamp = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    cv2.putText(resize, timestamp,(1,30), cv2.FONT_HERSHEY_PLAIN, 2,(0,255,0),2)
    cv2.imwrite(f"{path}/{filename}", resize)
