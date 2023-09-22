git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
yay -Y --gendb
yay -Syu --devel
yay -Y --devel --save
yay -S flatpak
yay -S pamac-all
yay -S godot-mono-bin labwc logmein-hamachi pamac-all rofi-lbonn-wayland sacad sfwbar adwaita-qt4 adwaita-qt5-git adwaita-qt6-git
