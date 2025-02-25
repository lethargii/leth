#!/bin/bash
#
function affiche_entre(){
	if [ ! $# -eq 3 ] ; then
		echo Cette fonction prend 3 arguments.
		return 1
	fi
	if [ ! -e $1 ] || [ ! -f $1 ] ; then
		echo $1 n\'est pas un fichier ou n\'existe pas.
		return 2
	fi
	head $1 -n $3 | tail -n $[$3-$2+1]
	return 0
}
