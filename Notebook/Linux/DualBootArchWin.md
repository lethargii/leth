# Installation simple d'arch linux ou en dual boot avec Windows
## Télécharger l'image d'Arch Linux et créer un média d'installation
1. Télécharger une image d'Arch Linux dans la catégorie Download de leur site web
2. Créer un média d'installation avec la commande dd sur Linux ou le logiciel Rufus sur Windows
Commande dd :
```bash
dd if=arch.iso of=/dev/media bs=4M & sync
```
## Booter sur le média d'installation
1. Entrer dans le bios de votre carte mère (la touche dépend de la carte mère, probablement Suppr/Del, F4, F12 ou une autre touche Fonction)
2. Booter sur la clé usb contenant l'image d'Arch Linux en mode UEFI
## Mettre le clavier en azerty
```bash
loadkeys fr-latin1
```
Appuyer sur q pour faire un a en qwerty.
## Verifier le mode de boot
Pour être sûr que vous pouvez bien installer systemd-boot et que vous avez bien démarré en mode UEFI :
```bash
ls /sys/firmware/efi/efivars
```
## Se connecter à Internet
Pour se connecter à Internet en wifi on utilisera un utilitaire appelé iwd.
Pour utiliser l'invite de commande :
```bash
iwctl
```
Pour en sortir :
```bash
exit
```
La démarche pour se connecter :
```bash
device list
```
```bash
station Station scan
```
Remplacer Station par un des appareils listés par la commande précédente.
S'il est impossible de se connecter au wifi, quitter l'invite de commande iwctl, utiliser cette commande avant de rentrer dans l'invite de commande :
```bash
rfkill unblock wifi
```
```bash
station Station get-networks
```
```bash
station Station connect Network
```
Remplacer Network par le réseau auquel vous voulez vous connecter, puis, entrer le mot de passe de votre réseau wifi.
## Mettre à jour l'horloge système
```bash
timedatectl
```
## Partitionner les disques
Pour faire cela il est possible d'utiliser fdisk ou d'autres gestionnaires de partitions.
Lister les disques et les partitions :
```bash
fdisk -l
```
Modifier un disque (souvent nommé nvmeXn1 pour les disques nvme ou sdX pour les ssd ou hdd, remplacer X par la lettre ou le chiffre correspondant):
```bash
fdisk /dev/disque
```
Il faut obligatoirement créer une partition Linux. Pour une installation simple il faut créer une partition UEFI (appelé EFI dans fdisk). Pour un dual boot il faut créer une partition XBOOTLDR (au format Linux Extended Boot) car la partition EFI de windows n'est pas assez grande.
## Formater les partitions
Formater la partition Linux en ext4 :
```bash
mkfs.ext4 /dev/mountpartition
```
Formater la partition UEFI (installation simple) ou XBOOTLDR (dual boot) en FAT32 :
```bash
mkfs.fat -F 32 /dev/efipartition
```
## Monter les partitions
Monter la partition Linux :
```bash
mount /dev/root_partition /mnt
```
Monter la partition EFI :
```bash
mount --mkdir /dev/efi_partition /mnt/efi
```
Monter la partition XBOOTLDR (dual boot):
```bash
mount --mkdir /dev/boot_partition /mnt/boot
```
## Sélectionner les miroirs
```bash
reflector --latest 100 --sort rate --protocol https --country France --age 12 --save /etc/pacman.d/mirrorlist
```
## Installation de linux
La commande ci-dessous permet d'installer les paquets essentiels au fonctionnement de Linux.
```bash
pacstrap -K /mnt base linux linux-firmware
```
Pour avoir le noyau linux zen pour waydroid :
```bash
pacstrap -K /mnt base linux-zen linux-firmware
```
### Fstab
Fstab est le fichier qui indique à votre système au démarrage quels partitions il doit monter.
```bash
genfstab -U /mnt >> /mnt/etc/fstab
```
### Chroot
```bash
arch-chroot /mnt
```
Cette commande permet de se connecter en tant que root (administrateur) à votre nouveau système.
## Installation de quelques paquets
C'est à ce moment que l'on fait la rencontre du gestionnaire de paquets d'Arch : pacman. Pour ceux qui ne savent pas c'est ce qui sert à télécharger des applications en gros. Avant de télécharger un paquet il ne faut pas oublier de synchroniser les dépôts (parce que sinon ben on peut rien télécharger).
Synchroniser les dépôts :
```bash
pacman -Ssy
```
Installer des paquets :
```bash
pacman -S vim sudo
```
## Dépôts officiels
```bash
pacman -S wine wget usbutils swaylock swaybg wofi reflector neofetch arch-install-scripts git base-devel fish openssh bluez bluez-utils bluez-plugins blueman flatpak noto-fonts-cjk noto-fonts-emoji noto-fonts gnome-terminal cinnamon gnome-themes-extra networkmanager sddm plasma-workspace xorg amd-ucode man-db vim sudo
```
```bash
pacman -S wget
```

