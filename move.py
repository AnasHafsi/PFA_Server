import numpy
import gpiozero
from time import sleep

def main(path) :
    a = path
    for i in range(len(a)-1):
        b = tuple(numpy.subtract(a[i], a[i+1]))
        print(b)
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
        elif b == (0,1):
            print("move right")
        sleep(5)
