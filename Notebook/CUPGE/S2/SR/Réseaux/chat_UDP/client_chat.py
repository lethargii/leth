import threading
import socket

BALISE_NEW_NAME = "__new_name__:"
BALISE_MESSAGE = "__message__:"
BALISE_QUIT = "__quit__"

clientsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

clientsocket.sendto(f"{BALISE_NEW_NAME}{input('Enter your name :')}".encode("utf-8"),('localhost', 8080))


def send():
    while True:
        message = input()
        if message=="quit":
            clientsocket.sendto(BALISE_QUIT.encode("utf-8"),('localhost', 8080))
            break
        else:
            clientsocket.sendto(f"{BALISE_MESSAGE}{message}".encode("utf-8"),('localhost', 8080))

def receive():
    while True:
        message = clientsocket.recvfrom(1024)[0].decode("utf-8")
        if message==BALISE_QUIT:
            break
        else:
            print(message)

# Création des processus
send_thread = threading.Thread(target=send)
recv_thread = threading.Thread(target=receive)

# Lancement des processus
send_thread.start()
recv_thread.start()
