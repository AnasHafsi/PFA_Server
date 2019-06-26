import numpy
import gpiozero
from gpiozero import LED
from time import sleep

bit0 = LED(17)
bit1 = LED(27)
bit2 = LED(22)


def tle3():
    bit0.on()
    bit1.off()
    bit2.off()


def linmn():
    bit0.on()
    bit1.on()
    bit2.off()


def lisr():
    bit0.off()
    bit1.on()
    bit2.off()


def lor():
    bit0.off()
    bit1.off()
    bit2.on()


def diagP():
    bit0.on()
    bit1.off()
    bit2.on()


def diagM():
    bit0.off()
    bit1.on()
    bit2.on()


def stop():
    bit0.on()
    bit1.on()
    bit2.on()


def main(path):
    #sensor = DistanceSensor(echo=18, trigger=17)
    a = path
    #sensor.distance < 100
    prob = False
    final = []
    esc = (-1, -1)
    k = 0
    for i in range(len(a)-1):
        b = tuple(numpy.subtract(a[i+1], a[i]))
        if(k == 3):
            esc = a[i]
            print("obstacle detected")
            return True, esc, b, final
        k = k+1
        if b == (1, 1):
            print("move diag + +")
        elif b == (-1, -1):
            print("move diag - -")
        elif b == (-1, 1):
            print("move diag - +")
        elif b == (1, -1):
            print("move diag + -")
        elif b == (-1, 0):
            print("move down")
        elif b == (1, 0):
            print("move up")
        elif b == (0, -1):
            print("move left")
        elif b == (0, 1):
            print("move right")
        final.append(a[i])
        sleep(2)

    return prob, esc, b, final
