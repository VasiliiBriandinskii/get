import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
p = GPIO.PWM(21, 50)
p.start(10)
try:
   while True:
        inp = input()
        if inp == "stop" or inp == "out" or inp == "break" or inp == "end" or inp == "q":
           break
        inp = int(inp)
        p.start(inp)
        print(3.3/100*int(inp))
except TypeError:
    print("По-арабски пишите")
except ValueError:
    try:
        float(inp)
    except ValueError:
        print("запятую спрчьте")
    else:
        if (float(inp) < 0) and (type(inp) != int):
            print("у вас координатная ось это отрезок от 0 до 100 вы куда со своими нецельными минусами, грнажданин?")
        if type(inp) != int:
            print("у вас координатная ось это отрезок от 0 до 100 вы куда со своими нецельными, грнажданин?")
        elif inp < 0:
            print("у вас координатная ось это отрезок от 0 до 100 вы куда со своими минусами, грнажданин?")
except RuntimeError:
    print("неправильно ты, дядя Федор числа вводишь, надо от 0 до 100!")
else:
    print("если любишь, занули!")
finally:
    p.stop()
    GPIO.cleanup()