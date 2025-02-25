---
title: "TP1 - Électronique embarquée : ARDUINO"
author: "Lucien Sevault Wolber et Marc Prince"
date: 01/01/2025
---

# 1. Prise en main de la carte ARDUINO UNO

L'Arduino Uno est une carte à microcontrôleur open source développée par la société Arduino. Elle est équipée du microcontrôleur ATMEGA328P.

## 1.1 Programme de clignotement de la LED (Blink) - utilisation d'une sortie numérique

On lance le logiciel Arduino et on vérifie dans le menu Outils/Ports que la carte Arduino Uno est bien connectée.

Dans le menu Fichier/exemples, on ouvre le programme 01.Basics/Blink. On remarque la fonction setup qui est lancée une seule fois à l'allumage de la carte dans laquelle on initialise la pin LED_BUILTIN comme une sortie. Il y a aussi la fonction loop qui s'exécute indéfiniment et qui contient l'ensemble du programme.

Ce programme sert à faire clignoter la led sur la carte. Pour cela la suite d'instructions suivante est effectuée :  
- Mettre la tension à un niveau haut sur la sortie LED_BUILTIN (ce qui allume la LED)
- Attendre 1000 millisecondes (1 seconde)
- Mettre la tension à un niveau bas sur la sortie LED_BUILTIN (ce qui éteint la LED)
- Attendre 1000 millisecondes (1 seconde)

On branche une autre LED avec une résistance en série sur la sortie 12 et on rajoute des instructions.

Dans setup :
- On a rajouté la pin 12 comme sortie

Dans loop :
- On met la tension à un niveau bas quand la sortie LED_BUILTIN est à un niveau haut
- On met la tension à un niveau haut quand la sortie LED_BUILTIN est à un niveau bas

## 1.2 Utilisation d'une entrée numérique

## 1.3 Utilisation d'une entrée analogique

# 2. Utilisation du Joystick

# 3. Utilisation d'un capteur à ultrasons

# 4. Afficheur LCD par bus I2C

## 4.1 Affichage d'une lettre

## 4.2 noDisplay et display

## 4.3 Utilisations générales de l'afficheur

# 5. Application finale
