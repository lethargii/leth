---
title: "Manipulation N°3"
subtitle: "Hydrolyse basique d'un ester : Détermination du produit d'hydrolyse"
author: "Lucien Sevault Wolber et Marc Prince"
date: "05/12/24"
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

L'objectif de ce TP est de déterminer le produit d'hydrolyse entre un ester inconnu et l'hydroxyde de potassium. Pour ce faire, nous utiliserons différentes techniques comme la RMN $\ce{^1H}$, la spectrométrie de masse ou la spectroscopie infrarouge.

### 2. Écrire l'équation bilan générale de la réaction d'hydrolyse basique d'un ester.

$$\chemfig[atom sep=2em]{O([:180]=([:120]-R)([:-120]-R'O))}
+
\chemfig[atom sep=2em]{H2O}
\rightleftharpoons
\chemfig[atom sep=2em]{O([:180]=([:120]-R)([:-120]-HO))}
+
\chemfig[atom sep=2em]{R'([, 0.08em]-OH)}$$

### 3. Écrire le mécanisme de la réaction d'hydrolyse basique d'un ester.

$$
\chemfig[atom sep=2em]{H@{O11}\charge{90:3pt=\(\ominus\)}{O}}
\qquad + \qquad
\chemfig[atom sep=2em]{@{O12}\charge{75:10pt=\(\delta^-\)}{O}([:180]=[@{db1}]\charge{75:13pt=\(\delta^+\)}{}([:120]-R)([:-120]-R'O))}
\chemmove[red]{
\draw[shorten <=2pt, shorten >=8pt](O11) ..controls +(north east:12mm) and +(west:1mm)..(db1);
\draw[shorten <=2pt, shorten >=1pt](db1) ..controls +(down:5mm) and +(down:5mm)..(O12);
}
\qquad
\rightleftharpoons
\qquad
\chemfig[atom sep=2em]{HO-(-[@{sb21}]@{O21}\charge{45:3pt=\(\ominus\)}{O})([:90]-R)([:-90,,,2]-[@{sb22}]R'@{O22}O)}
\chemmove[red]{
\draw[shorten <=8pt, shorten >=3pt](O21) ..controls +(80:5mm) and +(up:5mm)..(sb21);
\draw[shorten <=1pt, shorten >=1pt](sb22) ..controls +(east:5mm) and +(east:5mm)..(O22);
}
\qquad
\rightleftharpoons
\qquad
\chemfig[atom sep=2em]{O([:180]=([:120]-R)([:-120]-HO))}
\qquad
+
\qquad
\chemfig[atom sep=2em]{R'\charge{45:3pt=\(\ominus\)}{O}}
$$

#### Explication du mécanisme :  

Nous sommes en milieu basique il y a donc présence de $\ce{OH-}$. L'oxygène de l'hydroxyde attaque l'ester pour former un carbocation et créer un $\ce{O-}$. Le carbocation récupère son électron sur le $\ce{O-}$ ce qui provoque la séparation du groupement $\chemfig{R'O}$.

### 4. Pourquoi faut-il acidifier le milieu réactionnel par $\ce{HCl}$ en fin de réaction ?

Il faut acidifier le milieu réactionnel par $\ce{HCl}$ en fin de réaction car puisque l'on fait la réaction en milieu basique, on obtient la base conjuguée du produit d'hydrolyse.

### 5. À l'aide de l'analyse centésimale et de la spectrométrie de masse, déterminer la formule brute du produit d'hydrolyse.

$$\frac{\si{\percent} C}{100} = \frac{x_{C} M_{C}}{M}$$
$$x_{C} = \frac{\si{\percent} C \cdot M}{M_{C}\times 100} = \frac{72,97\times 148}{12\times 100} = 9$$
$$\frac{\si{\percent} H}{100} = \frac{x_{H} M_{H}}{M}$$
$$x_{H} = \frac{\si{\percent} H \cdot M}{M_{H}\times 100} = \frac{5,41\times 148}{1\times 100} = 8$$
$$\frac{\si{\percent} O}{100} = \frac{x_{O} M_{O}}{M}$$
$$x_{O} = \frac{\si{\percent} O \cdot M}{M_{O}\times 100} = \frac{21,62\times 148}{16\times 100} = 2$$

La formule brute du produit d'hydrolyse est :  
$$\ce{C9H8O2}$$

### 6. À l'aide du spectre infrarouge et de la RMN 1H du produit d'hydrolyse, déterminer sa formule développée.

Sur le spectre infrarouge :  
On a un pic à $1686\si{cm^{-1}}$ qui correspondrait à un acide carboxylique.  
On a un pic à $1631\si{cm^{-1}}$ qui correspondrait à un alcène.  
On a un pic à $3027\si{cm^{-1}}$ qui correspondrait à un $\ce{CH}$ d'aromatique.  

Sur la RMN $\ce{^1H}$ :  
On a deux doublets, supposément un alcène $\chemfig[atom sep=2em]{C([:150]-)([:-150]-)(=C([:30]-)([:-30]-))}$

Les hydrogènes restants forment certainement un aromatique.

On trouve la formule développée suivante :  
$$\chemfig[atom sep=2em]{*6(-=-([:30]-([:-30]=([:30]-([:90]=O)([:-30]-OH))))=-=)}$$

### 7. Vérifier que le produit d'hydrolyse que vous proposez est cohérent à l'aide du point de fusion mesuré.

On trouve un point de fusion de $139\si{\degree C}$ ce qui est cohérent avec le produit d'hydrolyse trouvé (Température théorique de $135\si{\degree C}$).

### 8. À l'aide du spectre RMN 1H de l'ester de départ, déterminer sa formule développée.

On suppose qu'il y a un groupement ester.  


On a un doublet, supposément un alcène $\chemfig[atom sep=2em]{CH=CH([:30]=)([:-30]-)}$  


On a un autre doublet, supposément un alcène $\chemfig[atom sep=2em]{C-CH=CH-C}$  


On a un triplet à $1,4\si{ppm}$, supposément un saturé primaire $\chemfig[atom sep=2em]{CH3-CH2}$  


On a un quadruplet, supposément un saturé secondaire $\chemfig[atom sep=2em]{O-CH2-CH3}$  


Les hydrogènes restants forment certainement un aromatique.

On trouve la formule développée suivante :  
$$\chemfig[atom sep=2em]{*6(-=-([:30]-([:-30]=([:30]-([:90]=O)([:-30]-O([:30]-([:-30]-))))))=-=)}$$

### 9. De quel stéréoisomère s'agit-il ? Cis ou trans ? Pourquoi ?

Il s'agit d'un diastéréoisomère trans car par rapport à la double liaison les deux groupes ne seront pas du même côté (la molécule sera plus stable dans cette configuration).

### 10. Retrouver le nom de cet ester.

Le nom de cet ester est : Cinnamate d'éthyle.

### 11. Calcul du rendement de l'hydrolyse. Détailler les calculs.

$\text{r} = \frac{\text{m}_\text{expérimentale}}{\text{m}_\text{théroique}}\times 100 = \frac{1,57}{1,68128}\times 100 = 93,3\si{\percent}$  
On trouve un rendement de l'hydrolyse $\text{r} = 93,3\si{\percent}$.

### 12. Compléter le tableau ci-après et le joindre au compte-rendu.

|                                           | $\chemfig[atom sep=2em]{*6(-=-([:30]-([:-30]=([:30]-([:90]=O)([:-30]-O([:30]-([:-30]-))))))=-=)}$ | $\chemfig{KOH}$        | $\chemfig[atom sep=2em]{*6(-=-([:30]-([:-30]=([:30]-([:90]=O)([:-30]-OH))))=-=)}$ |
|-------------------------------------------|-----------------------------------------------------------------------------------|------------------------|-----------------------------------------------------------------------------------|
| Nom du composé                            | Cinnamate d'éthyle                                                                | Hydroxyde de potassium | Acide cinnamique                                                                  |
| Formule brute                             | $\ce{C11H12O2}$                                                                   | $\ce{KOH}$             | $\ce{C9H8O2}$                                                                     |
| Masse molaire ($\si{g/mol}$)              | $176\si{g/mol}$                                                                   | $56,1\si{g/mol}$       | $148\si{g/mol}$                                                                   |
| Densité ou masse volumique ($\si{g/mL}$)  | $1,05\si{g/mL}$                                                                   | $2,044\si{g/mL}$       | $1,2475\si{g/mL}$                                                                 |
| Point de fusion ($\text{mp}$)             | $6\si{\degree C}$                                                                 | $380\si{\degree C}$    | $135\si{\degree C}$                                                               |
| Point d'ébullition ($\text{T}_\text{eb}$) | $271\si{\degree C}$                                                               | $1324\si{\degree C}$   | $300\si{\degree C}$                                                               |
| Masse ou volume engagé                    | $2\si{g}$                                                                         | $2\si{g}$              |                                                                                   |
| Quantité de matière engagée en mol        | $0,01136\si{mol}$                                                                 | $0,03565\si{mol}$      | $0,01136\si{mol}$                                                                 |
| Nombre d'équivalent                       | $1$                                                                               | $3,1382$               |                                                                                   |
| Masse théorique attendue                  |                                                                                   |                        | $1,68128\si{g}$                                                                   |

#### Détail des calculs :  

$\text{M}_\text{ester} = \text{x}_\text{C}\text{M}_\text{C} + \text{x}_\text{H}\text{M}_\text{H} + \text{x}_\text{O}\text{M}_\text{O} = 11\times 12 + 12\times 1 + 2\times 16 = 176\si{g/mol}$

$\text{M}_\text{potassium} = \text{x}_\text{K}\text{M}_\text{K} + \text{x}_\text{O}\text{M}_\text{O} + \text{x}_\text{H}\text{M}_\text{H} = 1\times 39,1 + 1\times 16 + 1\times 1 = 56,1\si{g/mol}$

$\text{M}_\text{produit} = \text{x}_\text{C}\text{M}_\text{C} + \text{x}_\text{H}\text{M}_\text{H} + \text{x}_\text{O}\text{M}_\text{O} = 9\times 12 + 8\times 1 + 2\times 16 = 148\si{g/mol}$

$\text{m}_\text{ester} = 2\si{g}\text{ (Données du TP)}$

$\text{m}_\text{potassium} = 2\si{g}\text{ (Données du TP)}$

$\text{V}_\text{potassium} = \frac{\text{m}_\text{potassium}}{\rho_\text{potassium}} = \frac{2}{2,044} = 0,9785\si{mL}$

$\text{V}_\text{ester} = \frac{\text{m}_\text{ester}}{\rho_\text{ester}} = \frac{2}{1,05} = 1,905\si{mL}$

$\text{n}_\text{ester} = \frac{\text{m}_\text{ester}}{\text{M}_\text{ester}} = \frac{2}{176} = 0,01136\si{mol}$

$\text{n}_\text{potassium} = \frac{\text{m}_\text{potassium}}{\text{M}_\text{potassium}} = \frac{2}{56,1} = 0,03565\si{mol}$

$\text{n}_\text{produit} = \text{n}_\text{ester} = 0,01136\si{mol}\text{ (Car la réaction est limitée par le cinnamate d'éthyle)}$

Pour calculer le nombre d'équivalent, on prend comme référence le facteur limitant, c'est à dire le cinnamate d'éthyle.

$\text{Q}_\text{ester} = \frac{\text{n}_\text{ester}}{\text{n}_\text{ester}} = 1$

$\text{Q}_\text{potassium} = \frac{\text{n}_\text{potassium}}{\text{n}_\text{ester}} = \frac{0,03565}{0,01136} = 3,1382$

$\text{m}_\text{produit} = \text{n}_\text{produit}\rho_\text{produit} = 0,01136\times 148 = 1,68128\si{g}$

## 13. Conclusion

Pour conclure, lors de ce TP, nous avons pu observer l'inverse d'une réaction d'estérification, la réaction d'hydrolyse (ou saponification car on est en milieu basique). On a pu observer que la RMN $\ce{^1H}$, la spectrométrie de masse et la spectroscopie infrarouge permettait bien d'identifier les différentes molécules manipulées.
