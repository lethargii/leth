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
echo "    - $(find -mindepth 1 -type d | wc -l) répertoire(s)"

# Niveau 2 : détails sur les répertoires
if [ $1 ] && [ $1 -ge 2 ] ; then
	echo "        - $(find -mindepth 1 -type d -empty | wc -l) répertoire(s) vide(s)"
	echo "        - $(find -mindepth 1 -type d -name ".*" | wc -l) répertoire(s) caché(s)"
fi

# Afficher le nombre de fichiers
echo -n "    - $(find -mindepth 1 -type f | wc -l) fichier(s)"
if [ $1 ] && [ $1 -ge 2 ] ; then
	echo " dont"
else
	echo
fi
# Niveau 2 : détails sur les fichiers
if [ $1 ] && [ $1 -ge 2 ] ; then
	echo "        - $(find -mindepth 1 -type f -empty | wc -l) fichier(s) vide(s)"
	echo "        - $(find -mindepth 1 -type f -name ".*" | wc -l) fichier(s) caché(s)"
fi
# Niveau 3 : détails sur les fichiers
if [ $1 ] && [ $1 -ge 3 ] ; then
	echo "        - $(find -type f -mindepth 1 -size -512k | wc -l) fichier(s) de moins de 512 kio"
	echo "        - $(find -type f -mindepth 1 -size +15M | wc -l) fichier(s) de plus de 15 Mio"
	echo -e "        - le plus gros fichier est :\n             $(pwd)$(find -mindepth 1 -type f -printf "%s\t%p\n" | sort -n | tail -n 1 | cut -f2 | cut -c2-)"
fi
# Niveau 3 : détails sur le nombre de fichiers d'un certain type
if [ $1 ] && [ $1 -ge 3 ] ; then
	echo "       Il y a :"
	echo "          - $(find -name *.py | wc -l) fichier(s) Python"
	echo "          - $(find -name *.jpg -or -name *.png | wc -l) fichier(s) image"
	echo "          - $(find -name *.avi -or -name *.mp4 -or -name *.mkv | wc -l) fichier(s) vidéo"
fi

# Afficher la taille totale du répertoire
echo "    - taille totale : $(du -sh | cut -f1)"

}
