# Programmation Web - HTML

## Introduction

Les SGBD ne sont pas gérés par les utilisateurs donc il faut fournir une interface.
1989 : Premier navigateur
1990 : HTTP et URI/URL
1989/1991 : HTML
1994 : W3C
1994 : PHP pour rendre dynamique
1995 : JavaScript pour rendre dynamique encore plus
1996 : CSS1 pour ajouter du style

### Evolution du Web

Web 2.0 (web collaboratif, wiki, blog)
3.0 sémantique

### Moyens techniques

Langage de scripts
Côté serveur (PHP...)
Côté client (FLash...)

Aujourd'hui c'est le HTML (structure de la page), JS (dynamique de la page), CSS (mise en forme)
Pas de JavaScript dans ce cours.
On verra HTML, CSS et PHP.

On verra différentes architectures web :
- Web statique (site ne dépendant pas de variables)
- Web dynamique (certains paramètres peuvent changer par le biais de l'interrogation d'une page de données)

### Web statique

On clique sur un lien, la page index.html est cherché et s'afficher. Il faut donc juste écrire des fichiers HTML. Il est nécessaire de changer soi-même le site pour faire un quelconque changement.

### Web dynamique

Le contenu du fichier HTML peut être modifié.

On clique sur un lien, on remplit un formulaire et la page Page.php est cherchée et elle crée un fichier HTML en récupérant éventuellement des infos d'une base de données.

Le web dynamique s'appelle aussi application à page multiple.

## Quelques langages

Structure et contenu des pages : HTML, XML
Mise en forme : CSS
Comportement : JavaSript, AJAX
Générer le contenu : PHP, Python, JS, TS, Java
Interroger une source de données : SQL, Xpath, Xquery

# HTML : Généralités

Hypertext Markup Language
- extension .html
- langage de balise
- HTML2 en 1996, HTML 3/4 en 1997, HTML5 en 2014

HTML sert uniquement à la structure.
- Le navigateur lit le fichier et affiche les balise dans l'ordre. 

Le nom d'une balise indique le type d'élément qu'on ajoute.

### Balises en paires

<balise> contenu </balise>
<h1> titre </h1>

### Balises orphelines

<balise />
<br/>

Une balise ouvrante peut contenir des attributs :

<balise nomAtt1="val1" nomAtt2="val2"> ... </balise>
- Permet de spécifier des infos concernant la mise en forme, les propriétés de la balise...

