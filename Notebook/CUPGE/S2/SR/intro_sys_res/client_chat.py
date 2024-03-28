clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8080))
clientsocket.send("GET /pages/index.html HTTP/1.1\r\nHost: localhost\r\n\r\n".encode("utf-8"))
print(clientsocket.recv(65565).decode("utf-8"))
