# Dual Boot Arch Linux et Windows avec systemd-boot
## Télécharger l'image d'Arch Linux et créer un média d'installation
1. Télécharger une image d'Arch Linux dans la catégorie Download de leur site web
2. Créer un média d'installation avec la commande dd sur Linux ou le logiciel Rufus sur Windows
```bash
dd if=arch.iso of=/dev/media bs=4M
```
## Booter sur le média d'installation
1. Entrer dans le bios de votre carte mère (la touche dépend de la carte mère peut-être Suppr/Del)
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
Pour se connecter à Internet en wifi, procéder comme ci-dessous :
```bash
iwctl
```
```bash
device list
```
```bash
station Station scan
```
Remplacer Station par un des appareils listés par la commande précédente.
S'il est impossible de se connecter au wifi, utiliser cette commpande :
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
Il faut créer une partition Linux et une partition XBOOTLDR (au format Linux Extended Boot) car la partition EFI de windows n'est pas assez grande.
## Formater les partitions
Formater la partition Linux en ext4 :
```bash
mkfs.ext4 /dev/mountpartition
```
Formater la partition XBOOTLDR en FAT32 :
```bash
mkfs.fat -F 32 /dev/efipartition
```
## Monter les partitions
Monter la partition Linux :
```bash
mount /dev/root_partition /mnt
```
Monter la partition EFI de windows :
```bash
mount --mkdir /dev/efi_partition /mnt/efi
```
Monter la partition XBOOTLDR :
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
Synchroniser les dépôts :
```bash
pacman -Ssy
```
```bash
pacman -S networkmanager vim sudo terminal
```
### Time zone
```bash
ln -sf /usr/share/zoneinfo/Region/City /etc/localtime
```
```bash
hwclock --systohc
```
### Localization
```bash
vim /etc/locale.gen
```
Uncomment 'fr_FR.UTF-8 UTF-8'.
```bash
locale-gen
```
```bash
vim /etc/locale.conf
```
Write 'LANG=fr_FR.UTF-8'.
```bash
vim /etc/vconsole.conf
```
Write 'KEYMAP=fr-latin1'.
### Configuration du réseau
```bash
vim /etc/hostnam
```
Write 'myhostname'.
### Mot de passe root
```bash
passwd
```
### Ajouter un utilisateur
Il est quasiment obligatoire d'ajouter un utilisateur autre que le root au système car se connecter au PC en ayant tous les droits
```bash
useradd -m utilisateur
```
```bash
usermod -aG wheel,audio,video,storage utilisateur
```
```bash
passwd utilisateur
```
```bash
visudo
```
## Installer systemd-boot
bootctl permet d'installer systemd-boot en tant que bootloader. Il est nécessaire de spécifier le chemin de la partition EFI et de la partition XBOOTLDR pour que l'installation se fasse correctement.
```bash
bootctl --esp-path=/efi --boot-path=/boot install
```
Normallement la partition windows sera automatiquement détectée.
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
```bash
title Arch Linux
linux /vmlinuz-linux.img
options root=PARTUUID=YOUR_PARTUUID
```
```bash
pacman -S ucode
```
Remplacer ucode par amd-ucode ou intel-ucode.
# Installer un environnement de bureau
```bash
pacman -S lightdm
```
```bash
pacman -S lightdm-gtk-greeter
```
```bash
pacman -S xorg
```
```bash
pacman -S cinnamon
```
```bash
systemctl enable lightdm.service
```
```bash
systemctl enable NetworkManager.service
```
```bash
pacman -S gnome-terminal
```
```bash
pacman -S firefox
```
```bash
localectl set-x11-keymap fr
```
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
yay -S flatpak
yay -S pamac-all
```