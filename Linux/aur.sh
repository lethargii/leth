git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
yay -Y --gendb
yay -Syu --devel
yay -Y --devel --save
yay -S pamac-all
yay -S logmein-hamachi pamac-all sacad mint-themes
