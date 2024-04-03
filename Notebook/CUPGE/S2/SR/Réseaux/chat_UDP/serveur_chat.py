# Importer le module socket
import socket

# Définir les variables des balises utlisées
BALISE_NEW_NAME = "__new_name__:"
BALISE_MESSAGE = "__message__:"
BALISE_QUIT = "__quit__"

# Création du dictionnaire contenant les adresses des clients
adresses = {}

def send_entrance_notification(addr, name):
    """
    """
    # Définir adresses comme une variable globale
    global adresses
    # Si addr n'est pas une adresse enregistrée l'ajouter et annoncer l'arrivée d'un nouveau client sur le chat
    if addr not in adresses:
        # Ajouter la nouvelle adresse
        adresses[addr]=name
        # Annoncer à tous les clients qu'un nouveau client est arrivé sur le chat
        for adresse in adresses:
            serveursocket.sendto(f"\n***{name}*** vient de rentrer sur le chat !\n".encode('utf-8'),adresse)

def send_message(addr, message):
    """
    """
    # Définir adresses comme une variable globale
    global adresses
    # Envoyer le message à tous les clients sauf l'expéditeur
    for adresse in adresses:
        if adresse!=addr:
            serveursocket.sendto(f"{adresses[addr]} : {message}".encode('utf-8'),adresse)

def send_quit_notification(addr):
    """
    """
    # Définir adresses comme une variable globale
    global adresses
    # Annoncer à tous les clients sauf l'expéditeur qu'une personne a quitté le chat
    for adresse in adresses:
        if adresse!=addr:
            serveursocket.sendto(f"***{adresses[addr]}*** a quitté le chat.".encode('utf-8'),adresse)
    # Faire quitter le client
    serveursocket.sendto("__quit__".encode('utf-8'),addr)
    # Supprimer son adresse du dictionnaire
    del adresses[addr]

def traite_data(addr, data):
    """
    """
    # Si les données correspondent à BALISE_QUIT lancer la fonction send_quit_notification()
    if data==BALISE_QUIT:
        send_quit_notification(addr)
    # Si le début des données correspond à BALISE_MESSAGE lancer la fonction send_message()
    elif data[0:len(BALISE_MESSAGE)]==BALISE_MESSAGE:
        send_message(addr, data[len(BALISE_MESSAGE):])
    # Si le début des données correspond à BALISE_NEW_NAME lancer la fonction send_entrance_notification()
    elif data[0:len(BALISE_NEW_NAME)]==BALISE_NEW_NAME:
        send_entrance_notification(addr,data[len(BALISE_NEW_NAME):])

# Créer le socket du serveur et l'associer à l'adresse localhost et au port 8080
serveursocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serveursocket.bind(('localhost',8080))
# Écouter continuellement sur le port 8080 et traiter les données reçues
while True:
    # Recevoir les données et l'adresse du client
    data,addr = serveursocket.recvfrom(1024)
    # Afficher les données reçues
    print(f"recv_data : {data}")
    # Traiter les données
    traite_data(addr, data.decode('utf-8'))
