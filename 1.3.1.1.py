import RPi.GPIO as GPIO
import time as time

GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.IN)

while True:
    GPIO.output(14, GPIO.input(15))
    print(GPIO.input(15))
    time.sleep(0.5)