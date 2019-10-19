import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
sock.connect(('localhost', 13245))
print("Соединение с сервером")

msg = input()
sock.send(msg.encode())
print("Отправка данных серверу")
data = sock.recv(1024)
print("Прием данных от сервера")
sock.close()

print(data.decode())
