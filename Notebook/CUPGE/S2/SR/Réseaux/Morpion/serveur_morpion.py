# Importer les modules doctest et socket
import doctest
import socket

# Définir les variables des balises utilisées
BALISE_NEW_PLAYER = "__player__:"
BALISE_QUIT = "__quit__"


def generer_grille_vide(nb_col, nb_lig):
    """
    Fonction générant une grille vide de morpion de taille nb_col x nb_lig.
    Arguments :
    - nb_col : un entier
    - nb_lig : un entier
    >>> generer_grille_vide(7,6) == [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
    True
    >>> generer_grille_vide(2,3)
    [[0, 0], [0, 0], [0, 0]]
    >>> generer_grille_vide(3,2)
    [[0, 0, 0], [0, 0, 0]]
    >>> generer_grille_vide(4,4)
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    >>> generer_grille_vide(2,6)
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    """
    return [[0]*nb_col for i in range(nb_lig)]


def affiche_grille(grille):
    """
    Fonction affichant la grille grille.
    Arguments :
    - grille : une liste de listes d'entiers
    """
    nb_col = len(grille[0])
    nb_lig = len(grille)
    cases = ['.', 'X', 'O']
    nombres = [str(i) for i in range(1, nb_col+1)]
    affichage = ""
    for lig in range(nb_lig):
        affichage += " "*(len(str(nombres[-1]))-len(str(lig)))+f"{lig}|"
        for col in range(nb_col):
            affichage += ' '+cases[grille[nb_lig-lig-1][col]]
        affichage += '\n'
    affichage += ' '*(len(str(nombres[-1]))+1)+"-"*nb_col*2+"\n"
    affichage += ' '*(len(str(nombres[-1]))+1)
    for col in range(nb_col):
        affichage += ' '+chr(col+ord("A"))
    affichage += "\n"
    return affichage


def peut_jouer(grille, position):
    """
    Fonction renvoyant True si un joueur peut jouer dans la case position et False autrement.
    Arguments :
    - grille : une liste de listes d'entiers
    - position : une chaine de caractère au format LN où L est une lettre entre A et T compris et N est un entier entre 1 et 20 compris
    """
    if (not ord(position[0])-65 in range(len(grille[0]))) or (not int(position[1:])-1 in range(len(grille))) :
        return False
    if grille[len(grille)-int(position[1:])-1][ord(position[0])-65] == 0:
        return True
    return False


def joue(grille, position, joueur):
    """
    Fonction modifiant la grille grille en ajoutant un jeton du joueur joueur dans la colonne colonne.
    Arguments :
    - grille : une liste de listes d'entiers
    - position : une chaine de caractère au format LN où L est une lettre entre A et T compris et N est un entier entre 1 et 20 compris
    - joueur : un entier
    """
    grille[len(grille)-int(position[1:])-1][ord(position[0])-65] = joueur


def a_gagne_vert(grille, joueur, nb):
    """
    Fonction vérifiant si le joueur joueur a aligné verticalement 5 jetons dans la grille grille.
    Arguments :
    - grille : une liste de listes d'entiers
    - joueur : un entier
    """
    nb_col = len(grille[0])
    nb_lig = len(grille)
    compteur = 0
    for j in range(nb_col):
        i = 0
        while i < nb_lig-(nb-1)+compteur:
            if grille[i][j] == joueur:
                compteur += 1
                if compteur == nb:
                    return True
            else:
                compteur = 0
            i += 1
    return False


def a_gagne_hor(grille, joueur, nb):
    """
    Fonction vérifiant si le joueur joueur a aligné horizontalement 5 jetons dans la grille grille.
    Arguments :
    - grille : une liste de listes d'entiers
    - joueur : un entier
    """
    nb_col = len(grille[0])
    nb_lig = len(grille)
    compteur = 0
    for i in range(nb_lig):
        j = 0
        while j < nb_col-(nb-1)+compteur:
            if grille[i][j] == joueur:
                compteur += 1
                if compteur == nb:
                    return True
            else:
                compteur = 0
            j += 1
    return False


