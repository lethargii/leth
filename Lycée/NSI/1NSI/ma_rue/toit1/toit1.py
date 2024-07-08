#toit1

# Dépendances
from ma_rue import rue, affiche 
from ipycanvas import Canvas
from ma_rue import rue, affiche
# Définitions

# Fonction toit1()
def toit1(x, niveau):
    '''
    Dessine un triangle plein de couleur noir de 40 pixels de haut
    et avec une base de 160 pixels 
    Paramètres :
        x : abcisse du centre du toit
        niveau : numero du niveau (0 pour les rdc, ...)
    '''
    

        
    y = rue.height - niveau * 60 # ordonnée de la base du toit
    
    rue.begin_path();
    rue.fill_style = 'black';
    rue.move_to(x-74,y)
    rue.line_to(x,y-40);
    rue.line_to(x+74,y);
    rue.close_path();
    rue.fill();
    
    # Tests
if __name__ == '__main__':
    affiche(rue)
    toit1(rue.width/2, 0)

    # Autres tests
    for i in range(5) :
        for j in range(1, 6) :
            toit1(0 + 200 * i, j)
