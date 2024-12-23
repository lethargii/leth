# -*- coding: utf-8 -*-
"""
TP2 traitement Image CUPGE 2 ESIR
Lucien Sevault Wolber et Marc Prince
L'objectif de ce TP est d'améliorer la qualité d'une image issue d'imageries médicales
10/12/2024
"""
#Bibliothèques nécessaires
import numpy as np  
import matplotlib.pyplot as plt 
from skimage import io  
from scipy.ndimage import convolve
from skimage import util
from math import exp, log10

################################
### 1-Chargement de l'image ####
################################

# On charge l'image 'neuro.jpeg' avec la fonction 'imread'
image = io.imread("neuro.jpeg")

# On conserve seulement le canal rouge de l'image et on convertit la matrice en chiffres réels
image_rouge = image[:, :, 0]
image_rouge = image_rouge.astype(float)

# On affiche l'image et son histogramme
plt.figure(1)
im = plt.imshow(image_rouge, cmap='gray')
plt.colorbar(im)
plt.title("Canal rouge de l'image")
plt.show()



################################
### 2-Débruitage de l'image ####
################################

# On crée une fonction pour discrétiser un filtre gaussien 
def gaussian(N: int = 9, sigma: float = 3.0) -> list[list[float]]:
    res = np.zeros((N,N), dtype = float)
    res[N//2][N//2] = 1
    for i in range(N):
        for j in range(N):
            res[i][j] = exp(-((i-N//2)**2/(2*sigma**2)+(j-N//2)**2/(2*sigma**2)))
    return res/res.sum()

# On applique le filtre gaussien par convolution à l'aide de la fonction convolve
image_flou_gaussien = convolve(image_rouge, gaussian(N=5, sigma = 1.1)).astype(float)

# On affiche l'image floutée par filtre gaussien
plt.figure(2)
im = plt.imshow(image_flou_gaussien, cmap='gray')
plt.colorbar(im)
plt.title("Image floutée (filtre gaussien)")
plt.show()

# On crée une fonction pour créer un filtre moyen
def moyen(N: int = 9) -> list[list[float]]:
    res = np.ones((N,N), dtype = float)
    return res/res.sum()

# On applique le filtre moyen par convolution à l'aide de la fonction convolve
image_flou_moyen = convolve(image_rouge, moyen(N=5)).astype(float)

# On affiche l'image floutée par filtre moyen
plt.figure(3)
im = plt.imshow(image_flou_moyen, cmap='gray')
plt.colorbar(im)
plt.title("Image floutée (filtre moyen)")
plt.show()

###################################
#### 3-Réhaussement de l'image ####
###################################

# On code en dur la matrice laplacienne
mat_laplacienne = [[0, 1, 0], [1, -4, 1], [0, 1, 0]]

# On applique le filtre laplacien par convolution à l'aide de la fonction convolve
image_laplacien = convolve(image_flou_gaussien, mat_laplacienne).astype(float)

# On affiche la carte de contraste obtenue
plt.figure(4)
im = plt.imshow(image_laplacien, cmap='gray')
plt.colorbar(im)
plt.title("Carte de contraste")
plt.show()

# On effectue un moyennage entre l'image originale et la carte de contraste
image_out = image_rouge + 0.4*image_laplacien

# On affiche l'image obtenue
plt.figure(5)
im = plt.imshow(image_out, cmap='gray')
plt.colorbar(im)
plt.title("Image Out")
plt.show()

####################################
############## 4-PSNR ##############
####################################

# On crée une fonction pour calculer l'écart quadratique moyen
def eqm(im1, im2) -> float:
    im3 = (im1-im2)**2
    return im3.sum()/(len(im3)*len(im3[0]))

# On créer une fonction pour calculer la PSNR
def psnr(im1, im2, d: int = 255) -> float:
    return 10*log10((d**2)/(eqm(im1, im2)))

#Ajouter du bruit à une image
def add_noise(image, noise_type="gaussian", var=0.01):
    if noise_type == "gaussian":
        noisy_image = util.random_noise(image, mode='gaussian', var=var)
        return (noisy_image * 255).astype(np.uint8) 
    return image

# On charge l'image 'lena.bmp' avec la fonction 'imread'
lena = io.imread("lena.bmp")

# On affiche l'image originale
plt.figure(6)
plt.plot()
im = plt.imshow(lena, cmap = 'gray')
plt.colorbar(im)
plt.title("Image originale")
plt.show()

# On bruite l'image grâce à la fonction 'add_noise'
lena_bruitee = add_noise(lena)

# On affiche l'image bruitée
plt.figure(7)
plt.plot()
im = plt.imshow(lena_bruitee, cmap = 'gray')
plt.colorbar(im)
plt.title("Image bruitée")
plt.show()

# On applique le filtre gaussien et le filtre laplacien à l'image pour débruiter l'image
lena_debruitee = convolve(lena_bruitee, gaussian(N = 9, sigma = 1.7))
lena_debruitee = np.clip(lena_debruitee + 0.4*convolve(lena_debruitee, mat_laplacienne), 0, 255).astype(np.uint8)

# On affiche l'image débruitée
plt.figure(8)
plt.plot()
im = plt.imshow(lena_debruitee, cmap = 'gray')
plt.colorbar(im)
plt.title("Image débruitée")
plt.show()

# On calcule la PSNR
print(psnr(lena_debruitee, lena_bruitee))
