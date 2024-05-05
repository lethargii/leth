#!/bin/bash
sudo apt update
for app in $(cat mint-apps); do
	if [ "$app" = "[Install]" ]; then
		category="[Install]"
	elif [ "$app" = "[Uninstall]" ]; then
		category="[Uninstall]"
	else
		if [ $category = "[Install]" ]; then
			echo $app
			sudo apt install $app
		elif [ $category = "[Uninstall]" ]; then
			echo $app
			sudo apt remove --purge "$app*"
		fi
	fi
done
sudo apt autoremove
sudo apt upgrade
bash flatpak.sh
git config --global user.email "l.sevault@hotmail.com"
git config --global user.name "lethargii"
cp config.fish /home/lethargii/.config/fish/config.fish
