import socket

sock = socket.socket()
print("Запуск сервера")

code = ""


sock.bind(('', 13245))
print("Начало прослушивания порта")
sock.listen(1)

while True:
	conn, addr = sock.accept()
	print("iii")
	print(addr)

	msg = ''

	while True:
		data = conn.recv(1024)
		print("Приём данных от клиента")
		if not data:
			break
		elif data.decode() == "stop":
			break
		else:
			msg += data.decode()
			conn.send(data)
			print("Отправка данных клиенту")

	conn.close()
	print("Отключение клиента")

print("Остановка сервера")
sock.close()