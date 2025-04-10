- Il existe beaucoup de distributions linux, peut-être un peu trop.
  :LOGBOOK:
  CLOCK: [2024-05-04 Sat 23:21:35]--[2024-05-04 Sat 23:21:51] =>  00:00:16
  :END:
  Lorsqu'on découvre linux on ne sait pas vraiment où aller tellement on a de choix.
  Ce "tutoriel" va vous permettre, je l'espère d'y voir un peu plus clair sur quelle distribution linux choisir...
  Tout d'abord, qu'est-ce qui est vraiment important pour choisir une distribution linux ?
  Pour moi ça peut se résumer à 3 points :
  1. La popularité de la distribution
  2. Le type de distribution et le gestionnaire de paquet
  3. L'environnement de bureau
  Pour le premier point, ça peut paraître évident ou pas mais il faut choisir une distribution relativement populaire.
  Pourquoi ?
  Eh bien parce qu'une distribution pas très connue peut très bien fonctionner ou pas. Dans ce dernier cas, il n'y aura peut-être pas de support pour résoudre les problèmes.
  Ensuite, je dis relativement connu parce qu'il ne faut pas forcément prendre la distribution linux la plus connue.
  Il suffit qu'il y ait une communauté active sur la distribution linux souhaitée...
  
  Pour le deuxième point, il existe différentes "familles" de distribution linux qui possèdent des gestionnaires de paquets différents.
  Si je cite ceux qui me viennent à l'esprit là maintenant, on a Debian avec apt, les Fedora avec dnf ou yum, Arch Linux avec pacman et Gentoo avec portage.
  On va les séparer en deux grandes familles : la famille des LTS (long-term service) et la famille des rolling-release.
  Debian et Fedora sont des LTS et Arch Linux et Gentoo sont des rolling-release.
  Mais qu'est-ce que ça veut dire ?
  Ben en fait Debian et Fedora se basent sur des versions et Arch Linux et Gentoo non.
  Mais qu'est-ce que ça change ?
  Concrètement, pour une version donnée de Debian ou de Fedora les logiciels en eux-mêmes ne reçoivent pas de mise à jour autres que les patchs de sécurité ce qui en fait des systèmes très stables tandis que Arch Linux et Gentoo reçoivent des mises à jour en continu ce qui en fait des systèmes moins stables mais toujours à la pointe de la technologie.
  En pratique les distributions LTS correspondent plus à la majorité des utilisateurs car une distribution rolling-release peut casser.
  Je recommande donc de prendre une distribution LTS.
  
  Pour le troisième point, qui me semble être le plus important, ils existent une multitude d'environnement de bureau sous linux.
  Vous ne savez pas de quoi je parle ?
  L'environnement de bureau c'est l'apparence graphique de votre bureau. Sous Windows il y a un et un seul environnement de bureau et pareil pour MacOS. Sous linux, il y en a plein.
  Les 2 plus connus sont certainement Gnome et KDE Plasma. Personnellement, je ne recommande pas Gnome car l'interface ressemble beaucoup trop à celle d'une tablette. KDE Plasma ressemble plutôt à l'interface de Windows et est extrêmement modulable. On peut l'observer en prenant l'exemple de la distribution Linuxfx qui fait semblant d'être Windows 11 (attention je ne recommande pas Linuxfx pour autant car juste ressembler à Windows 11 n'apporte rien).
  Il y en a d'autres comme Cinnamon ou Pantheon. Cinnamon ressemble beaucoup à l'interface de Windows 7 et c'est d'ailleurs pour ça que je l'utilise. Pantheon, quant à lui, mimique l'apparence de MacOS.
  Pour les ordinateurs qui ne sont pas tous neufs, il existe XFCE, LXQT, LXDE, Mate... qui sont très légers en ressources mais qui en conséquence sont moins beaux et proposent moins de fonctionnalités.
  Voire pour un PC très très lent il y a les gestionnaires de fenêtres qui sont en quelque sorte des environnements de bureau minimaux. Parmi ceux-ci, on compte : Openbox, Fluxbox, Blackbox et bien d'autres...
  De manière alternative, il existe des environnements de bureau qui n'utilisent pas des fenêtre flottantes (c'est à dire des fenêtres que l'on redimensionne comme on veut et que l'on peut bouger) mais des tiles (où les fenêtres sont réparties sur l'écran). Quelques exemples : i3, Sway... La plupart des utilisateurs préféreront des fenêtres flottantes.
  Vous le voyez, il existe une infinité de manière de configurer son environnement de bureau.
  
  En conclusion, voici une petite liste de distributions que je conseille :
  1. Distributions user-friendly
  - Linux Mint (Cinnamon, XFCE ou Mate)
  - ElementaryOS (Pantheon)
  - KDE Neon (KDE Plasma)
  - Fedora (Gnome)
  - PopOS! (Cosmic, un fork de Gnome)
  2. Distributions rolling-release
  - Manjaro
  - EndeavourOS
  - Calculate Linux
  3. Distributions source
  - Debian
  - Arch Linux
  - Gentoo