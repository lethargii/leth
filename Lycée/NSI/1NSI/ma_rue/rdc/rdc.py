#rdc

# Dépendances
from ma_rue import rue, affiche
from facade import facade
from portes import portes
from fenetre import fenetre
from random import randint

# Définitions

# Fonction rdc()
def rdc(x, couleur):
    '''
    Dessine le rdc sur une facade au niveau do sol de la rue
    avec une seule porte et 2 fenêtres placées aléatoirement.
    Paramètres
        x : abscisse du milieu de la base du RDC
        couleur : couleur fixée par l'immeuble        
    '''
    # Dessine la facade
    facade(x,couleur,0)
    
    # Choix d'une distribution
    position=[0,0,0]
    position_porte=randint(0,2)
    position[position_porte]=1
    
    
        # dessiner une porte
    
    
        # dessiner une fenetre
    for k in range(3):
        if position[k]==0:
            fenetre(x-40+(40*k),rue.height-20)
        else:
            portes(x-40+(40*k),rue.height)

# Tests
if __name__ == '__main__':
    from couleur_aleatoire import couleur_aleatoire
    affiche(rue)
    for i in range(7) :
        rdc(i*160, couleur_aleatoire())