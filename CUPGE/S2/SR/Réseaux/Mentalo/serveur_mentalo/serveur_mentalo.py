# Importer les modules doctest et socket
import doctest
import socket
from random import randint
from time import time,sleep

# Définir les variables des balises utilisées
BALISE_NEW_PLAYER = "__player__:"
BALISE_QUIT = "__quit__"

def nb_hasard(level):
    nb = randint(1,9)
    if level >= 2:
        nb += randint(1,9)*10
    if level == 3:
        nb += randint(1,9)*100
    return nb

def addition(level):
    if level == 1:
        nb1,nb2 = nb_hasard(2),nb_hasard(2)*int(2*(randint(0,1)-0.5))
    elif level >= 2:
        nb1,nb2 = nb_hasard(3),nb_hasard(3)*int(2*(randint(0,1)-0.5))
    res = nb1 + nb2
    if nb2 > 0:
        chaine = f"{nb1} + {nb2} ="
    elif nb2 < 0:
        chaine = f"{nb1} - {-nb2} ="
    return str(res),chaine

def produit(level):
    division = randint(0,1)
    if level == 1:
        nb1,nb2 = nb_hasard(1),nb_hasard(1)
    elif level == 2:
        nb1,nb2 = nb_hasard(2),nb_hasard(1)
    elif level == 3:
        nb1,nb2 = nb_hasard(2),nb_hasard(2)
    res = nb1 * nb2
    if division:
        nb1,res = res,nb1 
    if not division:
        chaine = f"{nb1} x {nb2} ="
    else:
        chaine = f"{nb1} : {nb2} ="
    return str(res),chaine

def choix_operation(level):
    choix = randint(0,1)
    if choix:
        return addition(level)
    else:
        return produit(level)

def choix_joueur():
    return randint(0,3)

def connection_joueur(serveursocket):
    """
    Fonction attendant de recevoir une demande de connection d'un joueur.
    Arguments :
        - serveursocket : Le socket du serveur
    """
    data, joueur = b'', ('', 0)
    while data.decode('utf-8')[0:len(BALISE_NEW_PLAYER)] != BALISE_NEW_PLAYER:
        data, joueur = serveursocket.recvfrom(1024)
    serveursocket.sendto(f"Welcome {data.decode('utf-8')[len(BALISE_NEW_PLAYER):]} !".encode('utf-8'),joueur)
    return data.decode('utf-8')[len(BALISE_NEW_PLAYER):], joueur


def envoyer_operation(serveursocket, chaine, joueurs, joueur_recv, joueur_send):
    """
    Fonction envoyant la grille aux joueurs.
    Arguments :
        - serveursocket : Le socket du serveur
        - grille : Un tableau représentant une grille de morpion
        - joueurs : Un tuple contenant les noms et adresses des joueurs
    """
    serveursocket.sendto(f"{joueurs[joueur_send][0]} - {chaine}".encode('utf-8'), joueurs[joueur_recv][1])


def mauvais_res(serveursocket, joueurs, joueur_send):
    """
    Fonction annonçant au joueur qu'il ne peut pas effectuer le coup qu'il a rentré.
    Arguments :
        - serveursocket : Le socket du serveur
        - joueurs : Un tuple contenant les noms et adresses des joueurs
        - joueur_courant : Un entier représentant le joueur courant
    """
    serveursocket.sendto("Unvalid result!".encode('utf-8'), joueurs[joueur_send][1])

def delai(serveursocket, joueurs, joueur_send):
    """
    Fonction annonçant au joueur qu'il ne peut pas effectuer le coup qu'il a rentré.
    Arguments :
        - serveursocket : Le socket du serveur
        - joueurs : Un tuple contenant les noms et adresses des joueurs
        - joueur_courant : Un entier représentant le joueur courant
    """
    serveursocket.sendto("You weren't fast enough!".encode('utf-8'), joueurs[joueur_send][1])

