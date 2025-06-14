#!/bin/sh
# All packages
sudo xbps-install -Syu nvidia gnome-core fish-shell neovim epiphany dejavu-fonts-ttf xorg-fonts noto-fonts-ttf noto-fonts-cjk noto-fonts-emoji nerd-fonts pipewire alsa-pipewire wireplumber-elogind libspa-bluetooth flatpak bluez git steam gnome-software gnome-tweaks glibc-32bit mesa-32bit geary firefox xdg-user-dirs snapshot baobab gnome-disk-utility plymouth sway gamescope qt6-widgets qt6-plugin-tls-openssl fbv sassc ibus-mozc python3-venv
# Enabling services -- a completer
# Fish config
mkdir -p ~/.config/fish/
cp config.fish ~/.config/fish/
# Neovim config -- a completer
# Theming
## Grub2
git clone https://github.com/vinceliuice/grub2-themes.git
cd grub2-themes
sudo ./install.sh -t tela -s 1080p
cd ..
rm -rf grub2-themes
## Zorin icons
git clone https://github.com/ZorinOS/zorin-icon-themes.git
cd zorin-icon-themes
sudo mv -r zorin-icon-themes/* /usr/share/icons/
rm -rf zorin-icon-themes
## Magnetic theme
git clone https://github.com/vinceliuice/Magnetic-gtk-theme.git
cd Magnetic-gtk-theme
./install.sh -l
sudo ./install.sh -g
cd ..
rm -rf Magnetic-gtk-theme
sudo cp -r ~/.themes/* /usr/share/themes/
## Gnome-shell -- a completer
## GTK -- a completer
## Flatpak -- a completer
## GDM -- a completer
# Gnome extensions
# Pipewire
sudo mkdir -p /etc/pipewire/pipewire.conf.d
sudo ln -s /usr/share/examples/wireplumber/10-wireplumber.conf /etc/pipewire/pipewire.conf.d/
sudo ln -s /usr/share/examples/pipewire/20-pipewire-pulse.conf /etc/pipewire/pipewire.conf.d/
sudo ln -s /usr/share/applications/pipewire.desktop /etc/xdg/autostart/
# Flatpak
flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
flatpak remote-add --if-not-exists flathub-beta https://flathub.org/beta-repo/flathub-beta.flatpakrepo
sudo flatpak override --filesystem=$HOME/.themes
sudo flatpak override --filesystem=$HOME/.icons
flatpak install -y com.mattjakeman.ExtensionManager com.vysp3r.ProtonPlus io.missioncenter.MissionCenter
# Nvidia on wayland
## Force enable GDM
sudo mkdir -p /etc/udev/rules.d
sudo ln -s /dev/null /etc/udev/rules.d/61-gdm.rules
sudo xbps-reconfigure --force linux
## Undervolt
sudo mkdir -p /opt/venvs/undervolt/
sudo python -m venv /opt/venvs/undervolt/
sudo /opt/venvs/undervolt/bin/pip install pynvml
sudo mkdir -p /etc/sv/undervolt/
sudo cp ./run /etc/sv/undervolt/run
sudo chmod +x /etc/sv/undervolt/run
sudo ln -s /etc/sv/undervolt/ /var/service/
## Optimus -- a completer
# Plymouth -- a completer
sudo plymouth-set-default-theme -R bgrt
# Backlight -- a completer
