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

def adc(comp, dac, value = 128, i = 7):
    signal = num2dac(dac, value)
    time.sleep(0.005)
    compvalue = GPIO.input(comp)
    
    if compvalue == 0:
        i -= 1
        voltage = value / 256 * 3.3
        print("ADC value = {:^3} -> {}, input voltage = {:.2f}".format(value, signal, voltage), i)
        if i == -1:
            return voltage
        adc(comp, dac, value - 2**(i+1) + 2**(i), i)
    else:
        i -= 1
        voltage = value / 256 * 3.3
        print("ADC value = {:^3} -> {}, input voltage = {:.2f}".format(value, signal, voltage), i)
        if i == -1:
            return voltage
        adc(comp, dac, value+(2**i), i)



dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

try:
    while True:
        print(adc(comp, dac))
        print("-")
        time.sleep(12)
finally:
    GPIO.cleanup()