On installe vim et sudo. vim est un éditeur de texte qui s'utilise d'une certaine manière (à venir). On aura besoin de vim par la suite. sudo permet en tant qu'utilisateur d'obtenir les droits d'administrateur pour modifier le système.
### Time zone
```bash
ln -sf /usr/share/zoneinfo/Region/City /etc/localtime
```
En l'occurence :
```bash
ln -sf /usr/share/zoneinfo/Europe/Paris /etc/localtime
```
```bash
hwclock --systohc
```
### Localization
```bash
vim /etc/locale.gen
```
Décommenter 'fr_FR.UTF-8 UTF-8'.
Décommenter 'en_US.UTF-8 UTF-8'
```bash
locale-gen
```
```bash
vim /etc/locale.conf
```
Écrire 'LANG=fr_FR.UTF-8'.
Écrire 'LANG=en_US.UTF-8'.
```bash
vim /etc/vconsole.conf
```
Écrire 'KEYMAP=fr-latin1'.
### Configuration du réseau
```bash
vim /etc/hostname
```
Écrire 'myhostname'.
```bash
vim /etc/hosts
```
```bash
127.0.0.1        localhost
::1              localhost
127.0.1.1        myhostname
```
### Mot de passe root
```bash
passwd
```
### Ajouter un utilisateur
Il est quasiment obligatoire d'ajouter un utilisateur autre que le root au système car se connecter au PC en ayant tous les droits pose des problèmes de sécurité considérables.
```bash
useradd -m -G wheel utilisateur
```
```bash
useradd -m utilisateur
```
```bash
usermod -aG wheel utilisateur
```
```bash
passwd utilisateur
```
```bash
EDITOR=/usr/bin/vim visudo
```
## Boot manager (systemd-boot)
bootctl permet d'installer systemd-boot en tant que bootloader. Il est nécessaire de spécifier le chemin de la partition EFI et de la partition XBOOTLDR pour que l'installation en dual boot se fasse correctement.
Installation simple :
```bash
bootctl install
```
Dual boot :
```bash
bootctl --esp-path=/efi --boot-path=/boot install
```
Normallement la partition windows sera automatiquement détectée pour le dual boot.
Il est cependant nécessaire de rajouter une entrée pour que Arch Linux soit détecté.
```bash
vim /boot/loader/loader.conf
```
```bash
default arch.conf
timeout 10
```
```bash
blkid /dev/root_partition
```
```bash
vim /boot/loader/entries/arch.conf
```
Noyau linux :
```bash
title Arch Linux
linux /vmlinuz-linux
initrd /initramfs-linux.img
options root=PARTUUID=YOUR_PARTUUID
```
Noyau linux-zen :
```bash
title Arch Linux
linux /vmlinuz-linux-zen
initrd /initramfs-linux-zen.img
options root=PARTUUID=YOUR_PARTUUID
```
```bash
pacman -S ucode
```
Remplacer ucode par amd-ucode ou intel-ucode.
Il faut aussi installer un driver vidéo pour que la carte graphique puisse fonctionner. (à venir)
## Installer un environnement de bureau
Sur Windows l'environnement de bureau est déjà présent. Arch Linux permet cependant d'en choisir un parmi tous ceux qui existent pour Linux. Pour commencer il faut installer un serveur d'affichage. Le plus utilisé aujourd'hui est xorg (wayland est le serveur d'affichage qui est censé supplanter xorg mais il n'est pas encore tout à fait au point).
Installer xorg :
```bash
pacman -S xorg
```
Il faut ensuite installer un gestionnaire d'affichage permettant de démarrer un environnement de bureau. Ce n'est pas réellement nécessaire mais démarrer depuis un temrinal est bien moins intuitif que démarrer avec une interface graphique. Des gestionnaires d'affichage il y en a plusieurs. Je conseille LightDM (avec le greeter GTK) ou SDDM (avec le thème breeze).
LightDM :
```bash
pacman -S lightdm lightdm-gtk-greeter
```
```bash
systemctl enable lightdm.service
```
SDDM :
```bash
pacman -S sddm plasma-workspace
```
```bash
systemctl enable sddm.service
```
```bash
vim /usr/lib/sddm/sddm.conf.d/default.conf
```
```bash
[Theme]
Current=breeze
```
```bash
vim /usr/share/sddm/themes/breeze/theme.conf.user
```
```bash
[General]
background=/usr/share/sddm/themes/breeze/background.jpg
```
Passons maintenant aux environnements de bureau. Le plus connu est certainement Gnome mais il me donne des boutons (l'interface se rapproche trop de ce que l'on voudrait pour une tablette ou un téléphone selon moi). Je préfère utiliser Cinnamon qui se rapproche de l'interface de Windows.
Installer cinnamon :
```bash
pacman -S cinnamon gnome-themes-extra
```
Ensuite ce serait pas mal de pouvoir se connecter au wifi. Network Manager permet de gérer le réseau.
Installer Network Manager :
```bash
pacman -S networkmanager
```
Activer Network Manager :
```bash
systemctl enable NetworkManager.service
```
Une interface graphique tout à fait fonctionnelle est maintenant présente mais on ne pourra pas faire grand chose sans terminal et sans navigateur internet. gnome-terminal est le terminal de base de Gnome (il est très bien) et firefox ben vous connaissez.
Installer gnome-terminal et firefox :
```bash
pacman -S gnome-terminal firefox
```
Maintenant on va pouvoir utiliser notre système comme on le souhaite. Il y a un certain nombre de choses qu'il ne sera possible de faire qu'après un redémarrage. Pour cela, il faut d'abord sortir du chroot.
Sortir du chroot :
```bash
exit
```
Redémarrer :
```bash
reboot
```
### Activer le pavé numérique au démarrage

