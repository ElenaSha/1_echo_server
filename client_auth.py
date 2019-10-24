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
			port = 1024
			mark = 1

sock.connect((host, port))
print("Соединение с сервером")

#ввод имени/получение приветствия
while True:
	hi = sock.recv(1024)
	print(hi.decode())

	if hi.decode() == "Мы еще не знакомы. Введите ваше имя":
		name = input()
		sock.send(name.encode())
		a = sock.recv(1024) #приятно познакомиться
		print(a.decode())
		pswd = input()
		sock.send(pswd.encode())
		break
	else:		
		while True:
			pswd = input()
			sock.send(pswd.encode())
			print("ОТПРАВИЛ ПАРОЛЬ СЕРВЕРУ")
			answ = sock.recv(1024).decode()
			print(answ)
			if answ == "Пароль неверный. Попробуйте ещё раз.":
				continue
			else:
				break
	break

sock.close()
