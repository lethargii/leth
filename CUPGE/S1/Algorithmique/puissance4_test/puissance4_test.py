import doctest,time

def generer_grille_vide(nb_col,nb_lig) :
    """
    Fonction générant une grille vide de puissance 4 de taille nb_col x nb_lig.
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
    >>> affiche_grille([[1,1,2,1,2,1,1],[2,1,2,2,1,2,2],[0,2,1,1,0,1,2],[0,1,2,2,0,0,0],[0,1,2,1,0,0,0],[0,0,0,0,0,0,0]])
    +-+-+-+-+-+-+-+
    | | | | | | | |
    +-+-+-+-+-+-+-+
    | |X|O|X| | | |
    +-+-+-+-+-+-+-+
    | |X|O|O| | | |
    +-+-+-+-+-+-+-+
    | |O|X|X| |X|O|
    +-+-+-+-+-+-+-+
    |O|X|O|O|X|O|O|
    +-+-+-+-+-+-+-+
    |X|X|O|X|O|X|X|
    +-+-+-+-+-+-+-+
     0 1 2 3 4 5 6
    >>> affiche_grille([[1,2,1,2,1,2,1],[2,1,2,1,2,1,2],[1,2,1,2,1,2,1],[2,1,2,1,2,1,2],[1,2,1,2,1,2,1],[2,1,2,1,2,1,2]])
    +-+-+-+-+-+-+-+
    |O|X|O|X|O|X|O|
    +-+-+-+-+-+-+-+
    |X|O|X|O|X|O|X|
    +-+-+-+-+-+-+-+
    |O|X|O|X|O|X|O|
    +-+-+-+-+-+-+-+
    |X|O|X|O|X|O|X|
    +-+-+-+-+-+-+-+
    |O|X|O|X|O|X|O|
    +-+-+-+-+-+-+-+
    |X|O|X|O|X|O|X|
    +-+-+-+-+-+-+-+
     0 1 2 3 4 5 6

    >>> affiche_grille([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]])
    +-+-+-+-+-+-+-+
    | | | | | | | |
    +-+-+-+-+-+-+-+
    | | | | | | | |
    +-+-+-+-+-+-+-+
    | | | | | | | |
    +-+-+-+-+-+-+-+
    | | | | | | | |
    +-+-+-+-+-+-+-+
    | | | | | | | |
    +-+-+-+-+-+-+-+
    | | | | | | | |
    +-+-+-+-+-+-+-+
     0 1 2 3 4 5 6

    >>> affiche_grille([[0,1,0,2,0,1,0],[2,0,1,0,2,0,1],[0,2,0,1,0,2,0],[1,0,2,0,1,0,2],[0,1,0,2,0,1,0],[2,0,1,0,2,0,1]])
    +-+-+-+-+-+-+-+
    |O| |X| |O| |X|
    +-+-+-+-+-+-+-+
    | |X| |O| |X| |
    +-+-+-+-+-+-+-+
    |X| |O| |X| |O|
    +-+-+-+-+-+-+-+
    | |O| |X| |O| |
    +-+-+-+-+-+-+-+
    |O| |X| |O| |X|
    +-+-+-+-+-+-+-+
    | |X| |O| |X| |
    +-+-+-+-+-+-+-+
     0 1 2 3 4 5 6
    
    >>> affiche_grille([[0,1,2,0,1,2,0],[1,2,0,1,2,0,1],[2,0,1,2,0,1,2],[0,1,2,0,1,2,0],[1,2,0,1,2,0,1],[2,0,1,2,0,1,2]])
    +-+-+-+-+-+-+-+
    |O| |X|O| |X|O|
    +-+-+-+-+-+-+-+
    |X|O| |X|O| |X|
    +-+-+-+-+-+-+-+
    | |X|O| |X|O| |
    +-+-+-+-+-+-+-+
    |O| |X|O| |X|O|
    +-+-+-+-+-+-+-+
    |X|O| |X|O| |X|
    +-+-+-+-+-+-+-+
    | |X|O| |X|O| |
    +-+-+-+-+-+-+-+
     0 1 2 3 4 5 6
    """
    nb_col=len(grille[0])
    nb_lig=len(grille)
    cases=[' ','X','O']
    affichage='+-'*nb_col+'+\n'
    for lig in range(nb_lig):
        for col in range(nb_col):
            affichage+='|'+cases[grille[nb_lig-lig-1][col]]
        affichage+='|\n'
        affichage+='+-'*nb_col+'+\n'
    for col in range(nb_col):
        affichage+=' '+str(col)
    print(affichage)

