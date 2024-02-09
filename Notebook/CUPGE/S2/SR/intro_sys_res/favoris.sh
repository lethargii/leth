#!/bin/bash
FAV=$HOME/.favoris_bash
TMP=/tmp/favoris.tmp
if [ ! -e $FAV ]; then
	touch $FAV
fi
# Sauvegarder un favoris
function S(){
	echo Le répertoire $(pwd) est sauvegardé dans vos favoris.
	echo "	-> raccourci : ${@:1}"
	echo "${@:1}− >$(pwd)" >> $FAV
}
# Se déplacer dans un répertoire enregistré dans les favoris
function C(){
	CHEMIN=""
	if [ $(cat $FAV | grep ^"$(echo ${@:1})" | wc -l) -eq 1 ] && [ "$(cat $FAV | grep ^"$(echo ${@:1})")" ]; then
		CHEMIN="$(cat $FAV | grep ^"$(echo ${@:1})" |  awk -F'− >' '{print $2}')"
	fi
	if [ $(cat $FAV | grep ^"$(echo ${@:1})"'− >' | wc -l) -eq 1 ] && [ "$(cat $FAV | grep ^"$(echo ${@:1})"'− >')" ]; then
		CHEMIN="$(cat $FAV | grep ^"$(echo ${@:1})"'− >' | awk -F'− >' '{print $2}')"
	fi
	if [ -z "$CHEMIN" ] ; then
		echo Le favoris \"${@:1}\" n\'existe pas.
		return 1
	fi
	echo Vous êtes maintenant dans le répertoire
	echo $CHEMIN
	cd $CHEMIN
}
# Supprimer un favoris de la liste
function R(){
	cat $FAV | grep -v ^"$(echo ${@:1})" > $TMP
	cat $TMP > $FAV
	echo Le favoris \"${@:1}\" est supprimé de votre liste.
}
# Lister tous les favoris
function L(){
	if [ $1 ] ; then
		cat $FAV | grep "$(echo ${@:1})"
	else
		cat $FAV
	fi
}
