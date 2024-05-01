# Importer les modules threading et socket
import threading
import socket

# Définir les variables des balises utilisées
BALISE_NEW_PLAYER = "__player__:"
BALISE_QUIT = "__quit__"
# Définir le socket du client
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Se connecter au jeu
clientsocket.sendto(f"{BALISE_NEW_PLAYER}{input('Entrez votre nom : ')}".encode("utf-8"),('localhost', 8080))


def send():
    """
    Fonction attendant que l'utilisateur rentre une chaine de caractères au clavier et l'envoie au serveur.
    """
    # Demander continuellement à l'utilisateur d'écrire un message
    while True:
        # Demander un input à l'utilisateur
        message = input()
        # Envoyer le message
        clientsocket.sendto(message.encode("utf-8"), ('localhost', 8080))


def receive():
    """
    Fonction qui attend de recevoir des données et qui les affiche.
    """
    # Recevoir continuellement les messages
    while True:
        # Recevoir un message
        message = clientsocket.recvfrom(65565)[0].decode("utf-8")
        # Si le message reçu est égal à BALISE_QUIT sortir de la boucle
        if message == BALISE_QUIT:
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
