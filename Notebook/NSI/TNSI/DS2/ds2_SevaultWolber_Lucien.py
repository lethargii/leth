# Première implémentation pour les piles
def creer_pile():
    '''Renvoie une pile vide'''
    return []

def est_vide(pile):
    '''Renvoie un booléen, True si la pile est vide et False sinon'''
    return pile == []

def empiler(pile, element):
    '''Empile element au sommet de pile'''
    pile.append(element)
    
def depiler(pile):
    '''Renvoie et enlève la valeur du sommet de pile'''
    assert not est_vide(pile), "Pile vide"
    return pile.pop()

# Deuxième implémentation pour les piles
class Pile:

    '''classe Pile création d’une instance Pile avec une liste'''
    
    def __init__(self):
        '''Initialise une pile vide'''
        self.liste = []
        
    def est_vide(self):
        '''Renvoie un booléen, True si la pile est vide et False sinon'''
        return len(self.liste) == 0

    def empiler(self, element):
        '''Empile element au sommet de pile'''
        self.liste.append(element)

    def depiler(self):
        '''Renvoie et enlève la valeur du sommet de pile'''
        return self.liste.pop()

    def __repr__(self):
        return repr(self.liste)

def sommet(pile):
    
    ''' Renvoie la valeur au sommet de la pile mais sans la supprimer de la pile '''
    if est_vide(pile):
        raise IndexError('pile vide')
    sommet = depiler(pile)
    empiler(pile,sommet)
    return sommet

def sommet_poo(pile):
    
    ''' Renvoie la valeur au sommet de la pile mais sans la supprimer de la pile '''
    if pile.est_vide():
        raise IndexError('pile vide')
    sommet = pile.depiler()
    pile.empiler(sommet)
    return sommet

def mettre_disques(pile, n):
    '''met des disques de taille n à 1 sur la pile'''
    for disque in range(n):
        empiler(pile,n-disque)

def mettre_disques_poo(pile, n):
    '''met des disques de taille n à 1 sur la pile'''
    for disque in range(n):
        pile.empiler(n-disque)

def creation_tours(n):
    ''' renvoie une liste de 3 piles,
    la première correspond à la pile des n disques,
    les autres étant vides.'''
    tour = creer_pile()
    mettre_disques(tour, n)
    tours = [tour,[],[]]
    return tours

def creation_tours_poo(n):
    ''' renvoie une liste de 3 piles,
    la première correspond à la pile des n disques,
    les autres étant vides.'''
    tour = Pile()
    mettre_disques_poo(tour, n)
    tours = [tour,[],[]]
    return tours

def creation_tours_1(n):
    ''' renvoie une liste de 3 piles,
    la première correspond à la pile des n disques,
    les autres étant vides.'''
    p0 = creer_pile()
    p1 = creer_pile()
    p2 = creer_pile()
    mettre_disques(p0, n)
    return [p0, p1, p2]

def creation_tours_poo_1(n):
    ''' renvoie une liste de 3 piles,
    la première correspond à la pile des n disques,
    les autres étant vides.'''
    p0 = Pile()
    p1 = Pile()
    p2 = Pile()
    mettre_disques_poo(p0, n)
    return [p0, p1, p2]

def deplacer(tours, origine, cible):
    '''
    déplace la valeur au sommet de la pile d’indice origine vers le sommet de la pile d’indice cible.
    Si le déplacement n’est pas possible, parce qu’il ne respecte pas les règles du jeu, les piles ne sont pas modifiées.
    '''
    if not est_vide(tours[origine]):
        if est_vide(tours[cible]) or (sommet(tours[origine]) < sommet(tours[cible])):
            empiler(tours[cible],sommet(tours[origine]))
            depiler(tours[origine])

def deplacer_poo(tours, origine, cible):
    '''
    déplace la valeur au sommet de la pile d’indice origine vers le sommet de la pile d’indice cible.
    Si le déplacement n’est pas possible, parce qu’il ne respecte pas les règles du jeu, les piles ne sont pas modifiées.
    '''
    if not tours[origine].est_vide():
        if tours[cible].est_vide() or (sommet_poo(tours[origine]) < sommet_poo(tours[cible])):
            tours[cible].empiler(sommet_poo(tours[origine]))
            tours[origine].depiler()

def resoudre(tours, n, origine, cible, interm):
    if n==1:
        deplacer(tours, origine, cible)
    else:
        resoudre(tours, n-1, origine, interm, cible)
        deplacer(tours, origine, cible)
        resoudre(tours, n-1, interm, cible, origine)

