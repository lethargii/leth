<u>**Remarque**</u>  
Dans ce cas, la charge totale $Q_{tot}$ de la distribution volumique contenue dans le volume $V$ est :  
$$Q_{tot}=\int\int\int_{P \in V}dq(P)=\int\int\int_{P /in V}\rho(P)d\tau$$  
Il peut arriver que les charges soient réparties sur une nappe d'épaisseur négligeable devant ses deux autres dimensions spatiales. Dans ce cas, on utilise une modélisation surfacique.  
On d;efinit la densité surfacique de charges au point P par :  
$$\sigma(P)=\frac{dq(P)}{dS} (unité C \cdot m^-2)$$  
où $dS$ est la surface élémentaire entourant le point $P$ et $dq(P)$ est la charge contenue dans $dS$.  
Enfin, lorsque les charges sont réparties en volume dans un tubedont le rayon est négligeable devant sa longueur on utilise une modélisation linéique. On définit la densité linéique de charge comme :  
$d(P)=\frac{dq(P)}{dl}$ (unité $C\cdot m^{-1})$  
<u>**Remarque**</u>  
Dans le cas surfacique, la charge totale de la distribution vaut :  
$$Q_{tot}=\int\int_{P\in S}dq(P)=\int\int_{P\in S} \Tau(P)dS$$  
Dans le cas linéique, on a :
$$Q_{tot}=\int_{P\in L}dq(P)=\int_{P\in L}\lambda(P)dl$$  
Dans le cas continu comme dans le cas discret, on peut utiliser le principe de superposition pour obtenir les formules donnant le champ électrostatique créé par une distribution de charges.
Soit $D$ une distribution continue de charges. Chaque charge élémentaire $dq(P)$ centrée en un point $P$ de la distribution créée, en un point $M$ de l'espace, le champe électrostatique élémentaire $d \vec E_p(M)$, qui vaut :  
$$d\vec E_p(M)=\frac{dq(P)}{4\pi \epsilon_0}\cdot \frac{\vec{PM}}{\| \vec PM \|^3}$$  
Le champ électrostatique total $\vec E_D(M)$ créé par $D$ en $M$ est la somme de ces champs élémentaires $d\vec E_p(M)$ lorsque $P$ parcourt la distribution $D$.  
Ainsi :  
- le champ créé par une distribution volumique de charges $V$ en un point $M$ de l'espace vaut :  
$$\vec E_v(M)=\int\int_{P\in V} d\vec E_p(M)=\int\int_{P\in S}\frac{dq(P)}{4\pi\epsilon_0}\cdot \frac{\vec{PM}}{\| \vec{PM}\|^3}$$  
donc :  
$$\vec E_S(M)=\int\int_{P\in S}\frac{\sigma(P)}{4\pi\epsilon_0}\cdot \frac{\vec{PM}}{\| \vec{PM \|^3}}\cdot dS$$  
Il n'est pas défini aux points M où la densité surfacique est non nulle (i.e. sur la surface chargée)
- le champ créé par une distribution linéique de charges de longueur $L$ en un point $M$ de l'espace s'écrit :  
$$\vec E_L(M)=\int_{P\in L}d\vec E_p(M)=\int_{P\in L}\frac{dq(P)}{4\pi\epsilon_0}\cdot \frac{\vec{PM}}{\| \vec{PM}\|^3}$$  
donc :  
$$\vec E_L(M)=\int_{P\in L}\frac{\lambda(P)}{4\pi\epsilon_0}\cdot \frac{\vec{PM}}{\| \vec{PM}\|^3}\cdot dl$$  
Il n'est pas défini sur les points où $\lambda\neq 0$, i.e. sur la ligne chargée.

