import socket

BALISE_NEW_NAME = "__new_name__:"
BALISE_MESSAGE = "__message__:"
BALISE_QUIT = "__quit__"

adresses = {}

def send_entrance_notification(addr, name):
    global adresses
    if addr not in adresses:
        adresses[addr]=name
        for adresse in adresses:
            serveursocket.sendto(f"\n***{name}*** vient de rentrer sur le chat !\n".encode('utf-8'),adresse)

def send_message(addr, message):
    global adresses
    for adresse in adresses:
        if adresse!=addr:
            serveursocket.sendto(f"{adresses[addr]} : {message}".encode('utf-8'),adresse)

def send_quit_notification(addr):
    global adresses
    for adresse in adresses:
        if adresse!=addr:
            serveursocket.sendto(f"***{adresses[addr]}*** a quitté le chat.".encode('utf-8'),adresse)
    serveursocket.sendto("__quit__".encode('utf-8'),addr)
    del adresses[addr]

def traite_data(addr, data):
    if data==BALISE_QUIT:
        send_quit_notification(addr)
    elif data[0:len(BALISE_MESSAGE)]==BALISE_MESSAGE:
        send_message(addr, data[len(BALISE_MESSAGE):])
    elif data[0:len(BALISE_NEW_NAME)]==BALISE_NEW_NAME:
        send_entrance_notification(addr,data[len(BALISE_NEW_NAME):])

serveursocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serveursocket.bind(('localhost',8080))
while True:
    data,addr = serveursocket.recvfrom(1024)
    print(f"recv_data : {data}")
    traite_data(addr, data.decode('utf-8'))
