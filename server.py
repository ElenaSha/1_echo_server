import socket

sock = socket.socket()
sock.bind(('', 9090))
print("Запуск сервера")
sock.listen(1)
print("Начало прослушивания порта")
conn, addr = sock.accept()
print("iii")
print(addr)

msg = ''

while True:
	data = conn.recv(1024)
	print("iv")
	if not data:
		break
	msg += data.decode()
	conn.send(data)
	print("v")

print(msg)

conn.close()
print("vi")

print("vii")
sock.close()