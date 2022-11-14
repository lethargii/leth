#mon_module_toile

# Code de définition d'un nouveau canvas à enregistrer dans un fichier nommé mon_module_toile.py
from ipycanvas import Canvas
from math import pi, sin, cos


# Création d'une toile support pour le  dessin
toile = Canvas(width = int(input('Largeur en pixels ?')), height = int(input('Hauteur en pixels ?')))  
    
# Fonction point()
def point(x, y, couleur, taille) :
    # A compléter...
    toile.fill_style = couleur
    toile.fill_circle( x, y, taille)

# Fonction point_carre()
def point_carre(x, y, couleur, taille) :
    # A définir
    toile.fill_style = couleur
    toile.fill_rect(x-taille/2,y-taille/2,taille)
    
# Fonction cercle()
def cercle(x, y, couleur, taille, epaisseur) :
    # A définir
    toile.stroke_style = couleur
    toile.stroke_circle( x, y, taille)
    
# Fonction carre()
def carre(x, y, couleur, taille, epaisseur) :
    # A définir
    toile.stroke_style = couleur
    toile.stroke_rect(x-taille/2,y-taille/2,taille)