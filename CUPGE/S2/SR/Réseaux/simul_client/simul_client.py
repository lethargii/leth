import socket

IP = '133.45.78.9'
PORT = 80
MESSAGE = "GET /index.html HTTP/1.0\r\n\r\n".encode()



s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)



s.connect((IP,PORT))
s.send(MESSAGE)

data = s.recv(1024)
s.close()

print(data)
