#toit2

# Dépendances
from ma_rue import rue, affiche
from trait import trait
from math import pi

# Définitions

# Fonction toit2()

def toit2(x, niveau):
    '''
    Paramètres :
        x : abcisse du centre du toit
        y_sol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    '''
    y = rue.height - niveau * 60 # ordonnée de la base du toit
   
    # trait horizontal
    rue.line_width=8
    trait(x-70,y-4,x+70,y-4)
    rue.line_width=1
    
    #bords du toit
    rue.fill_style="black"
    rue.fill_arc(x-70,y-4,4,0,2*pi)
    rue.fill_arc(x+70,y-4,4,0,2*pi)
    
# Tests
if __name__ == '__main__':
    affiche(rue)
    for n in range(6) :
        toit2(rue.width/2, n)