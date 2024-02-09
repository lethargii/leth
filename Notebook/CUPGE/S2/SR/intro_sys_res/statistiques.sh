#!/bin/bash
#
# Script analysant le répertoire et ses sous-répertoires et affiche des statistiques.

# Si l'utilisateur rentre un argument incorrect, expliquer le fonctionnement de statistiques.sh
if ( [ $1 ] && ( [[ ! $1 =~ ^[0-9]+$ ]] || [ $1 -lt 1 ] || [ $1 -gt 3 ] ) ) || [ $# -gt 1 ] ; then
	echo -e "statistiques.sh s'exécute avec ou sans un argument :\n    statistiques.sh precision_statistiques\noù \"precision_satistiques\" est le chiffre (1, 2 ou 3)indiquant la précision des statistiques données"
	exit 1
fi

echo Analyse de $(pwd) :

# Afficher le nombre de répertoires
echo "	- $(find -type d | wc -l) répertoires"
# Niveau 2 : détails sur les répertoires
if [ $1 ] && [ $1 -ge 2 ] ; then
	echo "		- $(find -type d -name ".*" | wc -l) répertoire caché"
	echo "		- $(echo) répertoire vide"
fi

# Afficher le nombre de fichiers
echo "	- $(find -type f | wc -l) fichiers"
# Niveau 2 : détails sur les fichiers
if [ $1 ] && [ $1 -ge 2 ] ; then
	echo "		- $(find -type f -name ".*" | wc -l) fichier caché"
	echo "		- $(echo) fichier vide"
fi
# Niveau 3 : détails sur les fichiers
if [ $1 ] && [ $1 -ge 3 ] ; then
	echo "		- $(find -size -512k | wc -l) fichier de moins de 512kio"
	echo "		- $(find -size +15M | wc -l) fichier de plus de 15Mio"
	echo "		- le plus gros fichier est $(echo)"
fi
# Niveau 3 : détails sur le nombre de fichiers d'un certain type
if [ $1 ] && [ $1 -ge 3 ] ; then
	echo "	Il y a :"
	echo "		- $(echo) fichier Python"
	echo "		- $(echo) fichier image"
	echo "		- $(echo) fichier vidéo"
fi

# Afficher la taille totale du répertoire
echo "	- taille totale : $(du -sh)"
