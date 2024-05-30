#!/bin/bash
#
# Implémentation de todo liste
TACHES=$HOME/.todo_list
TMP=/tmp/todo_list.tmp
function todo()
{
	# Si le fichier todo list n'existe pas, le créer
	if [ ! -e $TACHES ] ; then
		touch $HOME/.todo_list
	fi
	# Afficher les tâches à faire
	if [[ $1 = list ]] ; then
		# Si il y a trop d'arguments, renvoyer une erreur
		if [[ $2 ]] ; then
			echo Trop d\'arguments
			return 1
		fi
		nl -w 1 -s ' - ' $TACHES
		return 0
	# Ajouter une tâche
	elif [[ $1 = add ]] ; then
		# Si le deuxième argument n'est pas un nombre, renvoyer une erreur
		if [[ ! $2 = +([0-9]) ]] ; then
			echo "La commande 'todo add' s'exécute avec 'todo add numero_tache action_a_ajouter'"
			return 1
		fi
		# Si le deuxième argument est inférieur à 1 ou supérieur au nombre de tâches dans la liste + 1, renvoyer une erreur
		if [[ $2 -gt $[$(wc -l < $TACHES) + 1] ]] || [[ $2 -le 0 ]] ; then
			echo Nombre trop petit ou trop grand.
			return 1
		fi
		echo La tâche \"${@:3}\" a été ajoutée en position $2.
		head -n $[$2-1] $TACHES > $TMP
		echo ${@:3} >> $TMP
		tail $TACHES -n +$2 >> $TMP
		cat $TMP > $TACHES
		return 0
	# Retirer une tâche
	elif [[ $1 = done ]] ; then
		# Si le deuxième argument n'est pas un nombre, renvoyer une erreur
		if [[ ! $2 = +([0-9]) ]] ; then
			echo "La commande 'todo done' s'exécute avec 'todo done numero_tache'"
			return 1
		fi
		# Si le deuxième argument est inférieur à 1 ou supérieur au nombre de tâches dans la liste, renvoyer une erreur
		if [[ $2 -gt $(wc -l < $TACHES) ]] || [[ $2 -le 0 ]] ; then
			echo Nombre trop petit ou trop grand.
			return 1
		fi
		echo La tâche $2 \($(head -n $2 $TACHES | tail -n 1)\) est faite !
		head -n $[$2-1] $TACHES > $TMP
		tail $TACHES -n +$[$2+1] >> $TMP
		cat $TMP > $TACHES
		return 0
	# Changer l'endroit où est stocké la todo_liste
	elif [[ $1 = load ]] ; then
		# Si le fichier n'existe pas, renvoyer une erreur.
		if [ ! -e $HOME/$2 ] ; then
			echo Il n\'existe aucun fichier $HOME/$2.
			return 1
		fi
		TACHES=$HOME/$2
		return 0
	# Si il n'y a pas de premier argument, expliquer comment fonctionne la commande todo
	else
		echo "La commande 'todo' s'exécute avec 'todo (add | done | list) (arguments)'"
		return 0
	fi
}
