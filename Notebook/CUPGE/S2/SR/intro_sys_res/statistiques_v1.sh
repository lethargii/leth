#!/bin/bash
#
# Script analysant le répertoire et ses sous-répertoires et affiche des statistiques.
function statistiques(){
# Si l'utilisateur rentre un argument incorrect, expliquer le fonctionnement de statistiques.sh
if ( [ $1 ] && ( [[ ! $1 =~ ^[0-9]+$ ]] || [ $1 -lt 1 ] || [ $1 -gt 3 ] ) ) || [ $# -gt 1 ] ; then
	echo -e "statistiques.sh s'exécute avec ou sans un argument :\n    statistiques.sh precision_statistiques\noù \"precision_satistiques\" est le chiffre (1, 2 ou 3)indiquant la précision des statistiques données"
	exit 1
fi

echo Analyse de $(pwd) :

# Afficher le nombre de répertoires
NB=$(find -type d | wc -l)
if [ $NB -lt 2 ] ; then
	echo "    - $NB répertoire"
else
	echo "    - $NB répertoires"
fi

# Niveau 2 : détails sur les répertoires
if [ $1 ] && [ $1 -ge 2 ] ; then
	NB=$(find -mindepth 1 -type d -name ".*" | wc -l)
	if [ $NB -lt 2 ] ; then
		echo "    - $NB répertoire caché"
	else
		echo "    - $NB répertoires cachés"
	fi
	NB=$(find -type d -empty | wc -l)
	if [ $NB -lt 2 ] ; then
		echo "    - $NB répertoire vide"
	else
		echo "    - $NB répertoires vides"
	fi
fi

# Afficher le nombre de fichiers
NB=$(find -type f | wc -l)
if [ $NB -lt 2 ] ; then
	echo "    - $NB fichier"
else
	echo "    - $NB fichiers"
fi
# Niveau 2 : détails sur les fichiers
if [ $1 ] && [ $1 -ge 2 ] ; then
	NB=$(find -type f -name ".*" | wc -l)
	if [ $NB -lt 2 ] ; then
		echo "    - $NB fichier caché"
	else
		echo "    - $NB fichiers cachés"
	fi
	NB=$(find -type f -empty | wc -l)
	if [ $NB -lt 2 ] ; then
		echo "    - $NB fichier vide"
	else
		echo "    - $NB fichiers vides"
	fi
fi
# Niveau 3 : détails sur les fichiers
if [ $1 ] && [ $1 -ge 3 ] ; then
	NB=$(find -size -512k | wc -l)
	if [ $NB -lt 2 ] ; then
		echo "    - $NB fichier de moins de 512kio"
	else
		echo "    - $NB fichiers de moins de 512kio"
	fi
	NB=$(find -size +15M | wc -l)
	if [ $NB -lt 2 ] ; then
		echo "    - $NB fichier de plus de 15Mio"
	else
		echo "    - $NB fichiers de plus de 15Mio"
	fi
	NB=$(find -type f -printf "%s\t%p\n" | sort -n | tail -n 1 | cut -f2)
	echo -e "    - le plus gros fichier est \n$(pwd)${NB:1}"
fi
# Niveau 3 : détails sur le nombre de fichiers d'un certain type
if [ $1 ] && [ $1 -ge 3 ] ; then
	echo "	Il y a :"
	NB=$(find -type f -exec file {} \; | grep "Python script" | wc -l)
	if [ $NB -lt 2 ] ; then
		echo "    - $NB fichier Python"
	else
		echo "    - $NB fichiers Python"
	fi
	NB=$(find -type f -exec file {} \; | grep "image" | wc -l)
	if [ $NB -lt 2 ] ; then
		echo "    - $NB fichier image"
	else
		echo "    - $NB fichiers image"
	fi
	NB=$(find -type f -exec file {} \; | grep "video" | wc -l)
	if [ $NB -lt 2 ] ; then
		echo "    - $NB fichier video"
	else
		echo "    - $NB fichiers video"
	fi
fi

# Afficher la taille totale du répertoire
echo "    - taille totale : $(du -sh | cut -f1)"

unset NB
}