def bon_res(serveursocket, joueurs, joueur_send):
    """
    Fonction annonçant au joueur qu'il ne peut pas effectuer le coup qu'il a rentré.
    Arguments :
        - serveursocket : Le socket du serveur
        - joueurs : Un tuple contenant les noms et adresses des joueurs
        - joueur_courant : Un entier représentant le joueur courant
    """
    serveursocket.sendto("That is correct!".encode('utf-8'), joueurs[joueur_send][1])


def recv_res(serveursocket, joueurs, joueur_send):
    """
    Fonction attendant de recevoir le coup souhaité par le joueur courant.
    Arguments :
        - serveursocket : Le socket du serveur
        - joueurs : Un tuple contenant les noms et adresses des joueurs
        - joueur_courant : Un entier représentant le joueur courant
    """
    data, joueur = serveursocket.recvfrom(1024)
    while joueur != joueurs[joueur_send][1]:
        serveursocket.sendto("It's not your turn!".encode('utf-8'), joueur)
        data, joueur = serveursocket.recvfrom(1024)
    return data.decode('utf-8')

def niveau_reussi(serveursocket, joueurs, level):
    """
    Fonction envoyant aux joueurs le signal de fin de partie.
    Arguments :
        - serveursocket : Le socket du serveur
        - joueurs : Un tuple contenant les noms et adresses des joueurs
    """
    for joueur in joueurs:
        serveursocket.sendto(f"You've completed the level {level}!".encode('utf-8'), joueur[1])

def niveau_suivant(serveursocket, joueurs, level):
    """
    Fonction envoyant aux joueurs le signal de fin de partie.
    Arguments :
        - serveursocket : Le socket du serveur
        - joueurs : Un tuple contenant les noms et adresses des joueurs
    """
    for joueur in joueurs:
        serveursocket.sendto(f"Level {level}!".encode('utf-8'), joueur[1])

def envoyer_score(serveursocket, joueurs, level, score):
    """
    Fonction envoyant aux joueurs le signal de fin de partie.
    Arguments :
        - serveursocket : Le socket du serveur
        - joueurs : Un tuple contenant les noms et adresses des joueurs
    """
    for joueur in joueurs:
        serveursocket.sendto(f"Score - {score}/{scores[level-1]}".encode('utf-8'), joueur[1])



def fin_de_partie(serveursocket, joueurs):
    """
    Fonction envoyant aux joueurs le signal de fin de partie.
    Arguments :
        - serveursocket : Le socket du serveur
        - joueurs : Un tuple contenant les noms et adresses des joueurs
    """
    for joueur in joueurs:
        serveursocket.sendto("__quit__".encode('utf-8'), joueur[1])

scores = [10,10,5]
times = [15,15,10]

def boucle_principale():
    serveursocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serveursocket.bind(('localhost', 8080))
    joueurs = (connection_joueur(serveursocket), connection_joueur(serveursocket), connection_joueur(serveursocket), connection_joueur(serveursocket))
    sleep(5)
    for level in [1,2,3]:
        niveau_suivant(serveursocket, joueurs, level)
        sleep(3)
        level_cleared = False
        while not level_cleared:
            res_correct = True
            score = 0
            envoyer_score(serveursocket, joueurs, level, score)
            while score < scores[level-1] and res_correct:
                joueur_recv = choix_joueur()
                joueur_send = choix_joueur()
                res,chaine = choix_operation(level)
                envoyer_operation(serveursocket, chaine, joueurs, joueur_recv, joueur_send)
                time1 = time()
                if recv_res(serveursocket,joueurs,joueur_send) != res:
                    res_correct = False
                    mauvais_res(serveursocket, joueurs, joueur_send)
                time2 = time()
                if times[level-1] < time2-time1:
                    res_correct = False
                    delai(serveursocket, joueurs, joueur_send)
                if res_correct:
                    bon_res(serveursocket, joueurs, joueur_send)
                    score += 1
                    envoyer_score(serveursocket, joueurs, level, score)
            if score == scores[level-1]:
                level_cleared = True
                niveau_reussi(serveursocket, joueurs, level)
    fin_de_partie(serveursocket,joueurs)





if __name__ == "__main__":
    # Doctest
    doctest.testmod()
    # Lancer le jeu
    boucle_principale()
