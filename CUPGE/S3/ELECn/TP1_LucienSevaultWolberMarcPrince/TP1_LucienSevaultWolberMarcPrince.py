# -*- coding: utf-8 -*-
"""
TP1 de traitement d'images'
Fonctions et librairies nécéssaires au TP
Lucien Sevault Wolber et Marc Prince
L'objectif de ce script est d'isoler sur une image de poumon un nodule
03/12/2024
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from skimage import io, morphology
from scipy.ndimage import label
from skimage.measure import regionprops, label
from scipy.ndimage import label as ndi_label

################################
### 1-Etirement histogrammes ###
################################

# On récupère l'image sous format matriciel
data = pd.read_csv('LungCut2.csv', header=None)
# On convertit la matrice au format numpy
im = data.to_numpy()

# On crée un plot avec 2 lignes et 5 colonnes
fig, ax = plt.subplots(2, 4)
# On affiche l'image et son histogramme
ax[0][0].imshow(im, cmap = 'gray')
ax[0][0].set_title("Image originale")
ax[1][0].hist(im, color = ['gray']*len(im))
ax[1][0].set_title("Histogramme de l'image originale")

# On effectue une transformation d'intensités linéaire
im_lin = im/im.max()
# On affiche l'image après la transformation d'intensités linéaire et on affiche son histogramme
ax[0][1].imshow(im_lin, cmap = 'gray')
ax[0][1].set_title("Image après transformation d'intensités linéaire")
ax[1][1].hist(im_lin, color = ['gray']*len(im_lin))
ax[1][1].set_title("Histogramme de l'image après \ntransformation d'intensités linéaire")

####################################################
### 2 - Binarisation et opérateur morphologiques ###
####################################################

# Seuil optimal
def seuil_optimal(Im):

    hi = np.zeros(100)
    delta = (np.max(Im) - np.min(Im)) / 100
    I = np.arange(np.min(Im), np.max(Im), delta)
    
    for i in range(len(I)):
        hi[i] = np.sum((Im > I[i]) & (Im < I[i] + delta))
    
    # Recherche automatique du seuil
    bestseuil = 1
    best_sigma = 0
    sigma = 0  
    mu1 = 0 
    mu2 = 0  
    
    for seuil in range(1, len(hi) - 1):
        q1 = np.sum(hi[:seuil])
        q2 = np.sum(hi[seuil:])
        mu1 = np.sum(hi[:seuil] * np.arange(1, seuil + 1)) / q1 if q1 != 0 else 0
        mu2 = np.sum(hi[seuil:] * np.arange(seuil + 1, len(hi) + 1)) / q2 if q2 != 0 else 0
        sigma = q1 * q2 * (mu1 - mu2) ** 2
        
        if sigma >= best_sigma:
            best_sigma = sigma
            bestseuil = seuil
    
    bestseuil = bestseuil / 100
    return bestseuil

# On détermine le seuil optimal avec la fonction seuil_optimal
seuil = seuil_optimal(im_lin)

# On passe l'image en noir et blanc et on l'affiche
imbw = (im_lin < seuil).astype(np.uint8)
ax[0][2].set_title("Image après binarisation")
ax[0][2].imshow(imbw, cmap = 'gray')

# On utilise la bibliothèque morphologie pour enlever le bruit en faisant une ouverture puis une fermeture et on affiche le résultat
im_no_noise = morphology.closing(morphology.opening(imbw.astype(bool), morphology.disk(3)), morphology.disk(3))
ax[0][3].set_title("Image après ouverture et fermeture")
ax[0][3].imshow(im_no_noise, cmap = 'gray')

####################################
### 3 - Segmentation des poumons ###
####################################


# Fonction segmentation
#prend en argument les propriétés renvoyés par la fonction regionprops et
#renvoie les indices des pixels correspondant à la région contenant au
#moins N pixels et dont le centre se situe dans la partie en bas à gauche de l'image

def segmentation(statsB):
    N =  500
    X =  256
    Y =  256
    centroids = np.array([region.centroid for region in statsB])
    areas = np.array([region.area for region in statsB])
    
    region_mask = (areas > N) & (centroids[:, 1] > X) & (centroids[:, 0] > Y)
    
    region_ids = [region.label for region, mask in zip(statsB, region_mask) if mask]
    
    return region_ids

# On labellise l'image
label_im = label(im_no_noise)
# On trouve l'identifiant de la région du poumon en triant les régions grâce à la fonction segmentation
id_cancer = segmentation(regionprops(label_im))
# On crée une image où seul le poumon gauche est présent et on l'affiche
im_cancer = 1 - np.isin(label_im, id_cancer)
ax[1][2].set_title("Image après segmentation du poumon gauche")
ax[1][2].imshow(im_cancer, cmap = 'gray')

################################
### 4 - Croissance de région ###
################################

# Point de référence
def point_ref(Im):

    labeled_array, _ = ndi_label(Im) 
    
    statsL = regionprops(labeled_array)
    
    areas = np.array([region.area for region in statsL])
    
    maxA_idx = np.argsort(areas)[-2]  
    
    # Indice du premier pixel de cette région
    pixel_idx_list = statsL[maxA_idx].coords  
    point = pixel_idx_list[0]  
    
    # Coordonnées X et Y à partir du pixel
    X = point[0]  
    Y = point[1]  
    
    X += 1
    
    return X, Y


# Croissance de région
def regiongrowing(I, x, y, reg_maxdist=0.2):

    J = np.zeros_like(I, dtype=bool)
    
    Isizes = I.shape
    
    reg_mean = I[x, y]
    reg_size = 1
    
    neg_free = 10000
    neg_pos = 0
    neg_list = np.zeros((neg_free, 3))
    
    pixdist = 0
    
    neigb = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while pixdist < reg_maxdist and reg_size < I.size:
        for j in range(4):
            xn = x + neigb[j][0]
            yn = y + neigb[j][1]
            
            xn, yn = int(np.round(xn)), int(np.round(yn))
            
            if 0 <= xn < Isizes[0] and 0 <= yn < Isizes[1]:
                if J[xn, yn] == 0:
                    neg_pos += 1
                    neg_list[neg_pos, :] = [xn, yn, I[xn, yn]]
                    J[xn, yn] = 1
        
        if neg_pos + 10 > neg_free:
            neg_free += 10000
            neg_list = np.resize(neg_list, (neg_free, 3))
        
        dist = np.abs(neg_list[:neg_pos, 2] - reg_mean)
        pixdist, index = np.min(dist), np.argmin(dist)
        
        J[x, y] = 2
        reg_size += 1
        
        reg_mean = (reg_mean * reg_size + neg_list[index, 2]) / (reg_size + 1)
        
        x, y = int(neg_list[index, 0]), int(neg_list[index, 1])
        
        neg_list[index, :] = neg_list[neg_pos, :]
        neg_pos -= 1
    
    return J >= 1

# On utilise la fonction point_ref pour trouver les coordo
x, y = point_ref(im_cancer)

# On utilise la fonction regiongrowing pour isoler le nodule dans une image et on l'affiche
im_growing = regiongrowing(im_cancer, x, y, 0.35)
ax[1][3].set_title("Image après isolation du nodule")
ax[1][3].imshow(im_growing, cmap = 'gray')

# Afficher les images et les histogrammes
plt.tight_layout()
plt.show()
