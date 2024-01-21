#!/bin/bash
#
# Implémentation de todo liste
TACHES=$HOME/.todo_list
function todo()
{
	# Afficher les commandes disponibles avec todo
	if [ ! $1 ] ; then
		echo "
		Implémentation de TODO liste en bash.
		Commandes todo
		todo list
		Afficher la liste des choses à faire.
		todo add [NUMERO] [NOM]
		Ajoute la tâche NOM à la ligne NUMERO.
		todo done [NUMERO]
		Enlève la tâche NUMERO."
		# Afficher les tâches à faire
	elif [[ $1 = list ]] ; then
		if [[ $2 ]] ; then
			echo Trop d\'arguments
		else
			nl -s ' - ' $TACHES
		fi
		# Ajouter une tâche
	elif [[ $1 = add ]] ; then
		if [[ ! $2 = +([0-9]) ]] ; then
			echo Un nombre est attendu.
			exit 1
		fi
		if [[ $2 -gt $[$(wc -l < $TACHES) + 1] ]] ; then
			echo Nombre trop grand.
			exit 1
		fi
		echo La tâche \"${@:3}\" a été ajoutée en position $2.
		head -n $[$2-1] $TACHES > TEMP
		echo ${@:3} >> TEMP
		tail $TACHES -n $[$(wc -l < $TACHES)-$2+1] >> TEMP
		cat TEMP > $TACHES
		rm TEMP
		# Retirer une tâche
	elif [[ $1 = done ]] ; then
		if [[ ! $2 = +([0-9]) ]] ; then
			echo Un nombre est attendu.
			exit 1
		fi
		if [[ $2 -gt $(wc -l < $TACHES) ]] ; then
			echo Nombre trop grand.
			exit 1
		fi
		echo La tâche $2 \($(head -n $2 $TACHES | tail -n 1)\) est faite !
		head -n $[$2-1] $TACHES > TEMP
		tail $TACHES -n $[$(wc -l < $TACHES)-$2] >> TEMP
		cat TEMP > $TACHES
		rm TEMP
	else
		echo $1 n\'est pas une commande TODO. Voir todo.
		exit 1
	fi
}
