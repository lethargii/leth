# -*- coding: utf-8 -*-
"""
TP1 de traitement d'images'
But:Isolation d'un nodule de tumeur'
Fait par Axel CHEVALLIER
03/12/2024
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import skimage
from skimage import io, morphology
#from scipy.ndimage import label #Importé 2 lignes plus loin
from skimage.measure import regionprops, label
from scipy.ndimage import label as ndi_label

################################
### 1-Etirement histogrammes ###
################################
imd=pd.read_csv("LungCut.csv",header=None)
img=imd.to_numpy()
io.imsave('image de base.png', (img * 255).astype(np.uint8))
plt.imshow(img,cmap="gray")
plt.title("Image de base")
#plt.show()
plt.close()

fig, ax = plt.subplots(2,2)
#print(str(img))
#cmap="Grays" (color map) pour mettre en niveau de gris . 0 est associé au blanc et 1 au noir.
#cmap="gray"  0 est associé au noir et 1 au blanc.
#
#vmin=0,vmax=1.00 pour éviter l'amélioration auto du contraste à l'affichage.

ax[0][0].imshow(img,cmap="gray",vmin=0,vmax=1.00)
ax[0][1].hist(img)
imgContraste=img/img.max()
ax[1][0].imshow(imgContraste,cmap="gray")
ax[1][1].hist(imgContraste)

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
seuil=seuil_optimal(img)
print("Seuil optimal:"+str(seuil))
#ax[1][0].imshow(img>0.49,cmap="Grays") test Threshold with 0.49
binaryImg=imgContraste<seuil
binaryImgb=(binaryImg).astype(np.uint8)#*255 
print(np.unique(binaryImgb))
plt.show()
plt.close()
fig, ax = plt.subplots(1,2)
ax[0].imshow(binaryImgb, cmap='gray' )#vmin=0, vmax=255
#withOutSmall=morphology.remove_small_holes(binaryImgb,area_threshold=10)
#ax[1].imshow(withOutSmall, cmap='gray',vmin=0, vmax=1.0 )#vmin=0, vmax=255
#print(np.array_equal(np.array(withOutSmall), np.array(binaryImgb)))

#io.imshow(binaryImg,cmap="Grays")
plt.close()
####################################
### 3 - Segmentation des poumons ###
####################################


# Fonction segmentation
#prend en argument les propriétés renvoyés par la fonction region props et
#renvoie les indices des pixels correspondant à la région contenant au
#moins N pixels et dont le centre se situe ....

def segmentation(statsB):
    N = 500 #completer
    X = 256#completer
    Y = 256 #completer
    centroids = np.array([region.centroid for region in statsB])
    areas = np.array([region.area for region in statsB])
    
    region_mask = (areas > N) & (centroids[:, 1] > X) & (centroids[:, 0] > Y)
    
    region_ids = [region.label for region, mask in zip(statsB, region_mask) if mask]
    
    return region_ids
io.imsave('image binaire.png', binaryImgb)
labeledImg=label(binaryImgb)
io.imsave('image labeled.png', (labeledImg ).astype(np.uint8))
plt.imshow(labeledImg, cmap = 'gray')
plt.show()
plt.close()
print(labeledImg)
regions=regionprops(labeledImg)
print("Segmentation:",segmentation(regions)) #TODO 
region_N = None
for region in regions:
    if region.label == 2:
        region_N = region
        break
regN=67
# Vérifier si la région avec l'étiquette N a été trouvée
if region_N is not None:
    # Créer une image vide de la même taille que l'image d'origine
    region_N_image = np.zeros_like(img, dtype=np.uint8)

    # Remplir la région avec l'étiquette N
    region_N_image[labeledImg == regN] = 255

    # Afficher l'image originale et l'image de la région N
    plt.subplot(1, 2, 1)
    plt.title('Image Originale')
    plt.imshow(img, cmap='gray')

    plt.subplot(1, 2, 2)
    plt.title('Région sélectionnée'+str(regN))
    plt.imshow(region_N_image, cmap='gray')

    plt.show()
else:
    print("Region with label N not found.")
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
pos=point_ref(img)
print("nodule:",pos)  #TODO Pourquoi les coordonnées sont à droite du poumonm gauche (qui est à droite sur l'image)?
imgRegion=regiongrowing(img,pos[0],pos[1]) 
plt.close()
plt.title("Methode de croissance de région")
plt.imshow(imgRegion, cmap = 'gray')
plt.show()
