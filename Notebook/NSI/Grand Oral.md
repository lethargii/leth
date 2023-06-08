# Introduction
 Je vais vous parler des algorithmes simples que l’on utilise souvent dans les jeux-vidéo et de comment les implémenter en programmation orientée objet en python. Pour rappel la programmation orientée objet est un paradigme de programmation (c’est à dire une manière de programmer) qui consiste en l’utilisation d’objets qui possèdent leurs propres fonctions et leurs propres attributs (qui sont des variables propres aux objets). La POO est le paradigme de programmation principalement utilisé dans les jeux-vidéo car dans un jeu tout peut s’apparenter à un objet : le joueur, les ennemis, les maisons, les arbres, la barre de vie…   


Roguelike :
- Déplacements du joueur
On va commencer par implémenter quelque chose de très simple : les déplacements du joueur. C’est souvent la première chose que l’on va coder dans un jeu et c’est un algorithme très simple puisqu’il consiste juste à incrémenter ou décrémenter les coordonnées du joueur en fonction de quelle touche est appuyée.
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
Cela reste une fonctionnalité nécessaire dans beaucoup de jeux vidéo donc elle par exemple présente dans RPG maker.
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
- « IA » d’un ennemi

```python
class Ennemi():
	def __init__(self, x, y ,w ,h):
		pass
	def update(self):
		pass
```
- Génération procédurale de donjon
```python
def generation_procedurale():
	pass
```

# Conclusion
En conclusion, il est possible de concevoir un jeu sans avoir de réelles connaissances en algorithmique avec certains moteurs de jeu qui ont un certain nombre de fonctionnalités précodées mais on doit se limiter à ces dites fonctionnalités. Il devient alors quasiment obligatoire de programmer que ce soit de manière visuelle ou textuelle.