```bash
pacman -S numlockx
```
```bash
vim /etc/lightdm/lightdm.conf
```
```bash
[Seat:*]
greeter-setup-script=/usr/bin/numlockx on
```
## Post-installation
```bash
localectl set-x11-keymap fr
```
```bash
pacman -S git base-devel
```
```bash
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
yay -Y --gendb
yay -Syu --devel
yay -Y --devel --save
yay -S pamac-all
```
```bash
sudo pacman -S bluez bluez-utils bluez-plugins blueman
```
```bash
modprobe btusb
```
```bash
systemctl enable bluetooth.service
```
## Activer le multilib
```bash
vim /etc/pacman.conf
```
```bash
[multilib]
Include = /etc/pacman.d/mirrorlist
```

## AUR
```bash
yay -S godot-mono-bin harmonoid-bin labwc logmein-hamachi pamac-all rofi-lbonn-wayland sacad sfwbar waydroid
```
## Flatpak
```bash
flatpak install ca.littlesvr.asunder com.atlauncher.ATLauncher com.discordapp.Discord com.github.Matoking.protontricks com.github.tchx84.Flatseal com.github.ztefn.haguichi com.heroicgameslauncher.hgl com.obsproject.Studio com.parsecgaming.parsec com.prusa3d.PrusaSlicer com.raggesilver.BlackBox com.usebottles.bottles com.vscodium.codium de.haeckerfelix.Shortwave eu.betterbird.Betterbird info.cemu.Cemu io.github.sameboy.SameBoy io.mgba.mGBA md.obsidian.Obsidian net.davidotek.pupgui2 net.kuribo64.melonDS net.pcsx2.PCSX2 net.rpcs3.RPCS3 net.sourceforge.Klavaro net.supertuxkart.SuperTuxKart org.DolphinEmu.dolphin-emu org.audacityteam.Audacity org.blender.Blender org.freecadweb.FreeCAD org.gimp.GIMP org.gnome.Shotwell org.inkscape.Inkscape org.kde.ark org.kde.kalk org.kde.kdenlive org.kde.krita org.libreoffice.LibreOffice org.libretro.RetroArch org.mozilla.firefox org.openmw.OpenMW org.openrgb.OpenRGB org.ppsspp.PPSSPP org.ryujinx.Ryujinx org.videolan.VLC org.yuzu_emu.yuzu
```