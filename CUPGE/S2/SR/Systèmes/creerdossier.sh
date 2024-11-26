#!/bin/bash
#
# Script permettant de créer un dossier
if [ ! $# -eq 1 ] ; then
	echo Un seul et unique argument doit être donné
	exit 1
fi
if [ ! -d $1 ] ; then
	mkdir $1
fi