## 5 Champ et force électrostatique
Dans le cas d'une charge ponctuelle et d'une distribution discrète de charges, on a défini le champs électrostatique via la force qu'il pouvait exercer sur une charge ponctuelle $q$.  
D'une façon générale, il s'agit de la définition du champs électrostatique.  
Soit $\Sigma$ une répartition de charges dans l'espace. Si on plaçait par la pensée une charge $q$ en un point $M$ de l'espace, cette charge subirait la force électrostatique $\vec f_{\Sigma\to q}$ venant de $\Sigma$. On définit le champ électromagnétique $\vec E_\Sigma(M)$ créé par $\Sigma$ en $M$ par :  
$$ \vec E_\Sigma(M)=\frac{i}{q}\cdot\vec f_{\Sigma\to q}$$  
Si il règne dans l'espace un champ électrostatique $\vec E$ dont on connait ou non l'origine, alors une charge $q$ placée en un point $M$ de l'espace subit une force électrostatique $\vec f$ qui s'écrit :  
$$\vec f=q\cdot \vec E(M)$$  
où $\vec E(M)$ est la valeur du champ $\vec E$ au point $M$.  
# <u>II. Interlude mathématique :</u>  
## <u>notion de différentielle et gradient</u>  
### <u>Notations et cadre de travail</u>  
On se place dans $\R ^3$ muni de sa base canonique $(e_1,e_2,e_3)$ et du produit scalaire usuel.  
On a :  
$$e_1=(1,0,0), e_2=(0,1,0) et e_3=(0,0,1)$$  
tout point $x\in \R^3$ peut s'écrire sous la forme  
$$x=x_1e_1+x_2e_2+x_3e_3=(x_1,x_2,x_3)$$  
et le produit scalaire entre deux points de $\R^3$ vaut :  
$$x-y=(x_1,x_2,x_3)-(y_1,y_2,y_3)=x_1y_1+x_2y_2+x_3y_3$$  
En particulier :  
$$e_i\cdot e_j=\delta_{ij}=$$
On voit donc que $x_i=x\cdot e_i$.  
On a ainsi :  
$$x=\sum^3_{i=1}(x-e_i)\cdot e_i \in \R^3$$  
Remarque :  
On rappelle que la norme de $x \in \R^3$ est $\|x\| = \sqrt{x\cdot x}$, et que la distance de $x \in \R^3$ à $y \in \R^3$ est $\|x-y\|$.  
![[Pysique dessin]]  
On considère $\Omega \subset \R^3$ et $f:\Omega \longrightarrow \R$  
On considèrera que $\Omega$ et $f$ sont "gentils", i.e. que $f4 est continue, dérivable, de dérivée continue (et toutes les dérivées qu'on cherche à écrire existent et sonty continues).  
### 2- Dérivées directionelles et partielles  
Soient $x \in \Omega$ et $v\in \R^3$.  
La fonction $ t \longmapsto f(x+tv)$ est bien définie autour de $0$, et sa dérivée en $0$ est appelée dérivée directionelle de $f$ en $x$ dans la direction $v$.  
![[Physique dessin 2]]  
Si $v = e_ i$, cette dérivée est la i-ième dérivée partielle de $f$ en $x$, notée $\partial_i(x)$ ou $\frac{\partial f}{\partial x_i}(x)$.  
SI $i=1$ par exemple, c'est la dérivée en $t=0$ de $t\mapsto f(x_1+t,x_2,x_3)$, ou la dérivée en $t=x_1$ de $t\mapsto f(t,x_2,x_3)$  
On note $\frac{\partial f}{\partial x_i} \Omega \longrightarrow \R$  
$x \longrightarrow \frac{\partial f}{\partial x_i}(x)$  
Exemple :  
Soit $f : \Omega \longrightarrow \R$  
$x=(x_1,x_2,x_3) \mapsto 3x_1^2 + \sin{x_2} + e^{x_3}$  
On a :  
$$\frac{\partial f}{\partial x_1}(x_1,x_2,x_3)=6x_1 + \sin{x_2}+ e^{x_3}$$  
$$\frac{\partial f}{\partial x_2}(x_1,x_2,x_3)=3x_1^2 + \cos{x_2}+ e^{x_3}$$  
$$\frac{\partial f}{\partial x_3}(x_1,x_2,x_3)=3x_1^2 + \sin{x_2}+ e^{x_3}$$  
### 3- Différentielle  
Pour tout $x\in \Omega$, la différentielle $df_x$ de $f$ en $x$ est la fonction  
$$df_x : \R^3 \longmapsto \R$$  
$$v=(v_1,v_2,v_3) \longmapsto \frac{\partial f}{\partial x_1}(x)\cdot v_1 +\frac{\partial f}{\partial x_2}(x)\cdot v_2 + \frac{\partial f}{\partial x_3}(x)\cdot v_3$$  
On note  
$dx_i : \R^3 \longmapsto \R$  
la fonction définie par  
$v=(v_1,v_2,v_3) \longmapsto v_i$, i.e. la projection sur la i-ième coordonnée.  
On a alors l'égalité :  
$df_i=\sum_{i=1}^{3} \frac{\partial f}{\partial x_i}(x)dx_i$  
La différentielle de $f$ est l'application  
$df : \Omega \cdot \R^3 \longmapsto \R$  
$(x,v) \longmapsto df_x(v)=\sum_{i=1}^{3}\frac{\partial f}{\partial x_i}(x)\cdot v_i$  
### 4- Règle de la chaine  
Cf polu sur Moodle  
### 5- Gradient  
Soit $x\in \Omega$, $df_x$ est "linéaire", i.e. qu'il existe un unique $a\in \R^3$ tel que $df_x : v \longmapsto a\cdot v$  
Cet unique vecteur $a$ est appelé le gradient de $f$ en $x$.  
On le notera $\vec{grad}f(x)$ dans ce cours. On trouve également la notation $\vec\nabla f(x)$ ou $\nabla f(x)$  
Pour tout $x\in \Omega$, $\vec{grad}f(x)\in \R^3$  
Le gradient de $f$ est l'application :  
$$\vec{grad}f : \Omega \longrightarrow \R^3  $$
$$x \longmapsto \vec{grad}f(x)$$  
Par définition, $\forall x \in \Omega \forall v \in \R^3$  
$df_x(v)=\vec{grad}f(x)\cdot v$  
Soit $(u_1,u_2,u_3)$ un repère orthonormé de $\R^3$, on a :  
$$\vec{grad}f(x)=\sum_{i=1}^{3}(\vec{grad}f(x)\cdot u_i)\cdot u_i$$  
En particulier, dans la base canonique on a :  
$$\vec{grad}f(x)=\sum_{i=1}^{3}(\vec{grad}f(x)\cdot e_i)\cdot e_i = \sum_{i=1}^{3}\frac{\partial f}{\partial x_i}(x)\cdot e_i = \begin{pmatrix} \frac{\partial f}{\partial x_1}(x)\\ \frac{\partial f}{\partial x_2}(x) \\ \frac{\partial f}{\partial x_3}(x)  
\end{pmatrix}$$  
À partir de l'expression de $\vec{grad}f(x)$ dans la bas canonique de $\R^3$, on peut déterminer l'expression du gradient de tout fonction scalaire $f:\Omega \subset \R^3\longrightarrow\R$ dans les systèmes de coordonnées usuels.  
On a :  
$$\vec{grad}f(x)=\frac{\partial f}{\partial x}\vec {u_x} + \frac{\partial f}{\partial y}\vec {u_y} + \frac{\partial f}{\partial z}\vec {u_z}$$  
en coordonnées cartésiennes,  
$$\vec{grad}f = \frac{\partial f}{\partial r}\vec {u_r} + \frac{1}{r}\frac{\partial f}{\partial \theta}\vec {u_\theta} + \frac{\partial f}{\partial z}\vec {u_z}$$  
en coordonnées cylindriques, et :  
$$\vec{grad}f = \frac{\partial f}{\partial r}\vec {u_r} + \frac{1}{r}\frac{\partial f}{\partial \theta}\vec {u_\theta} + \frac{1}{r\sin{\theta}}\frac{\partial f}{\partial \Phi}\vec {u_\Phi}$$ 
en coordonnées sphériques. 
# III - Potentiel électrostatique  
### 1- Potentiel électrostatique créé par une charge  
Considérons une charge $q$ placée en un point $O$, qu'on prendra comme origine d'un repère de l'espace muni d'une base sphérique.  
Cette charge crée en $M$ le champ  
$\vec E(M)=\frac{q}{4\pi\epsilon_0r^2}\vec{u_r}$ où $\vec{OM}=r\vec{u_r}$  
Soit $K \in \R$ une constante, on pose  
$V_K(M)=\frac{q}{4\pi\epsilon_0r}+K$  
Calculons le gradient de $V_K$.  
$$\begin{align*}\vec{grad}V_K(M)= & \frac{\partial V_K}{\partial r}(M)\vec {u_r} + \frac{1}{r}\frac{\partial V_K}{\partial \theta}(M)\vec {u_\theta} + \frac{1}{r\sin{\theta}}\frac{\partial V_K}{\partial \Phi}(M)\vec {u_\Phi} \\ & = \frac{\partial V_K}{\partial r}(M)\vec{u_r}\\ & = - \frac{q}{4\pi\epsilon_0}\cdot\frac{1}{r^2}\vec{u_r}\\ & = -\vec E(M)
\end{align*}$$  
Le champ électrostatique $\vec{E}(M)$ créé par une charge ponctuelle est donc un champ de gradient, i.e. qu'il s'écrit comme le gradient d'une fonction scalaire. Une telle fonction se nomme potentiel électrostatique. On dit que le champ électrostatiqur dérive d'un potentiel électrostatique.