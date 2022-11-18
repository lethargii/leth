# Première implémentation pour les piles
def creer_pile():
    '''Renvoie une pile vide'''
    return []

def est_vide(pile):
    '''Renvoie un booléen, True si la pile est vide et False sinon'''
    return p == []

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

def sommet(pile):
    
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

def mettre_disques(pile, n):
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

def creation_tours(n):
    ''' renvoie une liste de 3 piles,
    la première correspond à la pile des n disques,
    les autres étant vides.'''
    tour = Pile()
    mettre_disques(tour, n)
    tours = [tour,[],[]]
    return tours