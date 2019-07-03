import socket
import json

ip = ""
port = int(input("Veuillez enter le port : "))
buff = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, port))
s.listen(1)
c, addr = s.accept()
print("Connected from Address : ", addr)
F = open("f","w")
while True:
    #c, addr = s.accept()
    data = c.recv(buff)
    F.write(data.decode())
    if data.decode() != '' : 
        print("Data Received : ", data)
        dtt=data.decode()
    if data.decode() == '': break
c.send('Connection closed'.encode())
lst=dtt.split("\n")
print(lst[1])
print("Goodbye :D")
c.close()
