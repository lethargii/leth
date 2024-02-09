#!/bin/bash
#
# Script permettant de gérer des comptes étudiants.

# Vérifier que le fichier existe
if [ ! -f $1 ] ; then
	echo $1 n\'est pas un nom de fichier existant
	exit 1
fi
# Vérifier que le dossier existe
if [ ! -d $2 ] ; then
	echo $2 n\'est pas un nom de dossier existant
	exit 1
fi
# Si aucun argument n'est donné, expliquer le fonctionnnement de admin_etudiants
if [ $# -eq 0 ] ; then
	echo admin_etudiants.sh s\'utilise avec \"admin_etudiants.sh liste_nom_etudiants dossier_parent\"
	exit 0
fi
# Créer les dossiers des étudiants et leur mot de passe
cat $1 | while read LIGNE ; do
	PSEUDO=$(echo $LIGNE | cut -d ";" -f 2 | cut -c 1,2 | tr -c -d [:alpha:])$(echo $LIGNE | cut -d ";" -f 1 | tr -c -d [:alpha:] | head -c 7)
	mkdir $2/$PSEUDO $2/$PSEUDO/Documents $2/$PSEUDO/Images
	VOYELLES=$(head /dev/urandom | tr -cd aeiouy | cut -c1,2)
	CONSONNES=$(head /dev/urandom | tr -cd [:alpha:] | tr -d aeiouy | tr -d [:upper:] | cut -c1,2)
	LETTRES=$(echo $CONSONNES$VOYELLES | cut -c1,3)$(echo $CONSONNES$VOYELLES | cut -c2,4)
	CHIFFRES=$(head /dev/urandom | tr -cd [:digit:] | cut -c1,2,3,4)
	MDP=$LETTRES$CHIFFRES
	echo $MDP > $2/$PSEUDO/mot_de_passe.txt
done
