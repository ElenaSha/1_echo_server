import socket

f = open('server.log','a') 

sock = socket.socket()
f.write("Запуск сервера\n")

port = 1024

while True:
	try:
		sock.bind(('',port))
		break
	except:
			port+=1

print("Порт №", port)


f.write("Начало прослушивания порта\n")
sock.listen(1)

while True:
	conn, addr = sock.accept()
	f.write("Подключение клиента")
	print(addr)

	msg = ''

	while True:
		data = conn.recv(1024)
		f.write("Приём данных от клиента\n")
		if not data:
			break
		elif data.decode() == "stop":
			break
		else:
			msg += data.decode()
			conn.send(data)
			f.write("Отправка данных клиенту\n")

	conn.close()
	f.write("Отключение клиента\n")

f.write("Остановка сервера\n")
f.close()
sock.close()