def peut_jouer(grille,colonne):
    """
    Fonction renvoyant True si un joueur peut jouer dans la colonne colonne et False autrement.
    Arguments :
    - grille : une liste de listes d'entiers
    - colonne : un entier
    >>> peut_jouer([[1,1,2,1,2,1,1],[2,1,2,2,1,2,2],[0,2,1,1,0,1,2],[0,1,2,2,0,0,0],[0,1,2,1,0,0,0],[0,0,0,0,0,0,0]],0)
    True
    >>> peut_jouer([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]],1)
    True
    >>> peut_jouer([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]],13)
    False
    >>> peut_jouer([[1,1,1,1,1,1,1],[0,1,2,2,2,2,2],[0,0,1,2,2,2,2],[0,0,0,1,2,2,2],[0,0,0,0,1,2,2],[0,0,0,0,0,1,2]],4)
    True
    >>> peut_jouer([[1,1,1,1,1,1,1],[0,1,2,2,2,2,2],[0,0,1,2,2,2,2],[0,0,0,1,2,2,2],[0,0,0,0,1,2,2],[0,0,0,0,0,1,2]],5)
    False
    """
    if not colonne in range(len(grille[0])):
        return False
    if grille[-1][colonne]==0:
        return True
    return False

def joue(grille,colonne,joueur) :
    """
    Fonction modifiant la grille grille en ajoutant un jeton du joueur joueur dans la colonne colonne.
    Arguments :
    - grille : une liste de listes d'entiers
    - colonne : un entier
    - joueur : un entier
    """
    for lig in grille:
        if lig[colonne]==0:
            lig[colonne]=joueur
            return None

def a_gagne_vert_var1(grille,joueur):
    nb_col=len(grille[0])
    nb_lig=len(grille)
    for i in range(nb_lig):
        for j in range(nb_col):
            if grille[i][j]==joueur and i+4<nb_lig:
                if grille[i+1][j]==joueur and grille[i+2][j]==joueur and grille[i+3][j]==joueur:
                    return True
    return False

def a_gagne_hor_var1(grille,joueur) :
    nb_col=len(grille[0])
    nb_lig=len(grille)
    for i in range(nb_lig):
        for j in range(nb_col):
            if grille[i][j]==joueur and j+4<nb_col:
                if grille[i][j+1]==joueur and grille[i][j+2]==joueur and grille[i][j+3]==joueur:
                    return True
    return False

def a_gagne_diag1_var(grille,joueur) :
    nb_col=len(grille[0])
    nb_lig=len(grille)
    for i in range(nb_lig):
        for j in range(nb_col):
            if grille[i][j]==joueur and j+4<nb_col and i+4<nb_lig:
                if grille[i+1][j+1]==joueur and grille[i+2][j+2]==joueur and grille[i+3][j+3]==joueur:
                    return True
    return False

def a_gagne_diag2_var(grille,joueur) :
    nb_col=len(grille[0])
    nb_lig=len(grille)
    for i in range(nb_lig):
        for j in range(nb_col):
            if grille[i][j]==joueur and j+4<nb_col and i-4>=0:
                if grille[i-1][j+1]==joueur and grille[i-2][j+2]==joueur and grille[i-3][j+3]==joueur:
                    return True
    return False

def a_gagne_vert_var2(grille,joueur):
    nb_col=len(grille[0])
    nb_lig=len(grille)
    compteur=0
    j=0
    while j<nb_col:
        i=0
        while i<nb_lig-3+compteur:
            if grille[i][j]==joueur:
                compteur+=1
                if compteur==4:
                    return True
            else:
                compteur=0
            i+=1
        compteur=0
        j+=1
    return False

def a_gagne_hor_var2(grille,joueur) :
    nb_col=len(grille[0])
    nb_lig=len(grille)
    compteur=0
    i=0
    while i<nb_lig:
        j=0
        while j<nb_col-3+compteur:
            if grille[i][j]==joueur:
                compteur+=1
                if compteur==4:
                    return True
            else:
                compteur=0
            j+=1
        compteur=0
        i+=1
    return False

