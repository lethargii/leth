# Exercice 6
def double(n):
    return 'Le double de '+str(n)+' est '+str(2*n)+'.'

# Exercice 7
def calcule_prix_total(nb_personnes):
    if nb_personnes==0:
        prix=0
    elif nb_personnes==1:
        prix=10
    elif nb_personnes<4:
        prix=8*nb_personnes
    elif nb_personnes<6:
        prix=7*nb_personnes
    else:
        prix=6*nb_personnes
    return prix

# Exercice 9
def minimum_trois(a,b,c):
    if a<b:
        if a<c:
            mini=a
        else:
            mini=c
    else:
        if b<c:
            mini=b
        else:
            mini=c
    return min

# Exercice 14
def somme_k(n):
    somme=0
    k=0
    while k**2+3*k<n:
        somme+=k**2+3*k
        k+=1
    return somme

# Exercice 15
def punition():
    for i in range(50):
        print('Je dois ranger ma chambre')

# Exercice 16
def chanson(n):
    for i in range(n):
        print("C'est dans "+str(n-i)+" je m'en irai j'entends le loup le renard chanter")

# Exercice 17
def h(n):
    produit=1
    for i in range(1,n+1):
        produit*=i**i
    return produit

def s(n):
    somme=0
    for i in range(1,n+1):
        somme+=h(i)

# Exercice 18
from math import cos,sin,tan,exp
def u(n):
    u=1
    for i in range(n):
        u+=cos(u)
    return u

def v(n):
    v0=1
    v1=0
    v2=0
    for i in range(n-1):
        v2=v1+sin(v0)
        v0=v1
        v1=v2
    return v2

def w(n):
    w=1
    for i in range(n):
        w=tan(w)+i+1
    return w

# Exercice 19
def population_bacteries(n: int) -> float:
    toxine=0
    nb_bacteries=1
    while nb_bacteries!=0:
        if n>0:
            n-=1
            toxine+=nb_bacteries*((toxine+1)*exp(-toxine))
            nb_bacteries+=1
        else:
            nb_bacteries=0
    return toxine

# Exercice 20
def champernowne(n):
    pass

# Exercice 21
def somme_carre_tab(tableau):
    somme=0
    for element in tableau:
        somme+=element**2
    return somme

def produit_tab(tableau):
    produit=1
    for element in tableau:
        produit*=element
    return produit

def maximum(tableau):
    maxi=tableau[0]
    for element in tableau:
        if element>maxi:
            maxi=element
    return maxi

def indice_maximum(tableau):
    indice_maxi=0
    for i in range(len(tableau)):
        if tableau[i]>tableau[indice_maxi]:
            indice_maxi=i
    return indice_maxi

def miroir(tableau):
    tableau_miroir=[]
    for i in range(len(tableau)):
        tableau_miroir+=tableau[-i-1]
    return tableau_miroir

def maximum_tab(t1,t2):
    t3=[]
    for i in range(len(t1)):
        if t1[i]>t2[i]:
            t3+=t1[i]
        else:
            t3+=t2[i]
    return t3

def compte