#!/bin/bash
sudo apt update
Install=''
Uninstall=''
for app in $(cat mint-apps); do
	if [ "$app" = "[Install]" ]; then
		category="[Install]"
	elif [ "$app" = "[Uninstall]" ]; then
		category="[Uninstall]"
	else
		if [ $category = "[Install]" ]; then
			Install="$Install $app"
		elif [ $category = "[Uninstall]" ]; then
			Uninstall="$Uninstall $app"'*'
		fi
	fi
done
sudo apt install -qq $Install
sudo apt remove -qq --purge $Uninstall
sudo apt autoremove -qq
sudo apt upgrade -qq
bash flatpak.sh
git config --global user.email "l.sevault@hotmail.com"
git config --global user.name "lethargii"
cp config.fish /home/lethargii/.config/fish/config.fish
pip install --user numpy matplotlib
wget https://invent.kde.org/plasma/plasma-workspace-wallpapers/-/raw/master/Altai/contents/images/5120x2880.png
sudo mv 5120x2880.png /usr/share/backgrounds/linuxmint/Altai.png
