import cv2
import sqlite3
from datetime import datetime

connection = sqlite3.connect("cars.db")

connection.execute('''
CREATE TABLE IF NOT EXISTS cars (
    id INTEGER PRIMARY KEY,
    timestamp TEXT
)''')

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
    frame = frame[190:280, :]
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
        now = datetime.now()
        timestamp_str = now.strftime('%Y-%m-%d %H:%M:%S')
        connection.execute("INSERT INTO cars (timestamp) VALUES (?)", (timestamp_str,))
        connection.commit()
    if n > 0:
        save_image(frame)
        save_count()

def cars_today():
    now = datetime.now()
    day_str = now.strftime('%Y-%m-%d')
    cursor = connection.execute("SELECT COUNT(*) FROM cars WHERE timestamp LIKE ?", (day_str + '%',))
    return cursor.fetchone()[0]

def save_count(filename="count.txt", path="/home/pi/www"):
    count = cars_today()
    with open(f"{path}/{filename}", "w") as fid:
        fid.write(str(count))

