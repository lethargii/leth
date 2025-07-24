#!/bin/bash
declare -A Install
declare -A Uninstall
echo Searching for what needs to be done...
for app in $(cat apps); do
	if [ "$app" = "[Fedora]" ]; then
		distro="Fedora"
	elif [ "$app" = "[Mint]" ]; then
		distro="Mint"
	elif [ "$app" = "[Install]" ]; then
		category="[Install]"
	elif [ "$app" = "[Uninstall]" ]; then
		category="[Uninstall]"
	else
		if [ $category = "[Install]" ]; then
			Install[$distro]="${Install[$distro]} $app"
		elif [ $category = "[Uninstall]" ]; then
			Uninstall[$distro]="${Uninstall[$distro]} $app"'*'
		fi
	fi
done
if [ -e /bin/dnf ]; then
	echo Installing the required packages...
	sudo dnf install -qy ${Install[Fedora]}
	echo Removing the unwanted packages...
	sudo dnf remove -qy ${Uninstall[Fedora]}
	echo Removing the packages that are not needed anymore...
	sudo dnf autoremove -qy
	echo Updating the packages...
	sudo dnf update -qy
fi
if [ -e /bin/apt ]; then
	sudo apt update
	echo Installing the required packages...
	sudo apt install -qq ${Install[Mint]}
	echo Removing the unwanted packages...
	sudo apt remove -qq --purge ${Uninstall[Mint]}
	echo Removing the packages that are not needed anymore...
	sudo apt autoremove -qq
	echo Updating the packages...
	sudo apt upgrade -qq
fi
bash flatpak.sh
mkdir $HOME/.config/fish
cp config.fish $HOME/.config/fish/config.fish
pip install --user numpy matplotlib
wget https://invent.kde.org/plasma/plasma-workspace-wallpapers/-/raw/master/Altai/contents/images/5120x2880.png
sudo mv 5120x2880.png /usr/share/backgrounds/Altai.png
gsettings set org.cinnamon.desktop.background picture-uri file:///usr/share/backgrounds/Altai.png
if [ ! -d /usr/share/icons/Bibata-Modern-Classic ]; then
	echo Installing Bibata Modern Classic cursor theme...
	wget https://github.com/ful1e5/Bibata_Cursor/releases/latest/download/Bibata-Modern-Classic.tar.xz
	tar -xvf Bibata-Modern-Classic.tar.xz
	sudo mv Bibata-Modern-Classic/ /usr/share/icons/
	rm Bibata-Modern-Classic.tar.xz
fi
if [ -d /boot/grub2 & ! -e /usr/share/grub/themes/tela/theme.txt ]; then
	git clone https://github.com/vinceliuice/grub2-themes.git
	sudo grub2-themes/install.sh -t tela
	rm -rf grub2-themes/
fi
