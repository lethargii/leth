import matplotlib.pyplot as plt
import numpy as np
import doctest

color_table = [
    (66, 30, 15),
    (25, 7, 26),
    (9, 1, 47),
    (4, 4, 73),
    (0, 7, 100),
    (12, 44, 138),
    (24, 82, 177),
    (57, 125, 209),
    (134, 181, 229),
    (211, 236, 248),
    (241, 233, 191),
    (248, 201, 95),
    (255, 170, 0),
    (204, 128, 0),
    (153, 87, 0),
    (106, 52, 3)]

def prochains_termes(x,y,a,b) :
    """
    Fonction renvoyant les termes suivants des suites (x_n) et (y_n)
    Arguments :
    - x : un réel
    - y : un réel
    - a : un réel
    - b : un réel
    >>> prochains_termes(3,4,1,2)
    (-6, 26)
    >>> prochains_termes(0.5,0.1,1,3)
    (1.24, 3.1)
    >>> prochains_termes(0,0,2,2)
    (2, 2)
    >>> prochains_termes(5,5,5,5)
    (5, 55)
    >>> prochains_termes(0,0,0,0)
    (0, 0)
    """
    return x**2-y**2+a,2*x*y+b

def indice_divergence(x,y,a,b,n) :
    """
    Fonction récursive retournant l'indice n pour lequel x_n**2+y_n**2 est supérieur à 4 si n<=127 ou -1 sinon.
    Arguments :
    - x : un réel
    - y : un réel
    - a : un réel
    - b : un réel
    >>> indice_divergence(0,0,0.5,0.5,0)
    5
    >>> indice_divergence(0,0,0.01,0.1,0)
    -1
    >>> indice_divergence(0,0,-0.24,-0.9,0)
    8
    >>> indice_divergence(0,0,5,5,0)
    1
    >>> indice_divergence(0,0,0,0,0)
    -1
    """
    if n>127:
        return -1
    else:
        if x**2+y**2>4:
            return n
        else:
            x_1,y_1=prochains_termes(x,y,a,b)
            return indice_divergence(x_1,y_1,a,b,n+1)

def get_color(a,b) :
    """
    Fonction retournant la couleur associée à a et b.
    Arguments :
    - a : un réel
    - b : un réel
    >>> get_color(0.01,0.1)
    (0, 0, 0)
    >>> get_color(0.5,0.5)
    (12, 44, 138)
    >>> get_color(-0.24,-0.9)
    (134, 181, 229)
    >>> get_color(0,0)
    (0, 0, 0)
    >>> get_color(5,5)
    (25, 7, 26)
    """
    n=indice_divergence(0,0,a,b,0)
    if n==-1:
        return (0,0,0)
    return color_table[n%len(color_table)]

def create_image(x,y,l,h,nb_px,nb_py) :
    res = np.zeros((nb_px, nb_py, 3), dtype=np.uint8)
    for i in range(nb_px) :
        for j in range(nb_py) :
            res[i][j] = get_color(x+i*l/nb_px,y+j*h/nb_py)
    return res

if __name__ == "__main__":
    doctest.testmod()
    img = create_image(-2.,-1.25,2.5,2.5,500,500)
    # img = create_image(-0.7,0.5,0.3,0.3,500,500)
    # img = create_image(-0.58,0.626,0.03,0.03,500,500)

    plt.imshow(img)
    plt.axis("equal")
    plt.axis('off')
    plt.show()