def resoudre_poo(tours, n, origine, cible, interm):
    if n==1:
        deplacer_poo(tours, origine, cible)
    else:
        resoudre_poo(tours, n-1, origine, interm, cible)
        deplacer_poo(tours, origine, cible)
        resoudre_poo(tours, n-1, interm, cible, origine)

def nb_etapes(n):
    if n==1:
        return 1
    else:
        return 2*nb_etapes(n-1) + 1

def pile_vers_tableau(pile, n):
    '''
    
    '''
    tableau = [0]*n
    tmp = creer_pile()
    i = 0
    while not est_vide(pile):
        empiler(tmp,depiler(pile))
    while not est_vide(tmp):
        valeur = depiler(tmp)
        tableau[i] = valeur
        empiler(pile, valeur)
        i += 1
    return tableau

def pile_vers_tableau_poo(pile, n):
    '''
    
    '''
    tableau = [0]*n
    tmp = Pile()
    i = 0
    while not pile.est_vide():
        tmp.empiler(pile.depiler())
    while not tmp.est_vide():
        valeur = tmp.depiler()
        tableau[i] = valeur
        pile.empiler(valeur)
        i += 1
    return tableau

def tours_vers_matrice(tours, n) :
    matrice = []
    for tour in tours:
        matrice.append(pile_vers_tableau(tour, n))
    return matrice

def tours_vers_matrice_poo(tours, n) :
    matrice = []
    for tour in tours:
        matrice.append(pile_vers_tableau_poo(tour, n))
    return matrice

def affichage_matrice(matrice, n):
    for i in range(n):
        for liste in matrice:
            if liste[n-i-1] == 0:
                caractere = "|"
            else:
                caractere = liste[n-i-1]
            print(" " , caractere, end = "", sep = "")
        print()

def affichage_tours(tours, n) :
    matrice = tours_vers_matrice(tours, n)
    affichage_matrice(matrice, n)
    print(7*"=")

def resoudre(tours, n_disques, n, origine, cible, interm):
    if n==1:
        deplacer(tours, origine, cible)
        affichage_tours(tours, n_disques)
    else:
        resoudre(tours, n_disques, n-1, origine, interm, cible)
        deplacer(tours, origine, cible)
        affichage_tours(tours, n_disques)
        resoudre(tours, n_disques, n-1, interm, cible, origine)

def affichage_complexe(tours, n):
    matrice = tours_vers_matrice(tours,n)
    for i in range(n):
        for liste in matrice:
            if liste[n-i-1] == 0:
                caractere = "|"
            else:
                caractere = (liste[n-i-1]*2+1)*"="
            print(" "*(n-liste[n-i-1]) , caractere, " "*(n-liste[n-i-1]), end = "", sep = "")
        print()
    print(3*(2*n+1)*"_")

def resoudre(tours, n_disques, n, origine, cible, interm):
    if n==1:
        deplacer(tours, origine, cible)
        affichage_complexe(tours, n_disques)
    else:
        resoudre(tours, n_disques, n-1, origine, interm, cible)
        deplacer(tours, origine, cible)
        affichage_complexe(tours, n_disques)
        resoudre(tours, n_disques, n-1, interm, cible, origine)

from ipycanvas import Canvas
def affichage_canvas(tours, n) :
    matrice = tours_vers_matrice(tours,n)
    hanoi = Canvas(width = 30*(n*2+1), height = 50*n)
    hanoi.line_width = 10
    hanoi.fill_style = "red"
    for i in range(3):
        hanoi.fill_rect(((1+2*i)*hanoi.width/6)-5, 0, 10, hanoi.height)
    hanoi.fill_style = "black"
    for i in range(n):
        for j in range(3):
            if matrice[j][i] != 0:
                hauteur = 40
                largeur = 10*(matrice[j][i]*2)
                hanoi.fill_rect((j*2+1)*hanoi.width/6 - largeur/2, hanoi.height - i*50 - hauteur, largeur, hauteur)
    display(hanoi)

def resoudre(tours, n_disques, n, origine, cible, interm):
    if n==1:
        deplacer(tours, origine, cible)
        affichage_canvas(tours, n_disques)
    else:
        resoudre(tours, n_disques, n-1, origine, interm, cible)
        deplacer(tours, origine, cible)
        affichage_canvas(tours, n_disques)
        resoudre(tours, n_disques, n-1, interm, cible, origine)