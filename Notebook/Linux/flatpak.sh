#!/bin/bash
flatpak remote-add --user --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
Uninstall=''
for app in $(flatpak list --columns=application --app); do
	if ! $(grep -Fxq "$app" flatpak-apps); then
		Uninstall="$Uninstall $app"
	fi
done
if ! [ $Uninstall='' ]; then
	flatpak uninstall --user --noninteractive $Uninstall
fi
Apps=''
GTK3=''
GTK4=''
for app in $(cat flatpak-apps); do
	if [ $app = "[Apps]" ]; then
		category="[Apps]"
	elif [ $app = "[GTK3]" ]; then
		category="[GTK3]"
	elif [ $app = "[GTK4]" ]; then
		category="[GTK4]"
	else
		if [ $category = "[Apps]" ]; then
			Apps="$Apps $app"
		elif [ $category = "[GTK3]" ]; then
			GTK3="$GTK3 $app"
		elif [ $category = "[GTK4]" ]; then
			GTK4="$GTK4 $app"
		fi
	fi
done
flatpak install --user --noninteractive $Apps
if ! [ "$GTK3"="" ]; then
	flatpak override --user --env=GTK_THEME=Adwaita:dark $GTK3
fi
if ! [ "$GTK4"="" ]; then
	flatpak override --user --env=GTK_THEME=Adwaita-dark $GTK4
fi
flatpak override --user --env=QT_STYLE_OVERRIDE=kvantum
flatpak override --user --env=PRUSA_SLICER_DARK_THEME=true
flatpak update --user --noninteractive
