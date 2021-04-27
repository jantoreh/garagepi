import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
RIGHT_DOOR_PIN = 18
GPIO.setup(RIGHT_DOOR_PIN, GPIO.OUT)


def trigger_right_garage_door():
    GPIO.output(RIGHT_DOOR_PIN, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(RIGHT_DOOR_PIN, GPIO.LOW)
