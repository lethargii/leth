import doctest
import socket

BALISE_NEW_PLAYER = "__player__:"
BALISE_QUIT = "__quit__"

def generer_grille_vide(nb_col,nb_lig) :
    """
    Fonction générant une grille vide de morpion de taille nb_col x nb_lig.
    Arguments :
    - nb_col : un entier
    - nb_lig : un entier
    >>> generer_grille_vide(7,6)
    [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
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

def affiche_grille(grille) :
    """
    Fonction affichant la grille grille.
    Arguments :
    - grille : une liste de listes d'entiers
    """
    nb_col=len(grille[0])
    nb_lig=len(grille)
    cases=[' ','X','O']
    affichage=' '+'+-'*nb_col+'+\n'
    for lig in range(nb_lig):
        affichage+=chr(lig+65)
        for col in range(nb_col):
            affichage+='|'+cases[grille[nb_lig-lig-1][col]]
        affichage+='|\n'
        affichage+=' '+'+-'*nb_col+'+\n'
    nombres=[str(i) for i in range(1,nb_col+1)]
    for decimal in range(len(nombres[-1])):
        affichage+=' '
        for nombre in nombres:
            if nombre[decimal:decimal+1]=='':
                affichage+='  '
            else:
                affichage+=' '+nombre[decimal:decimal+1]
        affichage+='\n'
    return affichage

def peut_jouer(grille,position):
    """
    Fonction renvoyant True si un joueur peut jouer dans la case position et False autrement.
    Arguments :
    - grille : une liste de listes d'entiers
    - position : une chaine de caractère au format LN où L est une lettre entre A et T compris et N est un entier entre 1 et 20 compris
    """
    if (not ord(position[0])-65 in range(len(grille))) or (not int(position[1:])-1 in range(len(grille[0]))) :
        return False
    if grille[len(grille)-ord(position[0])+64][int(position[1:])-1]==0:
        return True
    return False

def joue(grille,position,joueur) :
    """
    Fonction modifiant la grille grille en ajoutant un jeton du joueur joueur dans la colonne colonne.
    Arguments :
    - grille : une liste de listes d'entiers
    - position : une chaine de caractère au format LN où L est une lettre entre A et T compris et N est un entier entre 1 et 20 compris
    - joueur : un entier
    """
    grille[len(grille)-ord(position[0])+64][int(position[1:])-1]=joueur


def a_gagne_vert(grille,joueur):
    """
    Fonction vérifiant si le joueur joueur a aligné verticalement 5 jetons dans la grille grille.
    Arguments :
    - grille : une liste de listes d'entiers
    - joueur : un entier
    """
    nb_col=len(grille[0])
    nb_lig=len(grille)
    compteur=0
    for j in range(nb_col):
        i=0
        while i<nb_lig-4+compteur:
            if grille[i][j]==joueur:
                compteur+=1
                if compteur==5:
                    return True
            else:
                compteur=0
            i+=1
    return False

def a_gagne_hor(grille,joueur) :
    """
    Fonction vérifiant si le joueur joueur a aligné horizontalement 5 jetons dans la grille grille.
    Arguments :
    - grille : une liste de listes d'entiers
    - joueur : un entier
    """
    nb_col=len(grille[0])
    nb_lig=len(grille)
    compteur=0
    for i in range(nb_lig):
        j=0
        while j<nb_col-4+compteur:
            if grille[i][j]==joueur:
                compteur+=1
                if compteur==5:
                    return True
            else:
                compteur=0
            j+=1
    return False

def a_gagne_diag1(grille,joueur) :
    """
    Fonction vérifiant si le joueur joueur a aligné 5 jetons dans une diagonale montante de la grille grille.
    Arguments :
    - grille : une liste de listes d'entiers
    - joueur : un entier
    """
    nb_col=len(grille[0])
    nb_lig=len(grille)
    compteur=0
    j=0
    while j<nb_col-4:
        k=0
        while k<nb_lig and k+j<nb_col-4+compteur:
            if grille[k][k+j]==joueur:
                compteur+=1
                if compteur==5:
                    return True
            else:
                compteur=0
            k+=1
        j+=1
    compteur=0
    i=1
    while i<nb_lig-4:
        k=0
        while k<nb_col and k+i<nb_lig-4+compteur:
            if grille[k+i][k]==joueur:
                compteur+=1
                if compteur==5:
                    return True
            else:
                compteur=0
            k+=1
        i+=1
    return False

def a_gagne_diag2(grille,joueur) :
    """
    Fonction vérifiant si le joueur joueur a aligné 5 jetons dans une diagonale descendante de la grille grille.
    Arguments :
    - grille : une liste de listes d'entiers
    - joueur : un entier
    """
    nb_col=len(grille[0])
    nb_lig=len(grille)
    compteur=0
    j=0
    while j<nb_col-4:
        k=0
        while k<nb_lig and k+j<nb_col-4+compteur:
            if grille[nb_lig-1-k][k+j]==joueur:
                compteur+=1
                if compteur==5:
                    return True
            else:
                compteur=0
            k+=1
        j+=1
    compteur=0
    i=1
    while i<nb_lig-4:
        k=0
        while k<nb_col and k+i<nb_lig-4+compteur:
            if grille[nb_lig-1-k-i][k]==joueur:
                compteur+=1
                if compteur==5:
                    return True
            else:
                compteur=0
            k+=1
        i+=1
    return False

def a_gagne(grille,joueur) :
    """
    Fonction vérifiant si le joueur joueur a aligné 5 jetons dans la grille grille.
    Arguments :
    - grille : une liste de listes d'entiers
    - joueur : un entier
    """
    return a_gagne_vert(grille,joueur) or a_gagne_hor(grille,joueur) or a_gagne_diag1(grille,joueur) or a_gagne_diag2(grille,joueur)

def grille_pleine(grille) :
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
            if colonne==0:
                return False
    return True

def connection_joueur(serveursocket):
    data, joueur = b'',('', 0)
    while data.decode('utf-8')[0:len(BALISE_NEW_PLAYER)]!=BALISE_NEW_PLAYER:
        data, joueur = serveursocket.recvfrom(1024)
    serveursocket.sendto(f"Bienvenue {data.decode('utf-8')[len(BALISE_NEW_PLAYER):]} !".encode('utf-8'),joueur)
    return data.decode('utf-8')[len(BALISE_NEW_PLAYER):], joueur

def envoyer_grille(serveursocket,grille,joueurs):
    affichage = affiche_grille(grille)
    serveursocket.sendto(affichage.encode('utf-8'),joueurs[0][1])
    serveursocket.sendto(affichage.encode('utf-8'),joueurs[1][1])

def demander_coup(serveursocket,joueurs, joueur_courant):
    serveursocket.sendto("Dans quelle case voulez-vous placer votre pion ?".encode('utf-8'), joueurs[joueur_courant][1])

def mauvais_coup(serveursocket,joueurs, joueur_courant):
    serveursocket.sendto("Vous ne pouvez pas jouer ce coup.".encode('utf-8'), joueurs[joueur_courant][1])

def recv_coup(serveursocket,joueurs, joueur_courant):
    data, joueur = serveursocket.recvfrom(1024)
    while joueur!=joueurs[joueur_courant][1] or (joueur not in joueurs[0] and joueur not in joueurs[1]):
        serveursocket.sendto("Ce n'est pas à votre tour de jouer.".encode('utf-8'), joueurs[(joueur_courant+1)%2][1])
        data, joueur = serveursocket.recvfrom(1024)
    return data.decode('utf-8')

def debut_de_partie(serveursocket, joueurs):
    serveursocket.sendto(f"Vous jouez contre {joueurs[1][0]} !".encode('utf-8'),joueurs[0][1])
    serveursocket.sendto(f"Vous jouez contre {joueurs[0][0]} !".encode('utf-8'),joueurs[1][1])

def prochain_tour(serveursocket, joueurs, joueur_courant):
    serveursocket.sendto(f"C\'est au tour de {joueurs[joueur_courant][0]} !".encode('utf-8'),joueurs[0][1])
    serveursocket.sendto(f"C\'est au tour de {joueurs[joueur_courant][0]} !".encode('utf-8'),joueurs[1][1])

def partie_gagnee(serveursocket, joueurs, joueur_courant):
    serveursocket.sendto(f"{joueurs[joueur_courant][0]} a gagné !".encode('utf-8'),joueurs[0][1])
    serveursocket.sendto(f"{joueurs[joueur_courant][0]} a gagné !".encode('utf-8'),joueurs[1][1])

def match_nul(serveursocket, joueurs):
    serveursocket.sendto("Match nul !".encode('utf-8'),joueurs[0][1])
    serveursocket.sendto("Match nul !".encode('utf-8'),joueurs[1][1])

def fin_de_partie(serveursocket, joueurs):
    serveursocket.sendto("__quit__".encode('utf-8'),joueurs[0][1])
    serveursocket.sendto("__quit__".encode('utf-8'),joueurs[1][1])

def boucle_principale() :
    serveursocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serveursocket.bind(('localhost', 8080))
    joueurs = (connection_joueur(serveursocket), connection_joueur(serveursocket))
    debut_de_partie(serveursocket, joueurs)
    grille=generer_grille_vide(3,3)
    joueur_courant=0
    while not grille_pleine(grille):
        envoyer_grille(serveursocket,grille, joueurs)
        prochain_tour(serveursocket, joueurs, joueur_courant)
        demander_coup(serveursocket,joueurs, joueur_courant)
        prochain_coup = recv_coup(serveursocket,joueurs, joueur_courant)
        coup_valable=False
        if len(prochain_coup)>=2 and type(prochain_coup[0])==str and prochain_coup[1:].isnumeric():
            if peut_jouer(grille,prochain_coup):
                coup_valable=True
        while not coup_valable:
            mauvais_coup(serveursocket,joueurs, joueur_courant)
            demander_coup(serveursocket,joueurs, joueur_courant)
            prochain_coup = recv_coup(serveursocket,joueurs, joueur_courant)
            if len(prochain_coup)>=2 and type(prochain_coup[0])==str and prochain_coup[1:].isnumeric():
                if peut_jouer(grille,prochain_coup):
                    coup_valable=True
        joue(grille,prochain_coup,joueur_courant+1)
        if a_gagne(grille,joueur_courant+1):
            partie_gagnee(serveursocket, joueurs, joueur_courant)# print("Le joueur "+str(joueur_courant+1)+" a gagné.")
            fin_de_partie(serveursocket, joueurs)
            return
        joueur_courant=(joueur_courant+1)%2
    match_nul(serveursocket, joueurs)
    fin_de_partie(serveursocket, joueurs)

if __name__ == "__main__" :
    doctest.testmod()
    boucle_principale()
