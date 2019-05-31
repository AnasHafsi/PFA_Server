import socket

ip = '127.0.0.1'
port = int(input("Veuillez enter le port : "))
buff = 255
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, port))
s.listen(1)
c, addr = s.accept()
print("Connected from Address : ", addr)
while True:
    #c, addr = s.accept()
    data = c.recv(buff)
    if data != '' : print("Data Received : ", data)
    if data == 'exit': break
c.send('Connection closed'.encode())
print("Goodbye :D")
c.close()
