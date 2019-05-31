import socket

HOST = '127.0.0.1'
port = 666
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, port))
    while True :
        sttr = input("Entrez le message : ")
        if sttr=="fttp" : 
            s.close()
            break
        s.send(sttr.encode('utf-8'))