def a_gagne_vert(grille,joueur):
    """
    Fonction vérifiant si le joueur joueur a aligné verticalement 4 jetons dans la grille grille.
    Arguments :
    - grille : une liste de listes d'entiers
    - joueur : un entier
    >>> a_gagne_vert([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]],1)
    False
    >>> a_gagne_vert([[2,1,2,2,0,0,0],[0,1,0,0,0,0,0],[0,1,0,0,0,0,0],[0,1,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]],1)
    True
    >>> a_gagne_vert([[1,1,1,2,1,1,1],[0,0,0,0,0,0,2],[0,0,0,0,0,0,2],[0,0,0,0,0,0,2],[0,0,0,0,0,0,2],[0,0,0,0,0,0,0]],2)
    True
    >>> a_gagne_vert([[0,1,1,2,1,1,1],[0,0,0,0,0,0,1],[0,0,0,0,0,0,2],[0,0,0,0,0,0,2],[0,0,0,0,0,0,2],[0,0,0,0,0,0,2]],2)
    True
    >>> a_gagne_vert([[1,2,1,1,0,0,0],[2,2,0,0,0,0,0],[1,0,0,0,0,0,0],[1,0,0,0,0,0,0],[2,0,0,0,0,0,0],[2,0,0,0,0,0,0]],2)
    False
    """
    nb_col=len(grille[0])
    nb_lig=len(grille)
    compteur=0
    for j in range(nb_col):
        i=0
        while i<nb_lig-3+compteur:
            if grille[i][j]==joueur:
                compteur+=1
                if compteur==4:
                    return True
            else:
                compteur=0
            i+=1
    return False

def a_gagne_hor(grille,joueur) :
    """
    Fonction vérifiant si le joueur joueur a aligné horizontalement 4 jetons dans la grille grille.
    Arguments :
    - grille : une liste de listes d'entiers
    - joueur : un entier
    >>> a_gagne_hor([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]],1)
    False
    >>> a_gagne_hor([[1,1,1,1,2,2,2],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]],1)
    True
    >>> a_gagne_hor([[2,2,2,1,1,1,1],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]],1)
    True
    >>> a_gagne_hor([[0,0,0,2,1,1,1],[0,0,0,2,1,1,2],[0,0,0,1,2,2,1],[0,0,0,1,1,1,2],[0,0,0,2,1,1,1],[0,0,0,2,2,2,2]],2)
    True
    >>> a_gagne_hor([[0,0,0,0,1,1,2],[0,0,0,0,0,1,2],[0,0,0,0,0,1,0],[0,0,0,0,0,1,0],[0,0,0,0,0,2,0],[0,0,0,0,0,2,0]],2)
    False
    """
    nb_col=len(grille[0])
    nb_lig=len(grille)
    compteur=0
    for i in range(nb_lig):
        j=0
        while j<nb_col-3+compteur:
            if grille[i][j]==joueur:
                compteur+=1
                if compteur==4:
                    return True
            else:
                compteur=0
            j+=1
    return False

def a_gagne_diag1(grille,joueur) :
    """
    Fonction vérifiant si le joueur joueur a aligné 4 jetons dans une diagonale montante de la grille grille.
    Arguments :
    - grille : une liste de listes d'entiers
    - joueur : un entier
    >>> a_gagne_diag1([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]],1)
    False
    >>> a_gagne_diag1([[2,2,1,1,2,1,1],[1,1,2,1,1,2,2],[1,2,2,2,1,1,2],[1,2,2,2,1,0,1],[2,2,1,1,2,0,2],[1,1,1,2,2,0,1]],1)
    True
    >>> a_gagne_diag1([[1,2,1,2,1,2,1],[2,1,2,1,2,1,2],[0,2,1,1,0,0,0],[0,0,2,1,0,0,0],[0,0,0,2,0,0,0],[0,0,0,0,0,0,0]],2)
    True
    >>> a_gagne_diag1([[1,2,2,1,2,0,0],[0,1,2,2,0,0,0],[0,0,1,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]],1)
    True
    >>> a_gagne_diag1([[0,0,0,2,1,2,1],[0,0,0,0,2,1,1],[0,0,0,0,0,2,1],[0,0,0,0,0,0,2],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]],2)
    True
    """
    nb_col=len(grille[0])
    nb_lig=len(grille)
    compteur=0
    j=0
    while j<nb_col-3:
        k=0
        while k<nb_lig and k+j<nb_col-3+compteur:
            if grille[k][k+j]==joueur:
                compteur+=1
                if compteur==4:
                    return True
            else:
                compteur=0
            k+=1
        j+=1
    compteur=0
    i=1
    while i<nb_lig-3:
        k=0
        while k<nb_col and k+i<nb_lig-3+compteur:
            if grille[k+i][k]==joueur:
                compteur+=1
                if compteur==4:
                    return True
            else:
                compteur=0
            k+=1
        i+=1
    return False

