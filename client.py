import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
sock.connect(('localhost', 13245))
print("Соединение с сервером")

msg = input()
print("Отправка данных серверу")
sock.send(msg.encode())

print("Прием данных от сервера")
print("Если вы хотите прервать соединение с сервером, введите \"exit\"")
while (input() != "exit"):
	data = sock.recv(1024)
	print(data.decode())
	print("Если вы хотите прервать соединение с сервером, введите \"exit\"")

sock.close()


