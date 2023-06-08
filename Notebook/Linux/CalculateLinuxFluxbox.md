Ceci est un tutoriel pour obtenir un interface graphique à partir d'une installation de Calculate Linux Scratch.
Tout d'abord, démarrer le média d'installation et sélectionner les paramètres de votre configuration avant de rentrer dans l'installeur en ligne de commande.

Une simple commande nommée cl-install permet d'installer automatiquement CLS. Le rajout d'un utilisateur personnalisé à la place de l'utilisateur guest est simplement une préférence personnelle.
```bash
cl-install -u lethargii:all:default,wheel
```
Pour pouvoir continuer l'installation il faut se connecter au wifi. L'utilitaire installé par défaut est network-manager auquel on peut accéder par la commande nmcli.
```bash
nmcli d wifi connect Station password Password
```
Il faut maintenant utiliser la commande de Calcu```bash
cl-update
```
```bash
<<<<<<< HEAD
emerge -avq nano vim sudo fluxbox lightdm lightdm-gtk-greeter x11-base/xorg
```
```bash
visudo
=======
merge -avq nano vim sudo fluxbox lightdm lightdm-gtk-greeter x11-base/xorg
```
```bash
visudo
```
Uncomment wheel.
```bash
rc-update add xdm
>>>>>>> 40e23f73c3fa202b2d14372f194f9599a7064f0f
```