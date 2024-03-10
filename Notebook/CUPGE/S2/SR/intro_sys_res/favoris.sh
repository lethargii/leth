#!/bin/bash
FAV=$HOME/.favoris_bash
TMP=/tmp/favoris.tmp
if [ ! -e $FAV ]; then
	touch $FAV
fi
# Sauvegarder un favoris
function S(){
	if [ -z $1 ] ; then
		echo La commande \'S\' s\'exécute avec \'S nom_raccourci\'
		return 0
	fi
	if [ $(cat $FAV | grep ^"$(echo ${@:1})") ] ; then
		echo Le raccourci \'$1\' existe déja :
		echo $(cat $FAV | grep ^"$(echo ${@:1})")
	fi
	echo Le répertoire $(pwd) est sauvegardé dans vos favoris.
	echo "-> raccourci : ${@:1}"
	echo "${@:1}− >$(pwd)" >> $FAV
}
# Se déplacer dans un répertoire enregistré dans les favoris
function C(){
	if [ -z $1 ] ; then
		echo La commande \'C\' s\'exécute avec \'C nom_raccourci\'
		return 0
	fi
	CHEMIN=""
	if [ $(cat $FAV | grep ^"$(echo ${@:1})" | wc -l) -eq 1 ] && [ "$(cat $FAV | grep ^"$(echo ${@:1})")" ]; then
		CHEMIN="$(cat $FAV | grep ^"$(echo ${@:1})" |  awk -F'− >' '{print $2}')"
	fi
	if [ $(cat $FAV | grep ^"$(echo ${@:1})"'− >' | wc -l) -eq 1 ] && [ "$(cat $FAV | grep ^"$(echo ${@:1})"'− >')" ]; then
		CHEMIN="$(cat $FAV | grep ^"$(echo ${@:1})"'− >' | awk -F'− >' '{print $2}')"
	fi
	if [ -z "$CHEMIN" ] ; then
		echo Le raccourci \'${@:1}\' n\'existe pas.
		return 1
	fi
	echo Vous êtes maintenant dans le répertoire
	echo $CHEMIN
	cd $CHEMIN
}
# Supprimer un favoris de la liste
function R(){
	if [ -z $1 ] ; then
		echo La commande \'R\' s\'exécute avec \'R nom_raccourci\'
		return 0
	else
		if [ $(grep -c ^$1 $FAV) -eq 0 ] ; then
			echo Le raccourci \'${@:0}\' n\'existe pas.
			return 0
		fi
		echo Le favori \"${@:1}\" a été supprimé de votre liste.
		cat $FAV | grep -v ^"$(echo ${@:1})" > $TMP
		cat $TMP > $FAV
	fi
}
# Lister tous les favoris
function L(){
	if [ $1 ] ; then
		cat $FAV | grep "$(echo ${@:1})"
	else
		cat $FAV
	fi
}
