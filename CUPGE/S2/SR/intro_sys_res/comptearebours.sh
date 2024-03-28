#!/bin/bash
#
# Compte à rebours de 10 à 0
COMPTEUR=10
while [ $COMPTEUR -ge 0 ] ; do
	echo $COMPTEUR
	COMPTEUR=$[$COMPTEUR-1]
done
