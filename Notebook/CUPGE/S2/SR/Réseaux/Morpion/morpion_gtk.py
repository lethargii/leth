# Importer le module socket
import socket
import sys
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gdk, GLib


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # paramètres de l'application
        self.set_default_size(1080, 720)
        self.set_title("morpionlan")
        self.BALISE_COUP = "__coup__:"
        self.BALISE_NEW_PLAYER = "__player__:"

        # css
        style = Gtk.CssProvider()
        style.load_from_path('style.css')
        Gtk.StyleContext.add_provider_for_display(
                Gdk.Display.get_default(),
                style,
                Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        # menu principal
        self.main = Gtk.Grid(orientation=Gtk.Orientation.VERTICAL,
                             halign=Gtk.Align.CENTER,
                             valign=Gtk.Align.CENTER,
                             row_spacing=50,
                             column_spacing=30)
        self.main_t = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                              halign=Gtk.Align.CENTER,
                              valign=Gtk.Align.CENTER)
        self.main_bl = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                               halign=Gtk.Align.CENTER,
                               valign=Gtk.Align.CENTER)
        self.main_br = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,
                               halign=Gtk.Align.CENTER,
                               valign=Gtk.Align.CENTER)

        self.serv_b = Gtk.Button(label="Host a game")
        self.serv_b.connect('clicked', self.start_server)
        self.cli_b = Gtk.Button(label="Join a game")
        self.cli_b.connect('clicked', self.start_client)
        self.main_title = Gtk.Label(label="Welcome to MorpionLAN!",
                                    halign=Gtk.Align.CENTER,
                                    valign=Gtk.Align.CENTER)
        self.main_title.set_css_classes(['title'])

        self.main.attach(self.main_t, 0, 0, 2, 1)
        self.main.attach(self.main_bl, 0, 1, 1, 1)
        self.main.attach(self.main_br, 1, 1, 1, 1)
        self.main_t.append(self.main_title)

        self.main_bl.append(self.serv_b)
        self.main_br.append(self.cli_b)

        # prompt name
        self.name = Gtk.Entry(halign=Gtk.Align.CENTER,
                              valign=Gtk.Align.CENTER)
        self.name.set_placeholder_text("Entrez votre pseudo...")
        self.name.connect('activate', self.name_prompted)

        # connection du serveur
        self.serv_connection = Gtk.Label(
                label="Le client doit rentrer cette adresse ip : 127.0.0.1")
        self.cli_connection = Gtk.Entry(halign=Gtk.Align.CENTER,
                                        valign=Gtk.Align.CENTER)
        self.cli_connection.set_placeholder_text(
                "Entrez l'adresse ip du serveur...")

        # start the app
        self.start_main()

    def start_main(self):
        self.set_child(self.main)

    def start_server(self, button):
        self.set_child(self.name)
        self.serv_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.next = self.serv_connection

    def start_client(self, button):
        self.set_child(self.name)
        self.cli_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.next = self.cli_connection

    def name_prompted(self, name):
        self.set_child(self.next)

    def start_game(self, name):
        self.game = Game()

    def connection_joueur(self, serveursocket):
        """
        Fonction attendant de recevoir une demande de connection d'un joueur.
        Arguments :
            - serveursocket : Le socket du serveur
        """
        data, joueur = b'', ('', 0)
        while data.decode('utf-8')[0:len(self.BALISE_NEW_PLAYER)] != self.BALISE_NEW_PLAYER:
            data, joueur = serveursocket.recvfrom(1024)
        serveursocket.sendto(f"Bienvenue {data.decode('utf-8')[len(self.BALISE_NEW_PLAYER):]} !".encode('utf-8'),joueur)
        return data.decode('utf-8')[len(self.BALISE_NEW_PLAYER):], joueur

    def listen_joueur(self):
        while True:
            data = self.serv_socket.recvfrom()
            if data[0:len(self.BALISE_COUP)] == self.BALISE_COUP:
                print("coucou")




class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()


class Game():
    def __init__(self, rows=6, columns=7, k=4, gravity=False):
        self.rows = rows
        self.columns = columns
        self.k = k
        self.gravity = gravity
        self.grid = [[[0] for i in range(columns)] for j in range(rows)]

    def get_grid(self):
        return self.grid

    def set_grid(self, joueur, i, j):
        if self.grid[i][j] == 0:
            self.grid[i][j] = joueur
            return True
        else:
            return False

    def align(self, joueur, x, y, nb):
        pos_x = (self.rows-1)/2
        pos_y = (self.cols-1)/2
        pos_final_x = (self.rows-1)/2
        pos_final_y = (self.cols-1)/2
        pos_x += x*((self.rows-1)/2-min(abs(x), abs(y))*(self.k-1))
        pos_final_y += y*((self.rows-1)/2-min(abs(x), abs(y))*(self.k-1))
        if x*y == 0:
            pos_final_x -= (x + y)*(self.rows-1)/2
            pos_y -= (x + y)*(self.cols-1)/2
            pos_x *= abs(y)
            pos_final_y *= abs(x)
        else:
            pos_final_x -= x*(self.rows-1)/2
            pos_y -= y*(self.cols-1)/2
        while pos_y != pos_final_y:
            if pos_x != pos_final_x:
                pos_x += 1
            else:
                pos_y += 1
            h = 0
            compteur = 0
            while h*x + pos_x < self.rows and h*y + pos_y < self.cols:
                if self.grid[pos_x + h*x][pos_y + h*y] == joueur:
                    compteur += 1
                else:
                    compteur = 0
                if compteur == 4:
                    return True
        return False


app = MyApp(application_id="github.lethargii.morpion")
app.run(sys.argv)

# Définir le socket du client
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# Se connecter au jeu
def nom():
    clientsocket.sendto(f"{BALISE_NEW_PLAYER}{input('Entrez votre nom : ')}".encode("utf-8"), ('localhost', 8080))


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
