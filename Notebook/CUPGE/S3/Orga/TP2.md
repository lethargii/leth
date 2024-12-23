---
title: "Manipulation N°2"
subtitle: "Synthèse d'un monomère de type ester : le benzoate d'éthyle"
author: "Lucien Sevault Wolber et Marc Prince"
date: "29/11/24"
geometry: margin=2cm
mainfont: Arial
output:
  pdf_document: 
    latex_engine: xelatex
header-includes:
    - \usepackage{chemfig}
    - \usepackage{mhchem}
    - \usepackage{siunitx}
    - \usepackage{mathtools}
---
## 1. Introduction

L'objectif de ce TP est de synthétiser du benzoate d'éthyle, par réaction d'estérification entre l'acide benzoïque et l'éthanol. Nous manipulerons différentes substances chimiques comme l'acide sulfurique ou l'éther par exemple et nous verrons différentes techniques utilisées en TP : l'évaporation, l'extraction et la distillation sous pression réduite.

### 2. Écrire l'équation bilan de la réaction.

$\ce{C7H6O2 + C2H6O ->[H+] C9H10O2 + H2O}$

### 3. Remplir le tableau ci-après et le joindre au compte-rendu.

|                                             | $\chemfig[atom sep=2em]{*6(-=-(-([:-30]-OH)([:90]=O))=-=)}$ | $\chemfig{EtOH}$              | $\chemfig[atom sep=2em]{*6(-=-(-([:-30]-OEt)([:90]=O))=-=)}$ |
|---------------------------------------------|-------------------------------------------------------------|-------------------------------|--------------------------------------------------------------|
| Nom du composé                              | Acide benzoïque                                             | Éthanol                       | Benzoate d'éthyle                                            |
| Formule brute                               | $\ce{C7H6O2}$                                               | $\ce{C2H6O}$                  | $\ce{C9H10O2}$                                               |
| Masse molaire ($\si{g/mol}$)                | $122\si{g/mol}$                                             | $46\si{g/mol}$                | $150\si{g/mol}$                                              |
| Densité ou masse volumique ($\si{g/mL}$)    | $1,3\si{g/mL}$                                              | $0,79\si{g/mL}$               |                                                              |
| Point de fusion ($\text{mp}$)               | $122,35\si{\degree C}$                                             | $-114,14\si{\degree C}$              | $-34\si{\degree C}$                                                 |
| Point d'ébullition ($\text{T}_\text{eb}$)   | $249,9\si{\degree C}$                                              | $78,23\si{\degree C}$                | $212\si{\degree C}$                                                 |
| Masse ou volume engagé/obtenu               | $7,5\si{g}$/$5,76923\si{mL}$                                     | $23,7\si{g}$/$30\si{mL}$ | $4,37\si{g}$                                                             |
| Quantité de matière engagée/attendue en mol | $0,0614754\si{mol}$                                         | $0,51522\si{mol}$             | $0,0614754\si{mol}$                                          |
| Nombre d'équivalent                         | $1$                                                      | $8,38$                           |                                                              |
| Masse théorique attendue                    |                                                             |                               | $9,22131\si{g}$                                              |

#### Détail des calculs :  

$\text{M}_\text{benzoïque} = \text{x}_\text{C}\text{M}_\text{C} + \text{x}_\text{H}\text{M}_\text{H} + \text{x}_\text{O}\text{M}_\text{O} = 7\times 12 + 6\times 1 + 2\times 16 = 122\si{g/mol}$

$\text{M}_\text{éthanol} = \text{x}_\text{C}\text{M}_\text{C} + \text{x}_\text{H}\text{M}_\text{H} + \text{x}_\text{O}\text{M}_\text{O} = 2\times 12 + 6\times 1 + 1\times 16 = 46\si{g/mol}$

$\text{M}_\text{éthyle} = \text{x}_\text{C}\text{M}_\text{C} + \text{x}_\text{H}\text{M}_\text{H} + \text{x}_\text{O}\text{M}_\text{O} = 9\times 12 + 10\times 1 + 2\times 16 = 150\si{g/mol}$

$\text{m}_\text{benzoïque} = 7,5\si{g}\text{ (Données du TP)}$

$\text{V}_\text{éthanol} = 30\si{mL}\text{ (Données du TP)}$

