# Importer les modules threading et socket
import threading
import socket

import sys
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, GObject, Gio


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_default_size(1080, 720)
        self.set_title("MyApp")
        self.box1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.grid1 = Gtk.Grid()
        self.box1.append(self.grid1)
        
        grille = [["O", "X", "O"],["X","O","X"]]
        for ligne in grille:
            for case in ligne:
                self.grid1.gtk_grid_attach(case)

class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()

app = MyApp(application_id="com.example.GtkApplication")
app.run(sys.argv)

# Définir les variables des balises utilisées
BALISE_NEW_PLAYER = "__player__:"
BALISE_QUIT = "__quit__"
# Définir le socket du client
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Se connecter au jeu
def nom():
    clientsocket.sendto(f"{BALISE_NEW_PLAYER}{input('Entrez votre nom : ')}".encode("utf-8"),('localhost', 8080))


def send():
    """
    Fonction attendant que l'utilisateur rentre une chaine de caractères au clavier et l'envoie au serveur.
    """
    # Demander continuellement à l'utilisateur d'écrire un message
    while True:
        # Demander un input à l'utilisateur
        message = input()
        if message == "__quit__":
            break
        # Envoyer le message
        if message != "":
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
#send_thread = threading.Thread(target=send)
#recv_thread = threading.Thread(target=receive)

# Lancement des processus
#send_thread.start()
#recv_thread.start()
