import socket
import pickle
import os

sock = socket.socket()
port = 1024

while True:
	try:
		sock.bind(('',port))
		break
	except:
			port+=1
print("port", port)

sock.listen(1)

#читаем файла словарь с парами ip - имя
if os.path.getsize('names.pickle') != 0:
	with open('names.pickle','rb') as file:
		names = pickle.load(file)
else:
	names = {}
print(names)

while True:
	conn, addr = sock.accept()
	print("Подключение клиента")

	#блок с проверкой имен
	ip = addr[0]
	print(ip)
	if ip in names.keys():
		st = "Привет, " + names[ip][0] + ". Введите пароль"
		conn.send(st.encode())
		print("ЩА КАК ПОЛУЧУ ПАРОЛЬ")
		psw = conn.recv(1024).decode()
		print("Я ПОЛУЧИЛ ПАРОЛЬ")
		if psw == names[ip][1]:
			conn.send("welcome".encode())
			break
		else:
			conn.send("Пароль неверный. Попробуйте ещё раз.".encode())

	else:
		conn.send("Мы еще не знакомы. Введите ваше имя".encode())
		new_name = conn.recv(1024).decode()
		st = "Приятно познакомиться, " + new_name + ". Придумайте пароль"
		conn.send(st.encode())
		new_pswd = conn.recv(1024).decode()
		itm = [new_name, new_pswd]
		names.update({ip:itm})
		with open('names.pickle','wb') as file:
			pickle.dump(names,file)
		break

conn.close()
print("Отключение клиента")

print("Остановка сервера")

sock.close()