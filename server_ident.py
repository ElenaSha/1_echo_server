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

while True:
	conn, addr = sock.accept()
	print("Подключение клиента")

	#блок с проверкой имен
	ip = addr[0]
	if ip in names.keys():
		st = "Привет, " + names[ip]
		conn.send(st.encode())
	else:
		conn.send("Мы еще не знакомы. Введите ваше имя".encode())
		new_name = conn.recv(1024).decode()
		st = "Приятно познакомиться, " + new_name
		conn.send(st.encode())
		names.update(ip = new_name)
		with open('names.pickle','wb') as file:
			pickle.dump(names,file)
	break



#	msg = ''

#	while True:
#		data = conn.recv(1024)
#		print("Приём данных от клиента")
#		if not data:
#			break
#		elif data.decode() == "stop":
#			break
#		else:
#			msg += data.decode()
#			conn.send(data)
#			print("Отправка данных клиенту")
#
	conn.close()
	print("Отключение клиента")

print("Остановка сервера")

sock.close()