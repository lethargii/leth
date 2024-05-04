#!/bin/bash
flatpak remote-add --user --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
for app in $(flatpak list --columns=application --app); do
	if ! $(grep -Fxq "$app" flatpak-apps); then
		flatpak uninstall --user --noninteractive $app
	fi
done
for app in $(cat flatpak-apps); do
	if [ $app = "[Apps]" ]; then
		category="[Apps]"
	elif [ $app = "[GTK3]" ]; then
		category="[GTK3]"
	elif [ $app = "[GTK4]" ]; then
		category="[GTK4]"
	else
		if [ $category="[Apps]" ]; then
			flatpak install --user --noninteractive $app
		elif [ $category="[GTK3]" ]; then
			flatpak override --user --env=GTK_THEME=Adwaita:dark $app
		elif [ $category="[GTK4]" ]; then
			flatpak override --user --env=GTK_THEME=Adwaita-dark $app
		fi
	fi
done
flatpak override --user --env=QT_STYLE_OVERRIDE=kvantum
flatpak override --user --env=PRUSA_SLICER_DARK_THEME=true
flatpak update --user --noninteractive
