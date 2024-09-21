#rue_finale

# Dépendances

from sol import sol
from immeuble import *

# Définitions


def rue_finale(canvas):
    
    # Affichage de ma rue
    affiche(canvas)
    
    
    # Dessin des immeubles
    for k in range(4):
        immeuble(rue.width/5*(k+1))
    
        
    # Dessin du sol de la rue
    sol()
    
# Tests
if __name__ == '__main__':
    rue_finale(rue)