import RPi.GPIO as GPIO
import time as time

leds = [21, 20, 16, 12, 7, 8, 25, 24]
GPIO.setmode(GPIO.BCM)

GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)

for i in range(24):
    GPIO.output(leds[i%8], 1)
    time.sleep(0.2)
    GPIO.output(leds[i%8], 0)

GPIO.output(leds, 0)
GPIO.cleanup()