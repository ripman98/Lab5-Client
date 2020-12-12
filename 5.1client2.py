import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

port = 8888
s.connect(('192.168.114.6',port))

data = s.recv(1024)

s.send(b'Hello, saya client!');

print(data)

s.close()
