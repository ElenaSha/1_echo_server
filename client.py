import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
mark = 0
#проверка айпишника
while mark == 0:
	print("Введите ваш ip")
	host = input()
	if ("." in host) and (len(host.split(".")) == 4):
		ip = host.split(".")
		for i in range(4):
			if int(ip[i])<256 and int(ip[i])>=0:
				mark = 1;
			else:
				print("Ошибка ввода. Значение каждого октета должно принадлежать промежутку [0;255]")
				print("Если вы хотите еще раз ввести ip, введите 1. Если нет - любую другую строку.")
				ind = input()
				if ind != "1":
					host = 'localhost'
					mark = 1
				break;
	else:
		print("Ошибка ввода. ip-адрес должен состоять из 4 октетов, разделенных точками.")

mark = 0
#проверка порта
while mark == 0:
	print("Введите номер порта")
	port = int(input())
	if 1024<=port<=49151:
		mark = 1
		break
	else:
		print("Ошибка ввода. Номер порта должен принадлежать промежутку [1024;49151]")
		print("Если вы хотите еще раз ввести номер порта, введите 1. Если нет - любую другую строку.")
		ind = input()
		if ind != "1":
			port = 1025
			mark = 1

print("ATTENTION!!!!!!")
print(host, " ", port)

sock.connect((host, port))
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


