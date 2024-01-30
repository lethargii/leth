#!/bin/bash
#
# Script permettant de gérer des comptes étudiants.
cat $1 | while read LIGNE ; do
PSEUDO=$(echo $LIGNE | cut -d ";" -f 2 | cut -c 1,2 | tr -c -d [:alpha:])$(echo $LIGNE | cut -d ";" -f 1 | tr -c -d [:alpha:])
mkdir $PSEUDO $PSEUDO/Documents $PSEUDO/Images
VOYELLES=$(head /dev/urandom | tr -cd aeiouy | cut -c1,2)
CONSONNES=$(head /dev/urandom | tr -cd [:alpha:] | tr -d aeiouy | tr -d [:upper:] | cut -c1,2)
LETTRES=$(echo $CONSONNES$VOYELLES | cut -c1,3)$(echo $CONSONNES$VOYELLES | cut -c2,4)
CHIFFRES=$(head /dev/urandom | tr -cd [:digit:] | cut -c1,2,3,4)
MDP=$LETTRES$CHIFFRES
echo $MDP > $PSEUDO/mot_de_passe.txt
done
