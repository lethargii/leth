---
title: "TP1 - Interpolation polynomiale"
subtitle: "Comment approcher une fonction par un polynome ?"
author: "Sevault Wolber Lucien et Marc Prince"
date: "27/02/2025"
---

# Introduction

## 1. Interpolation de Lagrange

### 1.

On crée la fonction polyLagrange(x,y), qui retourne p_n(x), le polynôme obtenu par l'interpolation de Lagrange à partir des coordonnées des n + 1 points d'interpolation (x_i, y_i).

On utilise la formule :  
$$p_n(x) = \sum_{i=0}^n f(x_i) \prod_{j=0, i\neq j}^n \frac{x-x_j}{x_i - x_j}$$

'''matlab

'''

### 2.

On crée un script test1.m et on teste la fonction polyLagrange sur une fonction polynomiale que l'on a choisi.

On affiche la courbe de la fonction choisie et de son polynome interpolateur:

![]()

## 2. Points équidistants et effet Runge

Soit la fonction $f(x) = \frac{1}{1 + 25x^2}$ dont on souhaite étudier l'efficacité de l'interpolation de Lagrange ainsi qu'identifier ses potentielles faiblesse sur l'intervalle [-1, 1]. On choisit n + 1 points d'interpolation équidistants.

On crée un nouveau script test2.m qui aura pour but d'étudier l'erreur d'interpolation en fonction de n.

### 1.

On représente le résultat de notre interpolation $p_n(x)$ pour différentes valeurs de n.

### 2.



## 3. Points de Tchebychev

### 1.

On crée la fonctionn tchebyPoints(a, b, n) qui retourne les n+1 points de Tchebychev dans l'intervalle $[a, b]$.

### 2.

On teste notre fonction tchebyPoints(a, b, n) pour différentes valeurs de a, b et n.

### 3.

On crée un nouveau script test3.m dans lequel on représente la fonction f(x) et le résultat de notre interpolation p_n(x) utilisant les points de Tchebychev pour différentes valeurs de n :  
![]()

Lorsque n augmente on ne constate pas le même phénomène que pour le cas de points équidistants.

## 4. Problèmes facultatifs

# Conclusion

# Suggestions pour les améliorations du TP

