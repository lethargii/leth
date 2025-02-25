---
title: "TP2 - Simulation de circuits électroniques"
author: "Lucien Sevault Wolber et Axel Chevallier"
date: 01/01/2025
header-includes:
    - \usepackage{siunitx}
---

# 1. Simulation de circuits en basse fréquence

## 1.1 Montage micro électret + amplificateur audio

$S = 0,0089\si{V/Pa}$

$P_\text{max} = 0,2\si{Pa}$

$U_\text{max} = S \cdot P_\text{max} = 0,0089 \times 0,2 = 0,00178\si{V}$

$U_\text{vol max} = 0,7\si{V}$

$A = \frac{U_\text{vol max}}{U_\text{max}} = \frac{0,7}{0,00178} = 393,258427$

## 1.2 Simulation en régime statique

## 1.3 Simulation temporelle

## 1.4 Simulation fréquentielle

# 2. Simulation d'une antenne en haute fréquence

Un maillage permet lors d'une simulation numérique de représenter la géométrie de manière discrète.

Une antenne Yagi-Uda est une antenne qui est utilisable des hautes fréquences jusqu'aux ultra hautes fréquences (elle est simple à réaliser et est notamment utilisée pour la télévision).

## 2.1 Visualisation de la géométrie de l'antenne

La longueur d'onde représente la période spatiale d'une onde électromagnétique.

$\lambda = \frac{c}{f} = \frac{3\cdot 10^8}{2,45 \cdot 10^9} = 0,122\si{m}$

On calcule le diamètre d des brins :

$d = 0,0085 \times \lambda = 0,0085 \times 0,122 = 0,00104 \si{m}$

On calcule la longueur du réflecteur et de chaque brin :

$l_1 = 0,482 \times \lambda = 0,482 \times 0,122 = 0,059 \si{m}$
$l_3 = 0,428 \times \lambda = 0,428 \times 0,122 = 0,0524 \si{m}$
$l_4 = 0,424 \times \lambda = 0,424 \times 0,122 = 0,0519 \si{m}$
$l_5 = 0,428 \times \lambda = 0,428 \times 0,122 = 0,0524 \si{m}$

On calcule la distance entre les brins :

$s_{ik} = 0,2 \times 0,122 = 0,0244 \si{m}$

On clique sur un brin et on récupère ses statistiques :  

numéro de brin : 6
nombre de segments : 11  
longueur : 0,0524 m  
rayon : 0,5204 mm
position de début : (0,0245, -0,026)
position de fin :  (0,0245, -0,026)

Cela correspond bien à la préparation.

## 2.2 Etude du fichier NEC

On regarde dans les différents onglets et on retrouve bien les différentes caractéristiques ud brin du 2.1.

## 2.3 Simulation fréquentielle

On clique sur l'icone de calculatrice et on coche Frequency sweep pour faire la simulation fréquentielle. On modifie les valeurs des fréquences de simulation pour qu'elle varie de 2000MHz à 3000MHz par pas de 10MHz et on clique sur Generate.

On relève la valeur du coefficient de réflexion minimal = -17,963 dB et la fréquence correspondante = 2480MHz. -17,963 est une bonne valeur de coefficient de réflexion minimal car elle est en dessous de -10dB.

La fréquence max pour le wifi est de 2472MHz donc la fréquence de 2480 Mhz ne peut pas correspondre. Pour un fonctionnement en wifi, on pourrait prendre une fréquence de 2470MHz.

## 2.4 Modification de la géométrie

On modifie la longueur de la boucle d'excitation à 0,0545 m et on refait une simulation. En augmentant la longue de la boucle le coefficient de réflexion minimal augmente drastiquement : -8,8

Une longueur de la boucle d'excitation de 0,051 m semble être la meilleur option pour une fréquence de 2,45 GHz.

## 2.5 Simulation en rayonnement

