#différents imports
import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt

#ex 3
x = rd.normal(0,1,100)
mat = rd.normal(10,0.1,(5,5))

#ex 4
plt.figure()
plt.title('Représentation du vecteur aléatoire x')
plt.xlabel('Indice du vecteur')
plt.ylabel('Valeur')
plt.plot(x)

plt.figure()
plt.title('Représentation des vecteurs aléatoire de la matrice mat')
plt.xlabel('Indice du vecteur')
plt.ylabel('Valeur')
plt.plot(mat)

#ex 5

M=20
plt.figure()
plt.title('histogramme pour M=20')
plt.hist(x,M)

pas = 0.1
bins = np.arange(-3,3,pas)
plt.figure()
plt.title('histogramme avec arange')
plt.hist(x,bins)

#on test d'autres entiers pour M
M=10
plt.figure()
plt.title('histogramme pour M=10')
plt.hist(x,M)

M=40
plt.figure()
plt.title('histogramme pour M=40')
plt.hist(x,M)

# ex 6
sig=1 #ecart-type
m=0 #moyenne

x_px=np.arange(-3, 3, 0.05)
px=np.zeros(x_px.size)

for i in range(px.size):
    px[i]=1/(sig*np.sqrt(2*np.pi))*np.exp(-1/(2*sig**2)*(x_px[i]-m)**2)
plt.figure()
plt.hist(x, bins=30)
plt.plot(x_px, px, 'r-')
plt.title("Méthode boucle")

plt.figure()
plt.hist(x, bins=30, density=True)
plt.plot(x_px, px, 'r-')
plt.title("Méthode boucle density=True")

x_px=np.arange(-3,3,0.05)
px=1/(sig*np.sqrt(2*np.pi))*np.exp(-1/(2*sig**2)*(x_px-m)**2)
plt.figure()
plt.hist(x, bins=30)
plt.plot(x_px, px, 'r-')
plt.title("Méthode vectorisée")

plt.figure()
plt.hist(x, bins=30, density=True)
plt.plot(x_px, px, 'r-')
plt.title("Méthode vectorisée dentity=True")