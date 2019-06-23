# Echo client program
import socket
import time

HOST = '127.0.0.1'    # The remote host
PORT = 666              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(input('enter message').encode())
    time.sleep(13)
    data = s.recv(1024)
    if data!="":
        print('Received', repr(data))
