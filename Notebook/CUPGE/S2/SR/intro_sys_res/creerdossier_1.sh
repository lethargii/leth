#!/bin/bash
#
# Script permettant de créer un dossier
if [ $1 ] && [ ! $2 ] ; then
	if [ ! -d $1 ] ; then
		mkdir $1
	fi
else
	echo Un seul et unique argument doit être donné
	exit 1
fi