- On peut imbriquer des balises (une image au milieu d'un paragraphe)
<balise1><balise3 /><balise2></balise2></balise1>
Il ne faut pas entremeler les balises :
<balise1><balise3 /><balise2></balise1></balise2>

On peut faire des commentaires :

<!-- Un ex de commentaire -->

# Structure d'une page HTML

<!DOCTYPE html> pour spécifier la norme à utiliser en début de fichier
<html lang="fr"> pour spécifier le début du document (lang donne la langue)
<head>
<!-- Bloc d'entête contenant les métadonnées, scripts (fiche de style CSS par exemple) -->
</head>
<body>
<!-- Bloc affiché dans le navigateur -->
</body>
</html>

<head>
<meta charset="utf-8"/> pour l'encodage
<title> Titre de la page (obligatoire) </title>
<link rel="stylesheet" type="text/css" href="includes/styles.css">
<meta name="keywords" content="BDD-IHM, Cours, HTML">
<meta name="author" content="ESIR">
</head>

<body> donne la structure
On peut mettre dans body des balises structurantes et de contenu.

Plus précisément :
- Titre
- paragraphe
- image
- lien hypertext
- Tableau

<body>
Du texte, du texte et du texte sans forme.
</body>

On aura juste "Du texte, du texte et du texte sans forme."

# Bonnes pratiques

- Rigueur lors de l'écriture des Balises
- Balise en minuscule
- Eviter les balises spécifiques à un seul navigateur
- Indenter le code (pas comme moi)
- Eviter des blocs de code trop compacts (pour aérer)
- Valider son fichier HTML avec le validateur de la W3C.

Balises apportant de la sémantique :
- header (entête)
- footer (pied de page)
- nav (barre de navigation)
- section
- article
- aside (contenu sur le côté)
- main (section principale)

Site web structuré comme la figure page 27.

# Balises de regroupement

Header :
- entete en haut de la page
- logo, nom du site, slogan
- possibilité de plusieurs entêtechniques

Footer :
- en bas de page
- contacts

Section :
- regroupe des contenus selon leur thématique

Article :
- zone de contenu à part pouvant être reprise ailleurs

Aside :
- zone complémentaire au contenu principal

Nav :
- Zones contenant uniquement des liens hypertextes permettant de naviguer dans la page

Une balise a une type de rendu :
- Inline (balise suivante affichée sur la même ligne)
- Block (retour à la ligne)

Div :
- regroupe des éléments de type bloc ou inline

Span :
- regroupe les éléments de type inline (pour mettre une suite de mots en évidence)

# Bonnes pratiques 2
- Réfléchir à la structure dès sa conception (faire un schéma du site)
- Utiliser en priorité les balises structurantes
- Utiliser ensuite les balises div et span

# Balises de contenu

<h1></h1>
...
<h6></h6>
Titre 1 à 6

<p>Un paragraphe</p>
<p>Un autre sur une <br/>autre ligne</p>

- Notion de bloc retour à la ligne entre les paragraphes
- <br/> pour faire un retour à la ligne dans un paragraphe

<strong>Texte en gras</strong>
<em>Texte en italique</em>
<mark>Texte surligné</mark>

# Listes

Non ordonnées :
<ul></ul>

Ordonnées :
<ol></ol>

Pour chaque ligne des listes :
<li></li>

<ul>
    <li>Thé</li>
    <li>Café</li>
    <li>Chocolat</li>
</ul>

# Tableaux

Défini par :

<table></table>

- <tr></tr> pour chaque ligne
- <th></th> pour une cellule d'entête ou <td></td> pour le reste

<table>
    <tr>
        <th> Une cellue d'entêtre </th>
    </tr>
    <tr>
        <td> Une cellule pas d'entête </td>
    </tr>
</table>

# Liens hypertextes

<a href="url">zone cliquable</a>
href spécifie l'adresse sur laquelle on va quand on clique
la zone dans la balise est la zone cliquable

Autres attributs :
- target qui prend "_self" (pour ouvrir dans l'onglet courant) ou "_blank" (pour ouvrir dans un autre onglet) comme paramètre
- name : permet de définir une zone d'ancrage pour se déplacer rapidement dans un document

Exemples :

<a href="documents/doc.pdf"> Un lien avec un chemin relatif</a>
<a href="https://esir.univ-rennes.fr"> Un lien externe avec un chemin absolu</a>

# Images

Balise orphelines
<img src="url" alt="texte alternatif"/>
src : chemin de l'image
alt : texte alternatif si jamais l'image ne se charge pas
- Pour ajouter une légende <figcaption>
- Pour regrouper l'image et la légende <figure>


Il existe plus de 100 balises en HTML

Liens diapo 43 pour des exemples.

# Identifiant

On peut associer un id à une balise
- Attribut id

- Cela permet de référencer certaines balises et de manipuler plus facilement ces éléments (via un langage de programmation)

<p id="Coucou"></p>
<img id="Image" src="image.png"></img>

# Classe

On peut associer une classe à plusieurs balises
- Attribut class

- Utile pour appliquer une mise en forme (CSS) identique à plusieurs balises et pour manipuler des éléments via un langage de programmation

# Formulaire

Un formulaire est une zone interactive de la page

Il permet :
- Aux utilisateurs de saisir des paramètres et de les envoyer au serveur
- De générer une page web avec les paramètres

Un formulaire est composé de différents éléments correspondant à un paramètre
Ex : Champ de texte, liste déroulante, case à cocher...

Balise <form action"url" method="POST|GET" name="nomForm"></form>
- Attribut action : page sur laquelle on est redirigé
- Attribut name : pour nommer le formulaire (optionnel)
- Attribut method : POST (paramètres transmis de le corps de la page HTML) ou GET (paramètres transmis dans l'URL de la page)

Balise <input> :
- Champ de texte
- Cases
- Boutons

Chaque composant possède les attributs id (id du composant) et name (pour récupérer les données)

Label : permet d'associer un texte descriptif à un composant
<label for="id du composant"> texte descriptif </label>

Saisie de texte :

<input type="texte" name="nom" id="idTexte"/>
- Champ de saisie pour un texte
- Balise orpheline
- Attribut value="valeur" permet d'avoir un texte pré-rempli

Mot de passe

<input type="password" name="mdp" id="idmdp"/>

Cases à cocher

<input type="checkbox" name="produit" id="idproduit" value="Lait" checked/>

Boutons radios :
<input type="radio" name="radio" id="idradio1" value="HTML" checked/>
<input type="radio" name="radio" id="idradio2" value="HTML" checked/>
Même nom pour qu'un seul soit coché

Boutons submit :
<input type="submit" value"texte" id="btn_submit"/>

- Bouton déclarant le chargement de la page de destination

Paramètres cachés :
<input type="hidden" value="val" name="hello"/>
- Composant caché non visible par l'utilisateur
- Valeur par défaut val

Ramener son PC pour les TD en plus des TP.
