import RPi.GPIO as GPIO
import time as time
GPIO.setmode(GPIO.BCM)


def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

NULL = dec2bin(0)

def num2dac(dac, value):
    signal = dec2bin(value)
    GPIO.output(dac, signal)
    return signal

def adc(comp, dac):
    for value in range(256):
        signal = num2dac(dac, value)
        voltage = value
        time.sleep(0.005)
        compvalue = GPIO.input(comp)
        if compvalue == 0:
            return voltage
            break
        


dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
leds = [21, 20, 16, 12, 7, 8, 25, 24]

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(leds, GPIO.OUT)

try:
    while True:
        num2dac(leds, adc(comp, dac))
        print("-")
finally:
    GPIO.cleanup()