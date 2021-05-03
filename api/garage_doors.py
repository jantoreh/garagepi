import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
RIGHT_DOOR_PIN = 18
GPIO.setup(RIGHT_DOOR_PIN, GPIO.OUT)
GPIO.output(RIGHT_DOOR_PIN, GPIO.LOW)


def trigger_right_garage_door():
    GPIO.output(RIGHT_DOOR_PIN, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(RIGHT_DOOR_PIN, GPIO.LOW)