def a_gagne_diag2(grille,joueur) :
    """
    Fonction vérifiant si le joueur joueur a aligné 4 jetons dans une diagonale descendante de la grille grille.
    Arguments :
    - grille : une liste de listes d'entiers
    - joueur : un entier
    >>> a_gagne_diag2([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]],1)
    False
    >>> a_gagne_diag2([[1,1,2,1,1,2,2],[2,2,1,1,2,1,1],[2,1,1,2,2,2,1],[1,0,1,2,2,2,1],[2,0,2,1,1,2,2],[1,0,2,2,1,1,1]],1)
    True
    >>> a_gagne_diag2([[1,2,1,2,1,2,1],[2,1,2,1,2,1,2],[0,0,0,1,1,2,0],[0,0,0,1,2,0,0],[0,0,0,2,0,0,0],[0,0,0,0,0,0,0]],2)
    True
    >>> a_gagne_diag2([[0,0,2,1,2,2,1],[0,0,0,2,2,1,0],[0,0,0,1,1,0,0],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]],1)
    True
    >>> a_gagne_diag2([[1,2,1,2,0,0,0],[1,1,2,0,0,0,0],[1,2,0,0,0,0,0],[2,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]],2)
    True
    """
    nb_col=len(grille[0])
    nb_lig=len(grille)
    compteur=0
    j=0
    while j<nb_col-3:
        k=0
        while k<nb_lig and k+j<nb_col-3+compteur:
            if grille[nb_lig-1-k][k+j]==joueur:
                compteur+=1
                if compteur==4:
                    return True
            else:
                compteur=0
            k+=1
        j+=1
    compteur=0
    i=1
    while i<nb_lig-3:
        k=0
        while k<nb_col and k+i<nb_lig-3+compteur:
            if grille[nb_lig-1-k-i][k]==joueur:
                compteur+=1
                if compteur==4:
                    return True
            else:
                compteur=0
            k+=1
        i+=1
    return False

def a_gagne(grille,joueur) :
    """
    Fonction vérifiant si le joueur joueur a aligné 4 jetons dans la grille grille.
    Arguments :
    - grille : une liste de listes d'entiers
    - joueur : un entier
    >>> a_gagne([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]],1)
    False
    >>> a_gagne([[0,2,1,1,1,1,0],[0,2,2,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]],1)
    True
    >>> a_gagne([[2,1,1,1,2,1,1],[2,0,0,0,0,0,0],[2,0,0,0,0,0,0],[2,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]],2)
    True
    >>> a_gagne([[1,2,2,1,2,0,0],[0,1,2,2,0,0,0],[0,0,1,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]],1)
    True
    >>> a_gagne([[1,2,1,2,0,0,0],[1,1,2,0,0,0,0],[1,2,0,0,0,0,0],[2,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]],2)
    True
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
        for case in ligne:
            if case==0:
                return False
    return True

def boucle_principale() :
    grille=generer_grille_vide(7,6)
    joueur_courant=1
    while not grille_pleine(grille):
        affiche_grille(grille)
        prochain_coup=input("Dans quelle colonne le joueur "+str(joueur_courant)+" veut-il placer son pion ?")
        coup_valable=False
        if prochain_coup.isnumeric():
            if peut_jouer(grille,int(prochain_coup)):
                coup_valable=True
        while not coup_valable:
            print("Impossible de jouer ce coup")
            affiche_grille(grille)
            prochain_coup=input("Dans quelle colonne le joueur "+str(joueur_courant)+" veut-il placer son pion ?")
            if prochain_coup.isnumeric():
                if peut_jouer(grille,int(prochain_coup)):
                    coup_valable=True
        joue(grille,int(prochain_coup),joueur_courant)
        if a_gagne(grille,joueur_courant):
            print("Le joueur "+str(joueur_courant)+" a gagné.")
            return None
        joueur_courant=joueur_courant%2+1
    print("Match nul")

if __name__ == "__main__" :
    doctest.testmod()
    # boucle_principale()
    grille=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
    a=time.time()
    a_gagne_diag2_var(grille,1)
    b=time.time()
    print(b-a)
    a=time.time()
    a_gagne_diag2(grille,1)
    b=time.time()
    print(b-a)
