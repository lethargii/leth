import socket

IP = '133.45.78.9'
PORT = 80
BUFFER_SIZE = 1024



s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((IP,PORT))
s.listen()

s_conn,addr = s.accept()
data = s_conn.recv(BUFFER_SIZE)
print(data.decode())

s_conn.close()

s.close()