def a_gagne_diag1(grille, joueur, nb):
    """
    Fonction vérifiant si le joueur joueur a aligné 5 jetons dans une diagonale montante de la grille grille.
    Arguments :
    - grille : une liste de listes d'entiers
    - joueur : un entier
    """
    nb_col = len(grille[0])
    nb_lig = len(grille)
    compteur = 0
    j = 0
    while j < nb_col-(nb-1):
        k = 0
        while k < nb_lig and k+j < nb_col-(nb-1)+compteur:
            if grille[k][k+j] == joueur:
                compteur += 1
                if compteur == nb:
                    return True
            else:
                compteur = 0
            k += 1
        j += 1
    compteur = 0
    i = 1
    while i < nb_lig-(nb-1):
        k = 0
        while k < nb_col and k+i < nb_lig-(nb-1)+compteur:
            if grille[k+i][k] == joueur:
                compteur += 1
                if compteur == nb:
                    return True
            else:
                compteur = 0
            k += 1
        i += 1
    return False


def a_gagne_diag2(grille, joueur, nb):
    """
    Fonction vérifiant si le joueur joueur a aligné 5 jetons dans une diagonale descendante de la grille grille.
    Arguments :
    - grille : une liste de listes d'entiers
    - joueur : un entier
    """
    nb_col = len(grille[0])
    nb_lig = len(grille)
    compteur = 0
    j = 0
    while j < nb_col-(nb-1):
        k = 0
        while k < nb_lig and k+j < nb_col-(nb-1)+compteur:
            if grille[nb_lig-1-k][k+j] == joueur:
                compteur += 1
                if compteur == nb:
                    return True
            else:
                compteur = 0
            k += 1
        j += 1
    compteur = 0
    i = 1
    while i < nb_lig-(nb-1):
        k = 0
        while k < nb_col and k+i < nb_lig-(nb-1)+compteur:
            if grille[nb_lig-1-k-i][k] == joueur:
                compteur += 1
                if compteur == nb:
                    return True
            else:
                compteur = 0
            k += 1
        i += 1
    return False


def a_gagne(grille, joueur, nb=5):
    """
    Fonction vérifiant si le joueur joueur a aligné 5 jetons dans la grille grille.
    Arguments :
    - grille : une liste de listes d'entiers
    - joueur : un entier
    """
    return a_gagne_vert(grille, joueur, nb) or a_gagne_hor(grille, joueur, nb) or a_gagne_diag1(grille, joueur, nb) or a_gagne_diag2(grille, joueur, nb)


def grille_pleine(grille):
    """
    Fonction retournant True si la grille grille est pleine et False sinon.
    Arguments :
    - grille : une liste de listes d'entiers
    >>> grille_pleine([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]])
    False
    >>> grille_pleine([[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1]])
    True
    >>> grille_pleine([[2,2,2,2,2,2,2],[2,2,2,2,2,2,2],[2,2,2,2,2,2,2],[2,2,2,2,2,2,2],[2,2,2,2,2,2,2],[2,2,2,2,2,2,2]])
    True
    >>> grille_pleine([[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,0]])
    False
    >>> grille_pleine([[2,2,2,2,2,2,2],[2,2,2,2,2,2,2],[2,2,2,2,2,2,2],[2,2,2,2,2,2,2],[2,2,2,2,2,2,2],[0,2,2,2,2,2,2]])
    False
    """
    for ligne in grille:
        for colonne in ligne:
            if colonne == 0:
                return False
    return True


def connection_joueur(serveursocket):
    """
    Fonction attendant de recevoir une demande de connection d'un joueur.
    Arguments :
        - serveursocket : Le socket du serveur
    """
    data, joueur = b'', ('', 0)
    while data.decode('utf-8')[0:len(BALISE_NEW_PLAYER)] != BALISE_NEW_PLAYER:
        data, joueur = serveursocket.recvfrom(1024)
    serveursocket.sendto(f"Bienvenue {data.decode('utf-8')[len(BALISE_NEW_PLAYER):]} !".encode('utf-8'),joueur)
    return data.decode('utf-8')[len(BALISE_NEW_PLAYER):], joueur


