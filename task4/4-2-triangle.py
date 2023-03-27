import RPi.GPIO as GPIO
import time as time

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]


GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)

try:
    i = 0
    per = input()
    while True:
        per = float(per)
        out = dec2bin(int(i%256))
        GPIO.output(dac, out)
        time.sleep(per/256)
        i += 1
except TypeError:
    print("По-арабски пишите")
except ValueError:
    try:
        float(per)
    except ValueError:
        print("запятую спрчьте")
        if per < 0:
            print("у вас координатная ось это отрезок от 0 до 255 вы куда со своими минусами, грнажданин?")
#  except RuntimeError:
#      print("неправильно ты, дядя Федор числа вводишь, надо от 0 до 255!")
else:
    print("если любишь, занули!")
finally:
    GPIO.output(dac, [0,0,0,0,0,0,0,0])
