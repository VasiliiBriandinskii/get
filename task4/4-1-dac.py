import RPi.GPIO as GPIO
#  import time as time

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]


GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)
try:
   while True:
       inp = input()
       inp = int(inp)
       if inp == "stop" or inp == "out" or inp == "break" or inp == "end" or inp == "q":
           break
       out = dec2bin(int(inp))
       GPIO.output(dac, out)
       print(3.3/256*int(inp))
except TypeError:
    print("По-арабски пишите")
except ValueError:
    try:
        float(inp)
    except ValueError:
        print("запятую спрчьте")
    else:
        if (float(inp) < 0) and (type(inp) != int):
            print("у вас координатная ось это отрезок от 0 до 255 вы куда со своими нецельными минусами, грнажданин?")
        if type(inp) != int:
            print("у вас координатная ось это отрезок от 0 до 255 вы куда со своими нецельными, грнажданин?")
        elif inp < 0:
            print("у вас координатная ось это отрезок от 0 до 255 вы куда со своими минусами, грнажданин?")
except RuntimeError:
    print("неправильно ты, дядя Федор числа вводишь, надо от 0 до 255!")
else:
    print("если любишь, занули!")
finally:
    GPIO.output(dac, [0,0,0,0,0,0,0,0])
