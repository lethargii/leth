Est-il nécessaire d'avoir des compétences en algorithmique pour programmer un jeu vidéo ?
# Introduction
Aujourd'hui ce sont souvent des équipes composées de centaines de personnes qui conçoivent des jeux vidéo. Mais il y a aussi des développeurs indépendants qui font tout seul leurs propres jeux vidéo et qui sont malgré tout plutôt populaires. On peut tout de même se demander si il faut des compétences en algorithmique pour programmer par soi-même un jeu vidéo. Pour répondre à cette question nous allons imaginer que l'on veut développer un jeu vidéo de type roguelike. Pour commencer il convient de définir ce qu'est l'algorithmique. L'algorithmique est l'étude des procédés et des techniques qui permettent de concevoir un algorithme. Un algorithme étant une procédure permettant de résoudre un problème donné.

Roguelike :
- Déplacements du joueur
On va commencer par implémenter quelque chose de très simple : les déplacements du joueur. C’est souvent la première chose que l’on va coder dans un jeu. Une première notion d'algorithmique est nécessaire ici : ce sont les conditions. Si la touche gauche est pressée il faut aller à gauche. Ça reste malgré tout un algorithme très simple puisqu’il consiste juste à incrémenter ou décrémenter les coordonnées du joueur (c'est à dire de les augmenter ou de les diminuer de 1) en fonction de la touche qui est appuyée. On incrémente x quand la touche droite est pressée et on le décrémente quand la touche gauche est pressée. On incrémente y quand la touche bas est pressée et on le décrémente quand la touche haut est pressée. Il y a cependant un problème avec cet algorithme puisqu’on se mettra à bouger plus vite quand on se déplace en diagonale.

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
- POO
- 
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
- « IA » d’un ennemi/pathfinding

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
En conclusion, il est possible de concevoir un jeu sans avoir de réelles connaissances en algorithmique avec certains moteurs de jeu qui ont un certain nombre de fonctionnalités pré-codées mais on doit se limiter à ces dites fonctionnalités. Pour pouvoir implémenter par soi-même de nouvelles fonctionnalités on peut utiliser des langages de script visuel mais ceux-ci sont considérés comme limités et ne permettent pas de faire tout ce que l'on veut. Pour créer un jeu vidéo complet il est quasiment nécessaire selon moi de comprendre certaines notions d'algorithmique importantes.