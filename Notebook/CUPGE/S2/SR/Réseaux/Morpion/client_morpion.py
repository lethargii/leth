import threading
import socket

BALISE_NEW_PLAYER = "__player__:"
BALISE_COUP = "__coup__:"
BALISE_QUIT = "__quit__"

clientsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

clientsocket.sendto(f"{BALISE_NEW_PLAYER}{input('Enter your name :')}".encode("utf-8"),('localhost', 8080))


def send():
    while True:
        message = input()
        clientsocket.sendto(message.encode("utf-8"),('localhost', 8080))

def receive():
    while True:
        message = clientsocket.recvfrom(65565)[0].decode("utf-8")
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