def envoyer_grille(serveursocket, grille, joueurs):
    """
    Fonction envoyant la grille aux joueurs.
    Arguments :
        - serveursocket : Le socket du serveur
        - grille : Un tableau représentant une grille de morpion
        - joueurs : Un tuple contenant les noms et adresses des joueurs
    """
    affichage = affiche_grille(grille)
    serveursocket.sendto(affichage.encode('utf-8'), joueurs[0][1])
    serveursocket.sendto(affichage.encode('utf-8'), joueurs[1][1])


def demander_coup(serveursocket, joueurs, joueur_courant):
    """
    Fonction envoyant une demande de coup au joueur courant.
    Arguments :
        - serveursocket : Le socket du serveur
        - joueurs : Un tuple contenant les noms et adresses des joueurs
        - joueur_courant : Un entier représentant le joueur courant
    """
    serveursocket.sendto("Entrez votre prochain coup :".encode('utf-8'), joueurs[joueur_courant][1])


def mauvais_coup(serveursocket, joueurs, joueur_courant):
    """
    Fonction annonçant au joueur qu'il ne peut pas effectuer le coup qu'il a rentré.
    Arguments :
        - serveursocket : Le socket du serveur
        - joueurs : Un tuple contenant les noms et adresses des joueurs
        - joueur_courant : Un entier représentant le joueur courant
    """
    serveursocket.sendto("Coup Invalide !".encode('utf-8'), joueurs[joueur_courant][1])


def recv_coup(serveursocket, joueurs, joueur_courant):
    """
    Fonction attendant de recevoir le coup souhaité par le joueur courant.
    Arguments :
        - serveursocket : Le socket du serveur
        - joueurs : Un tuple contenant les noms et adresses des joueurs
        - joueur_courant : Un entier représentant le joueur courant
    """
    data, joueur = serveursocket.recvfrom(1024)
    while joueur != joueurs[joueur_courant][1] or (joueur not in joueurs[0] and joueur not in joueurs[1]):
        serveursocket.sendto("Ce n'est pas à vous de jouer !".encode('utf-8'), joueurs[(joueur_courant+1)%2][1])
        data, joueur = serveursocket.recvfrom(1024)
    return data.decode('utf-8')


def debut_de_partie(serveursocket, joueurs):
    """
    Fonction annonçant aux joueurs le début de la partie et leur adversaire.
    Arguments :
        - serveursocket : Le socket du serveur
        - joueurs : Un tuple contenant les noms et adresses des joueurs
    """
    serveursocket.sendto(f"Vous jouez contre {joueurs[1][0]} !".encode('utf-8'), joueurs[0][1])
    serveursocket.sendto(f"Vous jouez contre {joueurs[0][0]} !".encode('utf-8'), joueurs[1][1])


def prochain_tour(serveursocket, joueurs, joueur_courant):
    """
    Fonction annonçant aux joueurs le prochain tour.
    Arguments :
        - serveursocket : Le socket du serveur
        - joueurs : Un tuple contenant les noms et adresses des joueurs
        - joueur_courant : Un entier représentant le joueur courant
    """
    serveursocket.sendto(f"C\'est au tour de {joueurs[joueur_courant][0]} !".encode('utf-8'), joueurs[0][1])
    serveursocket.sendto(f"C\'est au tour de {joueurs[joueur_courant][0]} !".encode('utf-8'), joueurs[1][1])


def partie_gagnee(serveursocket, joueurs, joueur_courant, grille):
    """
    Fonction annonçant aux joueurs que le joueur courant a remporté la partie.
    Arguments :
        - serveursocket : Le socket du serveur
        - joueurs : Un tuple contenant les noms et adresses des joueurs
        - joueur_courant : Un entier représentant le joueur courant
    """
    envoyer_grille(serveursocket, grille, joueurs)
    serveursocket.sendto(f"{joueurs[joueur_courant][0]} remporte la partie !\nLe jeu est terminé ! (Appuyez sur Ctrl+C pour quitter)".encode('utf-8'), joueurs[0][1])
    serveursocket.sendto(f"{joueurs[joueur_courant][0]} remporte la partie !\nLe jeu est terminé ! (Appuyez sur Ctrl+C pour quitter)".encode('utf-8'), joueurs[1][1])


