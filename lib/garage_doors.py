import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
RIGHT_DOOR_PIN = 18
LEFT_DOOR_PIN = 17
GPIO.setup(RIGHT_DOOR_PIN, GPIO.OUT)
GPIO.output(RIGHT_DOOR_PIN, GPIO.LOW)
GPIO.setup(LEFT_DOOR_PIN, GPIO.OUT)
GPIO.output(LEFT_DOOR_PIN, GPIO.LOW)


def trigger_right_garage_door():
    trigger_pin(RIGHT_DOOR_PIN)

def trigger_left_garage_door():
    trigger_pin(LEFT_DOOR_PIN)

def trigger_pin(pin, sleep=1):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(sleep)
    GPIO.output(pin, GPIO.LOW)