$\text{V}_\text{benzoïque} = \frac{\text{m}_\text{benzoïque}}{\rho_\text{benzoïque}} = \frac{7,5}{1,3} = 5,76923\si{mL}$

$\text{m}_\text{éthanol} = \rho_\text{éthanol}\text{V}_\text{éthanol} = \frac{0,79}{30} = 23,7\si{g}$

$\text{n}_\text{benzoïque} = \frac{\text{m}_\text{benzoïque}}{\text{M}_\text{benzoïque}} = \frac{7,5}{122} = 0,0614754\si{mol}$

$\text{n}_\text{éthanol} = \frac{\text{m}_\text{éthanol}}{\text{M}_\text{éthanol}} = \frac{23,7}{46} = 0,51522\si{mol}$

$\text{n}_\text{éthyle} = \text{n}_\text{benzoïque} = 0,0614754\si{mol}\text{ (Voir la question 4)}$

Pour calculer le nombre d'équivalent, on prend comme référence le facteur limitant, c'est à dire l'acide benzoïque.

$\text{Q}_\text{benzoïque} = \frac{\text{n}_\text{benzoïque}}{\text{n}_\text{benzoïque}} = 1$

$\text{Q}_\text{éthanol} = \frac{\text{n}_\text{éthanol}}{\text{n}_\text{benzoïque}} = \frac{0,51522}{0,0614754} = 8,38$

$\text{m}_\text{éthyle} = \text{n}_\text{éthyle}\rho_\text{éthyle} = \times 150$

### 4. Y a-t-il un facteur limitant à la réaction ? Lequel ?

Il n'y a en théorie pas de facteur limitant à la réaction car elle n'est pas totale. Cependant, on déplace l'équilibre vers la droite en mettant en excès l'éthanol (ici on compare directement la quantité de matière car les deux réactifs ont les mêmes coefficients stochiométriques):

$\text{n}_\text{benzoïque} = 0,0614754\si{mol} << \text{n}_\text{éthanol} = 0,51522\si{mol}$

On peut donc considérer que le facteur limitant est l'acide benzoïque.

### 5. Écrire le mécanisme de la réaction d'estérification.

$$\chemfig[atom sep=2em]{@{O1}\charge{90=\|, -90=\|}{O}([:-180]=([:120]-*6(-=-=-=))([:-120]-OH))}
+
\chemfig[atom sep=2em]{@{H+}\charge{45:3pt=\(\oplus\)}{H}}
\chemmove[red]{
\draw[shorten <=3pt, shorten >=5pt](O1) ..controls +(up:10mm) and +(north east:10mm)..(H+);}$$

$$\rightleftharpoons$$

$$\chemfig[atom sep=2em]{@{O2}\charge{90:3pt=\(\oplus\)}{O}H([:-180]=[@{db2}]([:120]-*6(-=-=-=))([:-120]-OH))}
\chemmove[red]{
\draw[shorten <=3pt, shorten >=5pt](db2) ..controls +(down:10mm) and +(down:10mm)..(O2);}$$

$$\rightleftharpoons$$

$$\chemfig[atom sep=2em]{OH([:-180]=@{C3}\charge{180:6pt=\(\oplus\)}{}([:120]-*6(-=-=-=))([:-120]-OH))}
+
\chemfig[atom sep=2em]{Et@{O3}\charge{90=\|, -90=\|}{O}H}
\chemmove[red]{
\draw[shorten <=3pt, shorten >=5pt](O3) ..controls +(up:10mm) and +(up:10mm)..(C3);}$$

$$\rightleftharpoons$$

$$\chemfig[atom sep=2em]{HO-([:-90]-OH)([:90]-*6(-=-=-=))(-\charge{-90:3pt=\(\oplus\)}{O}([:60]-\textcolor{red}{H})([,0.08em]-Et))}$$

$$\rightleftharpoons$$

$$\chemfig[atom sep=2em]{HO-([:-90]-\charge{-90:3pt=\(\oplus\)}{\textcolor{blue}{O}}\textcolor{blue}{H}([:180]-\textcolor{red}{H}))([:90]-*6(-=-=-=))(-O([,0.08em]-Et))}$$

$$\rightleftharpoons$$

