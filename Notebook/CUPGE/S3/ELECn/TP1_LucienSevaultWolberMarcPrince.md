---
title: "TP1 Traitement d'images"
subtitle: "Opérateurs morphologiques et segmentation"
author: "Lucien Sevault Wolber et Marc Prince"
date: "03/12/2024"
geometry: margin=2cm
output:
  pdf_document: 
    latex_engine: xelatex
header-includes:
    - \usepackage{siunitx}
---
# Introduction

Il peut être utile de détecter les nodules en imagerie médicale car ce sont parfois des tumeurs malignes qui peuvent être à l'origine de cancers. Dans ce TP, nous allons traiter une image de scanner des poumons d'un patient atteint d'un cancer pour isoler un nodule (qui ici est certainement une tumeur maligne). Pour ce faire, nous utiliserons des transformations comme la transformation d'intensités linéaire, la segmentation, l'ouverture et la fermeture. 

## 1.

On affiche l'image 'LungCut.csv' (on voit bien le nodule dans le poumon gauche qui est à droite sur l'image) et son histogramme :  

![](11.png){ width=25% }

Les intensités les plus basse correspondent à l'arrière-plan et à l'intérieur des poumons (qui sont très sombres). Le reste des intensités correspond aux tissus et aux poumons (plus précisément les alvéoles). Il parait compliqué de faire la différence entre les tissus et les poumons sur l'histogramme.  
On utilise une transformation d'intensités linéaire pour étaler les intensités de 0 à 1 en utilisant la formule vue en TD :

$$I_2 = \frac{L - 1 - C}{max(I_1)-min(I_1)}(I_1-min(I_1)) + C$$

Ici, $min(I_1) = 0$, $C = 0$ et $L-1 = 1$

Il suffit alors de diviser chaque intensité par l'intensité max de l'image ($I_2 = \frac{I_1}{max(I_1)}$) :  

![](22.png){ width=25% }

L'intensité a bien été étalée de 0 à 1 (on le voit sur l'histogramme), mais on ne remarque pas d'amélioration nette de la qualité de l'image.

## 2.

En se basant sur le fait que l'arrière-plan est principalement composé des intensités les plus basses, nous prendrions un seuil de 0,2.  
Grâce à la fonction seuil_optimal on trouve un seuil de 0,35.  
On met tous les pixels dont l'intensité est inférieur au seuil à 0 (en noir) et ceux dont l'intensité est supérieur au seuil à 1 (en blanc) :  

![](33.png){ width=25% }

On cherche à nettoyer le bruit de l'image.  
On fait cela grâce à une ouverture (pour enlever le bruit dans les poumons) suivie d'une fermeture (pour enlever le bruit dans les tissus) :  

![](44.png){ width=25% }

En faisant cela, on modifie l'image mais le nodule en lui-même ne semble pas être trop impacté.

## 3.

Les propriétés d'une région permettant de différencier le poumon gauche des autres régions peuvent être l'air (area) et le centroïde (centroid).  
Arbitrairement, on décide de filtrer les régions tel qu'on obtienne celles ayant une aire supérieure à $500\si{px^2}$ et dont le centroïde soit dans la partie en bas à droite de l'image (On complète la fonction segmentation avec N = 500, X = 256, Y = 256).  
On affecte une intensité nulle aux pixels dont les coordonnées sont renvoyées par la fonction segmentation pour garder seulement le poumon gauche où se trouve le nodule :  

![](55.png){ width=25% }

On a bien isolé le poumon gauche avec le nodule.

## 4.

On utilise la fonction point_ref pour trouver les coordonnées d'un pixel d'intensité 1 appartenant au nodule. On obtient les coordonnées suivantes : X = 264, Y = 348.  
En utilisant la méthode de croissance regiongrowing, on segmente le nodule dans l'image originale en passant en paramètre les coordonnées trouvées précédemment. On obtient l'image suivante :  

![](66.png){ width=25% }

On a réussi à isoler le nodule sur l'image.

## 5.

On applique notre script sur le fichier 'LungCut2.csv'
On obtient les images suivantes :  

![LungCut2](Figure_2.png)

Comme pour le fichier 'LungCut.csv', on arrive bien à isoler le nodule dans le poumon gauche.

# Conclusion

Pour conclure, nous avons bien réussi à isoler le nodule dans le fichier LungCut.csv et LungCut2.csv. Cette première approche du traitement d'image nous a permis de découvrir plusieurs techniques pour modifier une image et pouvoir obtenir des données utilisables dans le domaine médicale.
