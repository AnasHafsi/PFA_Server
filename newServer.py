import os
import socket
import sys
import threading

from _thread import *


print_lock = threading.Lock()
ss = "IIO"


def cnn(c):
    while True:
        global ss
        data = c.recv(1024)
        ss = data.decode()
        
        if not data:
            print('Bye')
            print_lock.release()
            break
        f = open("out", "w+")
        f.write(ss)
        f.close()
        os.system('cmd /r python Astar.py')
    c.close()




def Main():
    host = ""
    port = 666
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to post", port)
    s.listen(5)
    print("socket is listening")
    while True:
        c, addr = s.accept()
        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])
        start_new_thread(cnn, (c,))
    s.close()


if __name__ == '__main__':
    Main()
