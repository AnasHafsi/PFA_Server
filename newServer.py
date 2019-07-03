import json
import os
import socket
import sys
import threading

import numpy as np
from time import sleep
import AstarAlt as As
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
            sleep(3000)
            print_lock.release()
            break
        lst = ss.split("\n")
        if "sendAutoObject" in lst[0]:
            s=lst[1]
            s = s.replace("\'", "\"")
            obj = json.loads(s)
            dim = (obj["rows"], obj["columns"])
            maze = np.zeros(dim, dtype=int)
            start = (obj["d"]["row"], obj["d"]["col"])
            fin = (obj["f"]["row"], obj["f"]["col"])
            print(len(obj["block"]))
            for i in range(len(obj["block"])):
                maze[obj["block"][i]["row"]][obj["block"][i]["col"]] = 1
            path = As.main(maze,start,fin)
            c.sendall(str(path).encode())
            print(path)
        elif "Manuel" in lst[0]:
            print("ManuelMode")
        #path = As.main(ss)

    
        #c.sendall(str(path).encode('utf-8'))
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
