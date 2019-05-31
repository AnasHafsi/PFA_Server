# import socket programming library
import socket
import sys
import threading

from _thread import *

print_lock = threading.Lock()
ss = "IIO"


def threaded(c):
    while True:
        global ss
        data = c.recv(1024)
        ss=data.decode
        if not data:
            print('Bye')

            # lock released on exit
            print_lock.release()
            break

        print(data.decode())
        ss = data.decode()

    # connection closed
    c.close()


def Main():
    host = ""

    # reverse a port on your computer
    # in our case it is 12345 but it
    # can be anything
    port = 666
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to post", port)

    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")

    # a forever loop until client wants to exit
    while True:

        # establish connection with client
        c, addr = s.accept()

        # lock acquired by client
        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])

        # Start a new thread and return its identifier
        start_new_thread(threaded, (c,))
        print("Sa7bi hak hada : {}".format(ss))
    s.close()

if __name__ == '__main__':
    Main()
    