def match_nul(serveursocket, joueurs):
    """
    Fonction annonçant aux joueurs que la partie s'est terminé sur un nul.
    Arguments :
        - serveursocket : Le socket du serveur
        - joueurs : Un tuple contenant les noms et adresses des joueurs
    """
    serveursocket.sendto("Match nul !".encode('utf-8'), joueurs[0][1])
    serveursocket.sendto("Match nul !".encode('utf-8'), joueurs[1][1])


def fin_de_partie(serveursocket, joueurs):
    """
    Fonction envoyant aux joueurs le signal de fin de partie.
    Arguments :
        - serveursocket : Le socket du serveur
        - joueurs : Un tuple contenant les noms et adresses des joueurs
    """
    serveursocket.sendto("__quit__".encode('utf-8'), joueurs[0][1])
    serveursocket.sendto("__quit__".encode('utf-8'), joueurs[1][1])


def coup_valable(prochain_coup, grille):
    """
    Fonction vérifiant si le coup donné par l'utilisateur est valable.
    Arguments :
        - prochain_coup : Une chaine de caractères représentant le coup de l'utilisateur
        - grille : Un tableau représentant une grille de morpion
    """
    if len(prochain_coup) >= 2 and type(prochain_coup[0]) is str and prochain_coup[1:].isnumeric() and peut_jouer(grille, prochain_coup):
        return True
    return False


def prochain_coup(serveursocket, joueurs, joueur_courant):
    """
    Fonction demandant au joueur qui doit jouer son prochain coup et le renvoie
    Arguments :
        - serveursocket : Le socket du serveur
        - joueurs : Un tuple contenant les noms et adresses des joueurs
        - joueur_courant : Un entier représentant le joueur courant
    """
    demander_coup(serveursocket, joueurs, joueur_courant)
    return recv_coup(serveursocket, joueurs, joueur_courant)


def boucle_principale():
    """
    Fonction représentant la boucle principale du jeu du Morpion
    """
    # Créer le socket du serveur et le lier à l'adresse de rebouclage locale et au port 8080
    serveursocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serveursocket.bind(('localhost', 8080))
    # Définir les noms et les adresses IP des joueurs
    joueurs = (connection_joueur(serveursocket), connection_joueur(serveursocket))
    # Initialiser la grille
    grille = generer_grille_vide(15, 15)
    # Initialisation de joueur_courant à 0
    joueur_courant = 0
    # Rester dans la boucle de jeu tant que la grille n'est pas pleine
    while not grille_pleine(grille):
        # Afficher la grille
        envoyer_grille(serveursocket, grille, joueurs)
        # Demander le coup
        coup = prochain_coup(serveursocket, joueurs, joueur_courant)
        # Tant que le coup n'est pas valable, afficher une erreur et le redemander
        while not coup_valable(coup, grille):
            mauvais_coup(serveursocket, joueurs, joueur_courant)
            coup = recv_coup(serveursocket, joueurs, joueur_courant)
        # Jouer le coup du joueur courant
        joue(grille, coup, joueur_courant+1)
        # Si le joueur courant a gagné la partie, l'afficher et terminer la partie
        if a_gagne(grille, joueur_courant+1, 5):
            partie_gagnee(serveursocket, joueurs, joueur_courant, grille)
            fin_de_partie(serveursocket, joueurs)
            return
        # Changer le joueur courant
        joueur_courant = (joueur_courant+1) % 2
    # Si la grille est pleine déclarer le match nul et terminer la partie
    match_nul(serveursocket, joueurs)
    fin_de_partie(serveursocket, joueurs)


if __name__ == "__main__":
    # Doctest
    doctest.testmod()
    # Lancer le jeu
    boucle_principale()
