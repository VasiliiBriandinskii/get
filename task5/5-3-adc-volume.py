import RPi.GPIO as GPIO
import time as time
GPIO.setmode(GPIO.BCM)


def ledout(value):
    value = value/3.3
    if value < 1/32:
        return [0, 0, 0, 0, 0, 0, 0, 0]
    elif value < 1/8:
        return [0, 0, 0, 0, 0, 0, 0, 1]
    elif value < 2/8:
        return [0, 0, 0, 0, 0, 0, 1, 1]
    elif value < 3/8:
        return [0, 0, 0, 0, 0, 1, 1, 1]
    elif value < 4/8:
        return [0, 0, 0, 0, 1, 1, 1, 1]
    elif value < 5/8:
        return [0, 0, 0, 1, 1, 1, 1, 1]
    elif value < 6/8:
        return [0, 0, 1, 1, 1, 1, 1, 1]
    elif value < 7/8:
        return [0, 1, 1, 1, 1, 1, 1, 1]
    elif value <= 1:
        return [1, 1, 1, 1, 1, 1, 1, 1]

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

NULL = dec2bin(0)

def num2dac(dac, value):
    signal = dec2bin(value)
    GPIO.output(dac, signal)
    return signal

def adc(comp, dac, leds, value = 128, i = 7):
    signal = num2dac(dac, value)
    time.sleep(0.01)
    compvalue = GPIO.input(comp)
    
    if compvalue == 0:
        i -= 1
        voltage = value / 256 * 3.3
        print("ADC value = {:^3} -> {}, input voltage = {:.2f}".format(value, signal, voltage), i)
        GPIO.output(leds, ledout(voltage))
        if i == -1:
            return voltage
            GPIO.output(leds, ledout(voltage))
        adc(comp, dac, leds, value - 2**(i+1) + 2**(i), i)
    else:
        i -= 1
        voltage = value / 256 * 3.3
        print("ADC value = {:^3} -> {}, input voltage = {:.2f}".format(value, signal, voltage), i)
        GPIO.output(leds, ledout(voltage))
        if i == -1:
            return voltage
            GPIO.output(leds, ledout(voltage))
        adc(comp, dac, leds, value+(2**i), i)


dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(leds, GPIO.OUT)

try:
    while True:
        print(adc(comp, dac, leds))
        print("-")
        time.sleep(0.1)
finally:
    GPIO.cleanup()