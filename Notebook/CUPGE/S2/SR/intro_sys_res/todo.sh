#!/bin/bash
#
# Implémentation de todo liste
TACHES=$HOME/.todo_list
TMP=/tmp/todo_list.tmp
function todo()
{
	if [ ! -e $TACHES ] ; then
		touch $HOME/.todo_list
	fi
	# Afficher les tâches à faire
	if [[ $1 = list ]] ; then
		if [[ $2 ]] ; then
			echo Trop d\'arguments
			return 1
		fi
		nl -w 1 -s ' - ' $TACHES
		return 0
		# Ajouter une tâche
	elif [[ $1 = add ]] ; then
		if [[ ! $2 = +([0-9]) ]] ; then
			echo "La commande 'todo add' s'exécute avec 'todo add numero_tache action_a_ajouter'"
			return 1
		fi
		if [[ $2 -gt $[$(wc -l < $TACHES) + 1] ]] || [[ $2 -le 0 ]] ; then
			echo Nombre trop petit ou trop grand.
			return 1
		fi
		echo La tâche \"${@:3}\" a été ajoutée en position $2.
		head -n $[$2-1] $TACHES > $TMP
		echo ${@:3} >> $TMP
		#tail $TACHES -n $[$(wc -l < $TACHES)-$2+1] >> $TMP
		tail $TACHES -n +$2 >> $TMP
		cat $TMP > $TACHES
		return 0
		# Retirer une tâche
	elif [[ $1 = done ]] ; then
		if [[ ! $2 = +([0-9]) ]] ; then
			echo "La commande 'todo done' s'exécute avec 'todo done numero_tache'"
			return 1
		fi
		if [[ $2 -gt $(wc -l < $TACHES) ]] || [[ $2 -le 0 ]] ; then
			echo Nombre trop petit ou trop grand.
			return 1
		fi
		echo La tâche $2 \($(head -n $2 $TACHES | tail -n 1)\) est faite !
		head -n $[$2-1] $TACHES > $TMP
		#tail $TACHES -n $[$(wc -l < $TACHES)-$2] >> $TMP
		tail $TACHES -n +$[$2+1] >> $TMP
		cat $TMP > $TACHES
		return 0
		# Afficher les commandes disponibles avec todo
	else
		echo "La commande 'todo' s'exécute avec 'todo (add | done | list) (arguments)'"
		return 0
	fi
}
