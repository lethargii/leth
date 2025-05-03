##########################
#    TP Probabilites     #
#TP1 : Aiguille de Buffon#
##########################

import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt

#Parametres


a = 10 #Ecart entre les lignes
N = 7 #nombre de lignes horizontales
L = a #longueur du baton

#Tracé des lignes
plt.figure()
for i in range(N+1):
    plt.plot([0,N*a],[i*a,i*a],color = 'black')
    plt.plot([i*a,i*a],[0,N*a],color = 'black')
    plt.xlim([0,N*a])
    plt.ylim([0,N*a+1e-2])
    
N_essais = 100                      # Nombre de lancers
N_realisations = 0                  # Nombre de realisations de l'evenement E
historique = np.zeros(N_essais)     # historique de la proba estimee

for i in range(N_essais):
    
    #Tirer l'angle phi du baton avec l'axe horizontal (utiliser la fonction rand du module random)
    phi = rd.rand()*np.pi
    #Tirer la position du centre M (toujours avec la fonction rand)
    XM = rd.rand()*N*a
    YM = rd.rand()*N*a
    
    #Calcul des coordonnees des extremites du baton (fonction cos et sin de Numpy)
    X1 = XM-np.cos(phi)*L/2
    X2 = XM+np.cos(phi)*L/2
    Y1 = YM-np.sin(phi)*L/2
    Y2 = YM+np.sin(phi)*L/2
    
    #test de l'intersection (A l'aide de la fonction floor de Numpy)
    if int(np.floor(Y2/a)) - int(np.floor(Y1/a)) != 0:
        N_realisations += 1
        
    #Calcul de la proba estimee au i-eme lancer
    historique[i] = N_realisations/(i+1)
    
    #affichage du lancer
    plt.plot([X1,X2],[Y1,Y2])
    
#Affichage des infos sur la visualisation
plt.title('Essais = '+str(N_essais)+', Reussites = '+str(N_realisations)+', Pr. estimee = '+str(historique[-1])+', Pr. theo = '+str(np.around(2/np.pi*L/a,4)))

#Trace de la courbe de l'historique avec la probabilite theorique associee
plt.figure()
plt.plot(historique)
plt.plot([0,historique.size],[2/np.pi*L/a,2/np.pi*L/a])
plt.xlabel('Indice realisation')
plt.title('Probabilite estimee au cours des iterations et theorique')
plt.show()
