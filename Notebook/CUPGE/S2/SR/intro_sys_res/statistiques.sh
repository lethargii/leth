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
NB=$(find -mindepth 1 -type d | wc -l)
echo "    - $NB répertoire(s)"

# Niveau 2 : détails sur les répertoires
if [ $1 ] && [ $1 -ge 2 ] ; then
	NB=$(find -mindepth 1 -type d -empty | wc -l)
	echo "        - $NB répertoires vide(s)"
	NB=$(find -mindepth 1 -type d -name ".*" | wc -l)
	echo "        - $NB répertoires caché(s)"
fi

# Afficher le nombre de fichiers
NB=$(find -mindepth 1 -type f | wc -l)
if [ $1 ] && [ $1 -ge 2 ] ; then
	echo "    - $NB fichier(s) dont"
else
	echo "    - $NB fichier(s)"
fi
# Niveau 2 : détails sur les fichiers
if [ $1 ] && [ $1 -ge 2 ] ; then
	NB=$(find -mindepth 1 -type f -empty | wc -l)
	echo "        - $NB fichier(s) vide(s)"
	NB=$(find -mindepth 1 -type f -name ".*" | wc -l)
	echo "        - $NB fichier(s) caché(s)"
fi
# Niveau 3 : détails sur les fichiers
if [ $1 ] && [ $1 -ge 3 ] ; then
	NB=$(find -mindepth 1 -size -512k | wc -l)
	echo "        - $NB fichier(s) de moins de 512 kio"
	NB=$(find -mindepth 1 -size +15M | wc -l)
	echo "        - $NB fichier(s) de plus de 15 Mio"
	NB=$(find -mindepth 1 -type f -printf "%s\t%p\n" | sort -n | tail -n 1 | cut -f2)
	echo -e "        - le plus gros fichier est \n             $(pwd)${NB:1}"
fi
# Niveau 3 : détails sur le nombre de fichiers d'un certain type
if [ $1 ] && [ $1 -ge 3 ] ; then
	echo "       Il y a :"
	NB=$(find -mindepth 1 -type f -exec file {} \; | grep -c "Python script")
	echo "          - $NB fichier(s) Python"
	NB=$(find -mindepth 1 -type f -exec file {} \; | grep -c "image")
	echo "          - $NB fichier(s) image"
	NB=$(find -mindepth 1 -type f -exec file {} \; | grep -c "video")
	echo "          - $NB fichier(s) video"
fi

# Afficher la taille totale du répertoire
echo "    - taille totale : $(du -sh | cut -f1)"

}
