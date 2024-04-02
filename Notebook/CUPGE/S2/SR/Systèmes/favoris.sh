#!/bin/bash

# Définir les variables FAV et TMP
FAV=$HOME/.favoris_bash
TMP=/tmp/favoris.tmp
# Si la liste des favoris n'existe pas, la créer
if [ ! -e $FAV ]; then
	touch $FAV
fi
# Sauvegarder un favoris
function S(){
	# Si aucun argument n'est donné explique le fonctionnement de la fonction puis arrêter le programme.
	if [ -z $1 ] ; then
		echo La commande \'S\' s\'exécute avec \'S nom_raccourci\'
		return 0
	fi
	# Si le raccourci existe déjà écrire un message et terminer le programme
	if [ ! $(grep -c ^"$(echo ${@:1})" $FAV) -eq 0 ] ; then
		echo Le raccourci \'$1\' existe déja :
		echo "  $(grep ^"$(echo ${@:1})" $FAV)"
		return 1
	fi
	# Sauvegarder le raccourci dans les favoris et afficher un message
	echo Le répertoire $(pwd) est sauvegardé dans vos favoris.
	echo "  -> raccourci : ${@:1}"
	echo "${@:1} -> $(pwd)" >> $FAV
}
# Se déplacer dans un répertoire enregistré dans les favoris
function C(){
	# Si aucun argument n'est donné explique le fonctionnement de la fonction puis arrêter le programme.
	if [ -z $1 ] ; then
		echo La commande \'C\' s\'exécute avec \'C nom_raccourci\'
		return 0
	fi
	# Initialiser la variable vide CHEMIN
	CHEMIN=""
	# Si il y a un raccourci exact trouvé, l'utiliser et modifier la variable CHEMIN
	if [ $(cat $FAV | grep ^"$(echo ${@:1})"' -> ' | wc -l) -eq 1 ] && [ "$(cat $FAV | grep ^"$(echo ${@:1})"' -> ')" ]; then
		CHEMIN="$(cat $FAV | grep ^"$(echo ${@:1})"' -> ' | cut -d'>' -f2)"
	# Si il n'y a qu'un seul raccourci trouvé, l'utiliser et modifier la variable CHEMIN
	elif [ $(cat $FAV | grep ^"$(echo ${@:1})" | wc -l) -eq 1 ] && [ "$(cat $FAV | grep ^"$(echo ${@:1})")" ]; then
		CHEMIN="$(cat $FAV | grep ^"$(echo ${@:1})" |  cut -d'>' -f2)"
	# Si aucun raccourci n'est trouvé renvoyer une erreur et arrêter le programme
	else
		echo Le raccourci \'${@:1}\' n\'existe pas.
		return 1
	fi
	# Si un raccourci est trouvé changer de répertoire
	cd $CHEMIN
}
# Supprimer un favoris de la liste
function R(){
	# Si aucun argument n'est donné explique le fonctionnement de la fonction puis arrêter le programme.
	if [ -z $1 ] ; then
		echo La commande \'R\' s\'exécute avec \'R nom_raccourci\'
		return 0
	fi
	# Si le raccourci n'existe pas renvoyer un message d'erreur et arrêter le programme.
	if [ $(grep -c ^$1 $FAV) -eq 0 ] ; then
		echo Le raccourci \'${@:1}\' n\'existe pas.
		return 0
	fi
	# Supprimer le raccourci de la liste et l'afficher
	echo Le favori \"${@:1}\" a été supprimé de votre liste.
	cat $FAV | grep -v ^"$(echo ${@:1})" > $TMP
	cat $TMP > $FAV
}
# Lister tous les favoris
function L(){
	# Si un argument est donné, rechercher les raccourcis correspondant
	if [ $1 ] ; then
		cat $FAV | grep "$(echo ${@:1})"
	# Autrement, afficher tous les raccourcis
	else
		cat $FAV
	fi
}
