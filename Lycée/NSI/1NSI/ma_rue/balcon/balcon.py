#!/usr/bin/env python
# coding: utf-8

# In[ ]:

#balcon

# Dépendances
from ma_rue import rue, affiche
from rectangle import rectangle
from trait import trait 

# Définitions

# Fonction balcon()
def balcon(x,y):
    '''
    Dessine une porte fenêtre de largeur 30 pixels et 50 pixels en hauteur
    avec une vitre de couleur 'Azure' le jour au contour noir,
    devancé d'un balcon constitué de traits noirs d'épaisseur 3 pixels.
    Paramètres :
        x est l'abcisse du milieu de la base de la porte-fenetre
        y est l'ordonnée du sol du niveau de la porte-fenetre
    '''
    
    # porte-fenetre
    
    rectangle(x -15, y, 30, 50, f"rgb{( 240, 255, 255)}")
    
    
    # balcon
    #lignes horizontales
    rue.line_width = 3
    trait(x +5,y -25,x -35,y -25)
    trait(x +5,y,x -35,y)
    
    #ligne verticale centrale 
    trait(x -15, y,x -15,y -25)
    
    #lignes verticales
    for balcon in range (1, 5):
        trait(x -(balcon *5) -15,y,x -(balcon *5) -15,y -25)
        trait(x +(balcon *5) -15,y,x +(balcon *5) -15,y -25)
    rue.line_width=1

if __name__ == '__main__':
    
    # Tests
    affiche(rue)
    balcon(rue.width/2,rue.height)

