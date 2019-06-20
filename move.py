import numpy
import gpiozero
from time import sleep

def main(path,k) :
    #sensor = DistanceSensor(echo=18, trigger=17)
    a = path
    #sensor.distance < 100
    esc=(-1,-1)
    prob=False
    for i in range(len(a)-1):
        if(k==0) : 
            esc = a[i]
            print("obstacle detected")
            prob=True
            break
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
    return prob,esc
