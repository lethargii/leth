# Importer les modules threading et socket
import threading
import socket

# Définir les variables des balises utilisées
BALISE_NEW_NAME = "__new_name__:"
BALISE_MESSAGE = "__message__:"
BALISE_QUIT = "__quit__"

# Définir le socket du client
clientsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# Se connecter au chat
clientsocket.sendto(f"{BALISE_NEW_NAME}{input('Enter your name : ')}".encode("utf-8"),('localhost', 8080))


def send():
    """
    Fonction attendant que l'utilisateur rentre une chaine de caractères au clavier et l'envoie au serveur.
    """
    # Demander continuellement à l'utilisateur d'écrire un message
    while True:
        # Demander un input à l'utilisateur
        message = input()
        # Si le message reçu est égal à "quit" envoyer comme message BALISE_QUIT au serveur et sortir de la boucle
        if message=="quit":
            clientsocket.sendto(BALISE_QUIT.encode("utf-8"),('localhost', 8080))
            break
        # Sinon envoyer le message avec BALISE_MESSAGE devant
        else:
            clientsocket.sendto(f"{BALISE_MESSAGE}{message}".encode("utf-8"),('localhost', 8080))

def receive():
    """
    Fonction qui attend de recevoir des données et qui les affiche.
    """
    # Recevoir continuellement les messages
    while True:
        # Recevoir un message
        message = clientsocket.recvfrom(1024)[0].decode("utf-8")
        # Si le message reçu est égal à BALISE_QUIT sortir de la boucle
        if message==BALISE_QUIT:
            break
        # Sinon afficher le message
        else:
            print(message)

# Création des processus
send_thread = threading.Thread(target=send)
recv_thread = threading.Thread(target=receive)

# Lancement des processus
send_thread.start()
recv_thread.start()
