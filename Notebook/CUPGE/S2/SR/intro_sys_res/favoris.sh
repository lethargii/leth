#!/bin/bash
FAV=$HOME/.favoris_bash
TMP=/tmp/favoris.tmp
if [ ! -e $FAV ]; then
	touch $FAV
fi
function S(){
	grep $1 >> $TMP
}
function C(){
	cd $1
}
function R(){
	grep -v $1 > $TMP
	echo $TMP > $FAV
}
function L(){
	cat $FAV
}
