#!/bin/bash
#
# Jeu du pendu en bash

# Si aucun nom de fichier n'est donné, renvoyer une erreur et arrêter le script
if [ ! $1 ] ; then
	echo -e "pendu.sh s'exécute avec un argument :\n    pendu.sh nom_fichier\noù \"nom_fichier\" est le dictionnaire pour le choix des mots"
	exit 1
fi
# Si le nom de fichier donné n'est pas celui d'un fichier existant, renvoyer une erreur et arrêter le script
if [ ! -f $1 ] ; then
	echo \"$1\" n\'est pas un nom de fichier existant
	exit 1
fi

# Définir la variable DICT avec le nom du dictionnaire utilisé et établir le nombre de tentative restantes à 10
DICT=$1
NB_TENTATIVES=10
function choisi_mot(){
	MOT_A_TROUVER=$(head $DICT -n $[$RANDOM % $(wc -m < $DICT) + 1] | tail -n 1)
	MOT_DEVINE=$(echo $MOT_A_TROUVER | tr [:alpha:] _ )
}
# Fonction testant si la lettre donnée par l'utilisateur est contenue dans le mot et modifier MOT_DEVINE et NB_TENTATIVES
function test_lettre(){
	LETTRES_TESTEES+=" $1"
	LETTRES_RESTANTES=$(echo $LETTRES_RESTANTES | tr -d $(echo $LETTRE))
	# Si la lettre est dans le mot, l'afficher dans MOT_DEVINE
	if [[ $MOT_A_TROUVER =~ $1 ]] ; then
		MOT_DEVINE=$(echo $MOT_A_TROUVER | tr $(echo $LETTRES_RESTANTES) _ )
	# Si la lettre n'est pas dans le mot, réduire NB_TENTATIVES de 1
	else
		NB_TENTATIVES=$[$NB_TENTATIVES-1]
	fi
}
# Fonction affichant le pendu en fonction du nombre de tentatives restantes
function affiche_pendu(){
	if [ $NB_TENTATIVES = 10 ] ; then
		echo -e "******************************\n\n\n\n\n\n\n\n"
	fi
	if [ $NB_TENTATIVES = 9 ] ; then
		echo -e "******************************\n\n\n\n\n\n\n___ ___\n"
	fi
	if [ $NB_TENTATIVES = 8 ] ; then
		echo -e "******************************\n\n\n   |\n   |\n   |\n   |\n___|___\n"
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
# Fonction principale du jeu du pendu
function jeu_pendu(){
	# Initialiser la variable LETTRES_TESTEES à une chaine de caractères vide et la variable LETTRES_RESTANTES à l'alphabet et choisir le mot
	LETTRES_TESTEES=""
	LETTRES_RESTANTES=ABCDEFGHIJKLMNOPQRSTUVWXYZ
	choisi_mot
	# Tant qu'il reste des tentatives afficher le pendu et demander une lettre à l'utilisateur
	while [ $NB_TENTATIVES -gt 0 ] ; do
		affiche_pendu
		echo "Lettres testées : " $LETTRES_TESTEES
		echo -e "\n$MOT_DEVINE\n"
		echo "Choisissez une lettre : "
		read LETTRE
		# Tant que la lettre rentrée est non correcte la redemander à l'utilisateur
		while ! [[ $LETTRES_RESTANTES =~ $LETTRE ]] || [[ ! $LETTRE ]] || [[ ! $(echo -n $LETTRE | wc -c) -eq 1 ]] ; do
			echo Lettre choisie incorrecte \(ou déjà testée\) \!
			echo -e "\n$MOT_DEVINE\n"
			echo "Choisissez une lettre : "
			read LETTRE
		done
		# Tester la lettre
		test_lettre $LETTRE
		# Si le joueur a trouvé le mot, afficher un message de victoire
		if [ $MOT_A_TROUVER = $MOT_DEVINE ] ; then
			echo GAGNE !!
			return 1
		fi
	done
	# Afficher le pendu et un message de défaite
	affiche_pendu
	echo -e "PERDU :""(""\nLe mot à trouver était : $MOT_A_TROUVER"
}
jeu_pendu
