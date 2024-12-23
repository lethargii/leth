---
title: "TP2 Traitement d'images"
subtitle: "Débruitage et réhaussement d'images médicales"
author: "Lucien Sevault Wolber et Marc Prince"
date: "10/12/2024"
geometry: margin=2cm
output:
  pdf_document: 
    latex_engine: xelatex
header-includes:
    - \usepackage{siunitx}
---
# Introduction

Dû à la nature du comportement de la lumière et de l'imprécision du matériel les images sont parfois de qualité non satisfaisante. Dans ce TP, nous verrons plusieurs techniques permettant d'améliorer la qualité visuelle d'une image, notamment en réduisant le bruit d'une image ou en réhaussant les contrastes d'une image.

## 1.

On charge l'image 'neuro.jpeg' avec la fonction 'imread'. On décide arbitrairement de ne garder que le canal rouge de l'image et on la convertit en chiffres réels pur pouvoir effectuer des calculs plus précis sur celle-ci.

On affiche l'image obtenu en nuances de gris avec une colorbar :  
![Image canal rouge](Figure_1.png)

## 2.

On crée un filtre gaussien grâce à la formule suivante :

$$f(x,y) = \exp\left[-\left(\frac{(x-x_0)^2}{2\sigma^2}+\frac{(y-y_0)^2}{2\sigma^2}\right)\right]$$

On applique le filtre gaussien à l'image par convolution :  
![Image flou gaussien](Figure_2.png)


On applique le filtre moyen à l'image par convolution :  
![Image flou moyen](Figure_3.png)

Le flou gaussien et le flou moyen ont quasiment le même effet. Il semble cependant que le filtre gaussien est plus "dou" que le filtre moyen.

## 3.

On implémente la matrice Laplacienne suivante :

\begin{center}
\begin{tabular}{ | c | c | c | }
\hline
0 & 1 & 0 \\ \hline
1 & -4 & 1 \\ \hline
0 & 1 & 0 \\
\hline
\end{tabular}
\end{center}

Par convolution, on applique le filtre laplacien à l'image :  
![Carte de contraste](Figure_4.png)

On effectue un moyennage entre l'image originale et celle obtenue précédemment (image_out = image_originale + 0.4*image_laplacien) :  
![Image out](Figure_5.png)

Le bruit a un peu été réduit par rapport à l'image originale.

## 4.

On crée une fonction pour calculer l'écart quadratique moyen (EQM) avec la formule suivante :  

$$\text{EQM} = \frac{1}{mn}\sum_{i=0}^{m-1}\sum_{j=0}^{n-1}(Image1(i,j)-Image2(i,j))^2$$

On crée une fonction pour calculer la PSNR (Peak Signal to Noise Ratio) avec la formule suivante :  

$$\text{PSNR} = 10\log_{10}\left(\frac{d^2}{EQM}\right)\text{ avec } d = 255$$

On charge l'image 'lena.bmp' avec la fonction 'imread' :  
![Lena](Figure_6.png)

On bruite l'image avec la fonction 'add_noise' :  
![Lena bruitée](Figure_7.png)

On débruite l'image en appliquant un filtre gaussien et un filtre laplacien comme fait plus tôt :  
![Lena débruitée](Figure_8.png)

On obtient une PSNR de $28,08$. Cela semble être correct mais on voit que l'image n'est pas bien débruitée.

# Conclusion

Pour conclure, les méthodes d'amélioration de la qualité d'une image vues dans ce TP sont bel et bien efficaces. Les filtres gaussien et moyen permettent bien de diminuer le bruit d'une image et le filtre laplacien permet bien de réhausser le contraste d'une image. Le rendu n'est cependant pas parfait car le réhaussement laplacien ne marche pas correctement si il reste du bruit après floutage.
