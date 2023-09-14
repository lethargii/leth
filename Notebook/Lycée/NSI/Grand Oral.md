Est-il nécessaire d'avoir des compétences en algorithmique pour programmer un jeu vidéo ?
# Introduction
Aujourd'hui ce sont souvent des équipes composées de centaines de personnes qui conçoivent des jeux vidéo. Mais il y a aussi des développeurs indépendants qui font tout seul leurs propres jeux vidéo et ces derniers sont malgré tout plutôt populaires. On peut tout de même se demander si il faut des compétences en algorithmique pour programmer par soi-même un jeu vidéo surtout avec les moteurs de jeu d'aujourd'hui qui ont un certain nombre de fonctionnalités inclues. Pour répondre à cette question nous allons imaginer que l'on veut développer un jeu vidéo de type roguelike. Pour commencer il convient de définir ce qu'est l'algorithmique. L'algorithmique est l'étude des procédés et des techniques qui permettent de concevoir un algorithme. Un algorithme étant une procédure permettant de résoudre un problème donné.

Roguelike :
- Déplacements du joueur
On va commencer par implémenter quelque chose de très simple : les déplacements du joueur. C’est souvent la première chose que l’on va coder dans un jeu et dans certains moteurs de jeu cette fonctionnalité basique peut déjà être présente. Deux notions d'algorithmique sont nécessaires ici : les conditions qui permettent d'exécuter une instruction quand une condition est respectée et les variables qui permettent de garder en mémoire des données. Malgré tout, un algorithme très simple permet d'implémenter cette fonctionnalité. Cet algorithme consiste juste à incrémenter ou décrémenter les coordonnées du joueur qui seront représentées par les variables x et y (c'est à dire de les augmenter ou de les diminuer de 1) en fonction de la touche qui est appuyée. On incrémente x quand la touche droite est pressée et on le décrémente quand la touche gauche est pressée. On incrémente y quand la touche bas est pressée et on le décrémente quand la touche haut est pressée. Il y a cependant un problème avec cet algorithme puisqu’on se mettra à bouger plus vite quand on se déplace en diagonale et ce dernier peut donc être améliorée.

```python
class Joueur():
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def update():
		if bouton_droit:
			self.x += 1
		if bouton_gauche:
			self.x += -1
		if bouton_haut:
			self.y += -1
		if bouton_bas:
			self.y += 1
```
- Collisions entre objets
Ensuite, voyons les collisions. Pouvoir gérer les collisions est quelque chose qui est souvent indispensable dans un jeu vidéo. Les collisions sont donc gérées de base par beaucoup de moteurs de jeu. Prenons l'exemple de 2 boîtes de collisions carrées, pour vérifier si elle se superposent il faut utiliser les coordonnées de celles-ci. Si le x minimal ou le x maximal de la première boîte se situe entre le x minimal et le x maximal de la seconde boîte et le y minimal ou le y maximal de la première boîte se situe entre le y minimal et le y maximal de la seconde boîte alors elles entrent en collision.
```python
class Objet():
	def __init__(self, x, y, w, h):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
	def collision(self, objet):
		if collision:
			return True
```

- Génération procédurale de donjon
Un jeu roguelike utilise souvent une génération procédurale de donjon c'est à dire que les donjons sont créés de manière aléatoire tout en suivant une logique. Il n'existe à ma connaissance aucun moteur de jeu capable de faire cela et il est donc absolument nécessaire de le programmer par soi-même. Pour cela, on va créer un tableau d'une taille lambda qui sera rempli de 0. Au milieu du tableau on va remplacer le 0 par un 1. Les 0 représentent un emplacement vide et les 1 représentent des salles. Le premier 1 placé représente la salle de départ. Autour de cette première salle on crée au hasard des salles au dessus, en dessous, à gauche ou à droite et on répète le même processus pour chaque salle créée jusqu'à obtenir une taille de salle suffisante.
```python
def generation_procedurale():
	pass
```
Tout du long de cet oral on a fait comme si on programmait avec un certain paradigme de programmation. Un paradigme de programmation est une manière de programmer. Celui que l'on a utilisé est la programmation procédural qui consiste à décomposer un code en séries d'instructions et en fonctions qui sont elles aussi des suites d'instructions qui sont réutilisables dans un code. Mais il existe un autre paradigme qui est celui qui est utilisé en grande majorité pour créer un jeu vidéo : la programmation orienté objet. La programmation orienté objet ou POO consiste en la création d'objets qui possèdent leurs propres attributs ou variables et leurs propres méthodes ou fonctions. Il parait indispensable de comprendre la POO pour programmer un jeu puisque tous les moteurs de jeu l'utilisent.
# Conclusion
Pour conclure, il est possible de concevoir un jeu sans avoir de réelles connaissances en algorithmique avec certains moteurs de jeu qui ont un certain nombre de fonctionnalités pré-codées mais on doit se limiter à ces dites fonctionnalités. Pour pouvoir implémenter par soi-même de nouvelles fonctionnalités il peut être suffisant de comprendre comment fonctionnent les conditions, les opérateurs et les fonctions et d'utiliser un langage de script visuel bien qu'ils soient considérés comme limités et qu'ils ne permettent pas de faire tout ce que l'on veut. Mais pour programmer un jeu vidéo comme on le souhaite il est nécessaire d'avoir des compétences en algorithmique plus développées et surtout de savoir utiliser la programmation orienté objet.