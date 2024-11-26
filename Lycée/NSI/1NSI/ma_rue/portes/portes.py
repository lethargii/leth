#portes

# Dépendances
from ma_rue import rue, affiche
from rectangle import rectangle
from trait import trait
from couleur_aleatoire import couleur_aleatoire
from math import pi
from random import randint

# Définitions

# Fonction portes()
def portes(x,y):
    '''
    Dessine une porte de 50 pixels en largeur et 70 pixels en hauteur
    La forme du haut de la porte est aléatoirement rectangulaire ou arrondi
    La couleur pleine de remplissage est choisi aléatoirement parmi les couleurs HTML valides
    Paramètres :
        x est l'abcisse du milieu de la base de la porte
        y est l'ordonnée du sol du niveau de la porte        
    ''' 
    couleur=couleur_aleatoire()
    choix_porte=randint(0,1)
    if choix_porte==0:
        rectangle(x, y, 30, 50, couleur)
    else:
        rectangle(x, y, 30, 30, couleur)
        rue.fill_style=couleur
        rue.fill_arc(x, y-35, 15, 0, 2*pi)
    
        trait(x-15,y-35,x-15,y)
        trait(x-15,y,x+15,y)
        trait(x+15,y,x+15,y-35)
        rue.stroke_arc(x,y-35,15,pi,2*pi,False)
    
    
    # Tests
if __name__ == '__main__':
    affiche(rue)
    for i in range(21) :
        portes(0 + i * 40,rue.height)