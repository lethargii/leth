## Centre étrangers J2 - Exercice 1

Figure 1.
1.
a. Une adresse valide pour le routeur F serait 192.168.5.0
b. On pourra connecter 254 machines

2.
a. Le masque de sous-réseau du réseau B correspond à 255.255.240.0
b.
192.168.2.2 = 11000000.10101000.00000010.00000010
255.255.240.0 = 11111111.11111111.11110000.00000000
11111111.11111111.11110000.00000000
ET 11000000.10101000.00000010.00000010
= 11000000.10101000.00000000.00000000
11000000.10101000.00000000.00000000 = 192.168.0.0
c. L'intérêt d'avoir une telle interconnexion entre les quatre routeurs A, B, E et F permet que le réseau continue de fonctionner si un câble est coupé ou qu'un routeur ne marche plus.

Figure 2.
1.
a. Chemin possible entre les routeurs A et E : 
- A-B-E
Chemins possibles entre les routeurs F et B : 
- F-H-G-B
- F-D-G-B
- F-D-A-B
b.
E :
| Destination | Routeur suivant | Distance |
| ----------- | --------------- | -------- |
| A           | B               | 2        |
| B           | B               | 1        |
| C           | H               | 2        |
| D           | G               | 2        |
| F           | H               | 2        |
| G           | G               | 1        |
| H           | H               | 1        |

G :
| Destination | Routeur suivant | Distance |
| ----------- | --------------- | -------- |
| A           | B               | 2        |
| B           | B               | 1        |
| C           | D               | 2        |
| D           | D               | 1        |
| E           | E               | 1        |
| F           | H               | 2        |
| H           | H               | 1        |
2.
a.
F :
| Destination | Routeur suivant | Coût total |
| ----------- | --------------- | ---------- |
| A           | D               | 1,1        |
| B           | H               | 10,11      |
| C           | D               | 1,1        |
| D           | D               | 0,1        |
| E           | H               | 10,1       |
| G           | D               | 1,1        |
| H           | H               | 0,1        |
b. E-H-F-D

## Centre étrangers J2 - Exercice 2

1.
a.
b.

2.
a.
b.

3.
a.
b.

4.
a.
b.

## Centre étrangers J2 - Exercice 3 (pas terminé)
1.
a.
`>>>bonjour('Alan')`
'Bonjour Alan !'

b. x et y sont de type bool
La valeur de x est False
La valeur de y est True.

c.
```python
def occurences_lettre(une_chaine : str,une_lettre : str) -> int:
	'''
		* Définition :
			fonction prenant en paramètres une chaîne une_chaine et une lettre une_lettre et renvoyant le nombre d'occurences de une_lettre dans une_chaine
		* Exemple :
			>>>occurences_lettre('Bonjour', 'o')
			2
		* Préconditions :
			une_chaine(str) : une chaîne dans laquelle on va rechercher le nombre d'occurence de une_lettre
			une_lettre(str) : une lettre dont on va rechercher le nombre d'occurences dans une_chaine
		* Postconditions :
			(int) : le nombre d'occurences de une_lettre dans une_chaine
	'''
	nb_occurences = 0
	for element in une_chaine:
		if element == une_lettre:
			nb_occurences = nb_occurences + 1
	return nb_occurences
```
2.
a.
b.

3.
a. mystere(abr_mots_francais) renvoie 336531 car la fonction renvoie la taille d'n arbre binaire (la taille de abr_mots_francais est de 336531)
b.
```python
def hauteur(un_abr) -> int:
	if un_abr.est_vide():
		return 0
	else:
		hauteur_gauche = hauteur(un_abr.sous_arbre_gauche)
		hauteur_droit = hauteur(un_abr.sous_arbre_droit)
		if hauteur_gauche > hauteur_droit:
			return 1 + hauteur_gauche
		else:
			return 1 + hauteur_droit
```

4.
a.
```python
def chercher_mots(liste_mots,longueur,lettre,position):
    res = []
	for i in range(len(liste_mots)): 
		if liste_mots[i] == longueur and liste_mots[i][position] == lettre:
            res.append(liste_mots[i])
    return res
```
b. Cette commande renvoie la liste de mots français de 3 lettres dont la deuxième lettre est 'a' et dont la troisième lettre est 'x'. Elle renvoie donc ['fax', 'max'].
c.
`>>>chercher_mots(chercher_mots(chercher_mots(liste_mots_francais,5,'t',4),5,'e',5),5,'r',6)`