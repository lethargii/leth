#!/bin/bash
#
# Jeu du pendu en bash

DICT=$1
NB_TENTATIVES=10
function choisi_mot(){
	MOT_A_TROUVER=$(head $DICT -n $[$RANDOM % $(wc -m < $DICT) + 1] | tail -n 1)
	MOT_DEVINE=$(echo $MOT_A_TROUVER | tr [:alpha:] _ )
}
function test_lettre(){
	LETTRES_TESTEES+=($1)
	LETTRES_RESTANTES=$(echo $LETTRES_RESTANTES | tr -d $(echo $LETTRE))
	if [[ $MOT_A_TROUVER =~ $1 ]] ; then
		MOT_DEVINE=$(echo $MOT_A_TROUVER | tr $(echo $LETTRES_RESTANTES) _ )
	else
		NB_TENTATIVES=$[$NB_TENTATIVES-1]
	fi
}
function affiche_pendu(){
	if [ $NB_TENTATIVES = 10 ] ; then
		echo -e "******************************\n\n\n\n\n\n\n\n"
	fi
	if [ $NB_TENTATIVES = 9 ] ; then
		echo -e "******************************\n\n\n\n\n\n\n___ ___\n"
	fi
	if [ $NB_TENTATIVES = 8 ] ; then
		echo -e "******************************\n\n   \n   |\n   |\n   |\n   |\n___|___\n"
	fi
	if [ $NB_TENTATIVES = 7 ] ; then
		echo -e "******************************\n\n    _____\n   |\n   |\n   |\n   |\n___|___\n"
	fi
	if [ $NB_TENTATIVES = 6 ] ; then
		echo -e "******************************\n\n    _____\n   |     |\n   |\n   |\n   |\n___|___\n"
	fi
	if [ $NB_TENTATIVES = 5 ] ; then
		echo -e "******************************\n\n    _____\n   |     |\n   |     O\n   |\n   |\n___|___\n"
	fi
	if [ $NB_TENTATIVES = 4 ] ; then
		echo -e "******************************\n\n    _____\n   |     |\n   |     O\n   |     |\n   |\n___|___\n"
	fi
	if [ $NB_TENTATIVES = 3 ] ; then
		echo -e "******************************\n\n    _____\n   |     |\n   |     O\n   |    /|\n   |\n___|___\n"
	fi
	if [ $NB_TENTATIVES = 2 ] ; then
		echo -e "******************************\n\n    _____\n   |     |\n   |     O\n   |    /|"'\\'"\n   |\n___|___\n"
	fi
	if [ $NB_TENTATIVES = 1 ] ; then
		echo -e "******************************\n\n    _____\n   |     |\n   |     O\n   |    /|"'\\'"\n   |    /\n___|___\n"
	fi
	if [ $NB_TENTATIVES = 0 ] ; then
		echo -e "******************************\n\n    _____\n   |     |\n   |     O\n   |    /|"'\\'"\n   |    / "'\\'"\n___|___\n"
	fi
}
function jeu_pendu(){
	LETTRES_TESTEES=()
	LETTRES_RESTANTES=ABCDEFGHIJKLMNOPQRSTUVWXYZ
	choisi_mot
	while [ $NB_TENTATIVES -gt 0 ] ; do
		affiche_pendu
		echo Lettres testées : ${LETTRES_TESTEES[@]}
		echo -e "\n$MOT_DEVINE\n"
		echo "Choisissez une lettre : "
		read LETTRE
		while ! [[ $LETTRES_RESTANTES =~ $LETTRE ]] || [[ ! $LETTRE ]] ; do
			echo Lettre choisie incorrecte.
			affiche_pendu
			echo Lettres testées : 
			echo ${LETTRES_TESTEES[@]}
			echo -e "\n$MOT_DEVINE\n"
			echo Choisissez une lettre : 
			read LETTRE
		done
		test_lettre $LETTRE
		if [ $MOT_A_TROUVER = $MOT_DEVINE ] ; then
			echo GAGNÉ :\)
			return 1
		fi
	done
	affiche_pendu
	echo PERDU :\(
}
jeu_pendu
