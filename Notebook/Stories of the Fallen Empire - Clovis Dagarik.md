## "Moteur de jeu"
1. Pygame + Tiled
2. Godot + plugin python
3. Blender Game Engine/UPBGE

On a voté et ce sera Godot.
Le plugin python marche à moitié donc je vais utiliser le langage de Godot, GDScript. La syntaxe est très proche de python donc c'est cool. En fait j'ai changé d'avis et je vais utiliser C# parce que c'est plus performant et puis c'est un langage bien plus utilisé.

## Équipe
- Ewil : Programmation
- Wolfrost : Scénario
- Lolilol : Musique/Son
- Shito : Dessin

## Scénario

Nous suivons l'histoire de Clovis Dagarik... (woah)

## Arbre de programmation du jeu

### Un Node Game qui va contenir tous les éléments du jeu

#### Un CanvasLayer contenant qui contiendra tous les éléments de l'UI

##### Le menu principal

##### Les dialogues

##### L'inventaire

##### Le menu de pause

##### La vie du personnage

#### Un Node2d qui contiendra les niveaux, le joueur, les ennemis

##### Les 3 layers des niveaux

##### Le personnage, les Pnjs et les ennemis

##### L'arrière plan et le premier plan

##### La caméra