$$\chemfig[atom sep=2em]{O([,0.08em]-Et)([:180]-\charge{-60:3pt=\(\oplus\)}{}([:-120]-[@{sb61}]O([:180]-[@{sb62}]H))([:120]-*6(-=-=-=)))}
+
\chemfig[atom sep=2em]{\textcolor{blue}{HO}([:-60,0.1em]-\textcolor{red}{H})}
\chemmove[red]{
\draw[shorten <=3pt, shorten >=5pt](sb62) ..controls +(up:5mm) and +(north west:5mm)..(sb61);}$$

$$\xrightleftharpoons[]{-\ce{H+}}$$

$$\chemfig[atom sep=2em]{O([,0.08em]-Et)([:180]-([:-120]=O)([:120]-*6(-=-=-=)))}
+
\chemfig[atom sep=2em]{H2O}$$

#### Explication du mécanisme :

La réaction se passe en milieu acide, donc en présence de $\ce{H+}$. L'oxygène qui a une double liaison de l'acide carboxylique, ici l'acide benzoïque est protoné. L'oxygène va récupérer un électron sur le carbone voisin entrainant la formation d'un carbocation. L'oxygène de l'éthanol attaque le carbocation pour s'y attacher. Le hydrogène du groupement alcool de l'éthanol va donner son électron à l'oxygène pour protoner l'oxygène d'un autre groupement alcool. L'oxygène du groupement alcool concerné va reprendre un électron au carbone voisin entrainant la formation d'un carbocation et la cassure de la liaison entre le carbone et l'oxygène (créant ainsi de l'eau). Le carbocation va ensuite récupérer un électron en cassant la liaison $\ce{OH}$ sur le groupement alcool restant ce qui entraine la formation de la molécule finale (un $\ce{H+}$ est aussi relaché avec la cassure de la liaison $\ce{OH}$).

### 6. Quelle est la composition du mélange réactionnel en fin de réaction ?

En fin de réaction, le mélange réactionnel est composé de benzoate d'éthyle, d'acide benzoïque, d'eau, d'éthanol, d'acide sulfurique et de pierres ponces.

### 7. Dans l'ampoule à décanter, lors de l'extraction ou des lavages, comment savoir où se situe la phase organique ? La phase aqueuse ?

Le solvant de la phase organique est l'éthanol et celui de la phase aqueuse est l'eau. L'eau étant plus dense que l'éthanol la phase aqueuse se retrouvera en dessous de la phase organique.Si il y a un doute on peut rajouter de l'eau et voir dans quelle phase elle se retrouve.

### 8. Expliquer comment est éliminé chaque produit non désiré.

L'éthanol est éliminé par évaporation (avec l'évaporateur rotatif). Les pierres ponces seront filtrés lorsque l'on mettra le mélange réactionnel dans l'ampoule à décanter pour l'extraction. L'eau sera principalement éliminé quand on séparera la phase aqueuse de la phase organique lors de l'extraction et du lavage, le reste sera éliminé lors du séchage avec le sulfate de sodium. L'acide benzoïque sera éliminé lors du lavage à l'hydrogénocarbonate de sodium, de même pour l'acide sulfurique. L'éther sera éliminé par évaporation avec l'évaporateur rotatif.

### 9. Calculer le rendement brut (avant purification). Détailler le calcul.

$\text{r}_\text{brut} = \frac{\text{m}_\text{expérimentale, pré-purification}}{\text{m}_\text{théroique}}\times 100 = \frac{7,63}{9,22131}\times 100 = 82,74\si{\percent}$

### 10. Calculer le rendement final (après purification).

$\text{r}_\text{final} = \frac{\text{m}_\text{expérimentale, post-purification}}{\text{m}_\text{théroique}}\times 100 = \frac{4,37}{9,22131}\times 100 = 47,39\si{\percent}$

### 11. Déterminer la pression à vide.

On trouve une température d'ébullition à vide $\text{T}_\text{eb} = 85\si{\degree C}$.
Grâce à l'abac, on trouve une pression à vide $\text{P}_\text{vide} = 6\si{Pa}$.

## 12. Conclusion

Pour conclure, lors de ce TP, nous avons pu observer l'action d'une réaction d'estérification entre un acide carboxylique et un alcool. Il était intéressant de découvrir de nouvelles techniques, notamment le lavage (pour supprimer les produits non souhaités) et la distillation (pour purifier des substances chimiques liquides).
