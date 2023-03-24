import cv2
from datetime import datetime

camera = cv2.VideoCapture(0)
bg_subtractor = cv2.createBackgroundSubtractorMOG2()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))

min_contour_area = 1000
    

def save_image(image, filename="image.jpg", path="/home/pi/www"):
    timestamp = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    cv2.putText(image, timestamp,(1,20), cv2.FONT_HERSHEY_PLAIN, 1,(0,255,0),1)
    cv2.imwrite(f"{path}/{filename}", image)


def get_frame(width=600, height=400):
    _, image = camera.read()
    resize = cv2.resize(image, (width, height))
    return resize


def detect_cars():
    frame = get_frame()
    fg_mask = bg_subtractor.apply(frame, 0.01)
    fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_OPEN, kernel)
    contours, hierarchy = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    n = 0
    for contour in contours:
        if cv2.contourArea(contour) < min_contour_area:
            continue
        n += 1
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    if n > 0:
        save_image(frame)
