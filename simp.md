<!--
theme: gaia
class: gaia lead
headingDivider: 1
paginate: true
header: UGA 2025
footer: 
backgroundImage: linear-gradient(-20deg, rgba(0, 0, 0, 0.6), transparent)
_paginate: false
_header: ''
_footer: ''

style: |
  @keyframes marp-outgoing-transition-vertical-scroll {
    from { transform: translateY(0%); }
    to { transform: translateY(-100%); }
  }
  @keyframes marp-incoming-transition-vertical-scroll {
    from { transform: translateY(100%); }
    to { transform: translateY(0%); }
  }

  @keyframes marp-outgoing-transition-vflip {
    0% { animation-timing-function: ease-in; }
    50% {
      transform: perspective(100vw) translateZ(-100vw) rotateX(-90deg);
      opacity: 0.5;
      animation-timing-function: step-end;
    }
    100% { opacity: 0; }
  }
  @keyframes marp-incoming-transition-vflip {
    0% {
      animation-timing-function: step-start;
      opacity: 0;
    }
    50% {
      transform: perspective(100vw) translateZ(-100vw) rotateX(90deg);
      opacity: 0.5;
      animation-timing-function: ease-out;
    }
  }

  header, footer { text-align: center; color: currentcolor; }
  section.small-code pre { font-size: 68%; }

-->

# Simplicial complexes
<!-- _transition: glow -->
greg mc shane


<!-- # -->
<!-- <!-1- _transition: cube -1-> -->


# Définition $n$-simplexe


Un **simplexe** est le type de polytope le plus simple dans une dimension donnée. Plus précisément, un simplexe est l'enveloppe convexe de  $\{ p_0,\ldots p_n\}$ points affinement indépendants dans $\mathbb{R}^n$. Il généralise la notion de triangle ou de tétraèdre à des dimensions arbitraires.

- **Simplexe de dimension 0** : Un point  
- **Simplexe de dimension 1** : Un segment de droite  
- **Simplexe de dimension 2** : Un triangle  
- **Simplexe de dimension 3** : Un tétraèdre  
- **Simplexe de dimension $n$** : Un $n$-simplexe avec $n+1$ sommets


#

- **sommets** : Les points $p_0,\ldots p_n$ sont appelés les Sommets
- **faces** : Les faces d'un simplexe sont les sous-ensembles de ses sommets. Par exemple, un tétraèdre a 4 faces : les triangles formés par 3 sommets.
- **le $n$-simplexe standard** est l'ensemble des points
$(x_0,\ldots,x_n)\in \mathbb{R}^n$ tels que $\sum x_i = 1$ et $x_i \geq 0$ pour tout
$i$.



# 

### Définition : Complexe simplicial  
- Un **complexe simplicial** $K$ est une famille de simplexes
qui satisfait les deux conditions suivantes :
1. **Fermeture par faces** : Si un simplexe $\sigma \in K$, alors toutes les faces de $\sigma$ appartiennent également à $K$. Une face d’un simplexe est tout sous-ensemble de ses sommets.
2. **Propriété d’intersection** : Si deux simplexes $\sigma_1, \sigma_2 \in K$ alors, leur intersection est 
    - soit vide, 
    - soit une face commune aux deux simplexes.

# 

### Exemples de complexes simpliciaux :


1. Un ensemble de points (simplexes de dimension 0) forme un complexe simplicial.
2. Un graphe (complexe simplicial de dimension 1) peut être vu comme un ensemble de sommets (simplexes de dimension 0) et d’arêtes (simplexes de dimension 1).
3. Une surface triangulée, où la surface est divisée en triangles (simplexes de dimension 2) partageant des arêtes et des sommets, constitue un complexe simplicial de dimension 2.
4. Un maillage tétraédrique, utilisé en modélisation 3D, forme un complexe simplicial de dimension 3.


[surface meshes](https://plotly.com/python/trisurf/)

<!-- ### Applications : -->
<!-- - **Topologie computationnelle** : Utilisés dans des algorithmes pour des tâches comme la reconnaissance de formes et l’analyse de données (par exemple, l’homologie persistante en analyse topologique des données). -->

#

## Notations

- On appelle COMPLEXE SIMPLICIAL K une collection de simplexes
$K = \{\sigma_\alpha\}_{\alpha \in A}$ telle que
- $\sigma_\alpha \in K \Rightarrow$ toutes les faces de $\sigma_\alpha$ sont dans K
- $\sigma_\alpha, \sigma_\beta \in K \Rightarrow$
    - $\sigma_\alpha \cap \sigma_\beta = \emptyset$  
    - ou $\sigma_\alpha \cap \sigma_\beta$ est une face de $\sigma_\alpha$ et de $\sigma_\beta$.

- La réalisation géométrique de K est le POLYÈDRE 
|K| de $\mathbb{R}^\infty$ définit par $|K| = \bigcup_{\alpha \in A} \sigma_\alpha$.


# 

## Dimension

- **Définition**.– Si $\sup \{\text{dim } \sigma_\alpha\} = k < +\infty$ 
on dit que K est un complexe simplicial de dimension k.

- un complexe simplicial de dimension k.
    - Un complexe simplicial de dimension 0 est espace
topologique discret
    - Un complexe simplicial de dimension 1 est un graphe




#


| Solide Platonicien   |  complexe simplicial | 
|-----------------------|-----------------|
| Tétraèdre             |  OUI| 
| Cube (Hexaèdre)       |                | 
| Octaèdre              |                |
| Dodécaèdre            |               | 
| Icosaèdre             |               | 
| Sphère             | OUI/NON             | 

#

### Espace quotient

- Soient X et Y deux espaces topologiques,
$A \subset Y$ et $f : A \to X$ une application continue. 
On définit une relation d’équivalence ∼ 
sur la somme disjointe $Z = X \sqcup Y$ par $z_1 ∼ z_2$

- si $z_1 = z_2$
 ou $(z_1 ∈ A \text{ et } z_2 = f(z_1))$
 ou $(z_2 ∈ A \text{ et } z_1 = f(z_2))$


- **Définition**– L’espace quotient est noté $X \cup_f Y = X \sqcup Y/∼$
et s’appelle le **recollement de $X$ à $Y$ le long de f.**




#

- **Définition.**– La donnée d’un espace topologique X et d’un
point base $x_0\in X$ est appelé un ESPACE POINTÉ et noté $(X, x_0)$.
- **Définition.**– Étant donnés deux espaces pointés 
$(X, x_0)$ et $(Y, y_0)$, on appelle BOUQUET DE X ET DE Y et 
$X \vee Y$ le recollement $X \cup_f Y$ où $A = \{y_0\}$ et $f(y_0) = x_0$
 On dit également que X ∨ Y est la SOMME POINTÉE de X
et de Y.


#

- **Exemple 1**.– Soit K un complexe simplicial connexe et fini
de dimension 1 et S l’ensemble de ses sommets (=face de
dimension 0). L’espace |K|/S est homéomorphe à un
bouquet de cercles dont le nombre de cercles est celui des
arêtes (=face de dimension 1) de K.
- **Exemple 2**.– Soit $A \subset \mathbb{S}^2$ un grand cercle,
$\mathbb{S}^2/A$ est un bouquet de deux sphères $\mathbb{S}^2 \vee \mathbb{S}^2$.
.
- **Exemple 3**.– Soit $A \subset \mathbb{S}^2$ l’ensemble des l’ensemble des arêtes de la triangulation par l’icosaèdre. L’espace $\mathbb{S}^2/A$ est un bouquet de 
vingt sphères.

#

- **Définition**.– Un CW -COMPLEXE X est un espace topologique
défini par la donnée d’une suite croissante (finie ou non)
$\emptyset \subset X^0 ⊂ X^1 ⊂ · · · ⊂ X^N = X$
d’espaces topologiques ($X^n$, n ∈ I) avec I = {0, 1, . . . , N} ou  $I = \mathbb{N}$,
- et telle que :
    -  $X = \bigcup_{n \in I} X^n$
    -  $X_0$ est un espace discret non vide
    - $X^n$ est obtenu en recollant $X^{n−1}$ avec une famille $(e^n_α)_{α \in A_n}$ 
    de n-cellules fermées par des applications continues $\phi_α : \partial e^n_α → X^{n−1}$, 

-  Une partie F est un fermé de X ssi son intersection avec $X^n$ est fermée pour tout $n \in I$.

#

-  Les espaces $X^n$ sont appelés les n-SQUELETTES,
les n-boules $e^n_α$ sont appelées les n-CELLULES.
-  Si I est finie, le dernier axiome est une conséquence
directe du fait que les inclusions entre les squelettes sont
des applications continues.
-  La topologie de X est la plus faible pour laquelle les
inclusions $X^n \subset X$ sont continues, autrement dit la TOPOLOGIE FAIBLE.
-  Cette topologie n’est par reliée à la TOPOLOGIE INITIALE
des espaces vectoriels topologiques, dite elle aussi,
TOPOLOGIE FAIBLE.
<!-- C’est la topologie de la limite directe $X = \varinjlim X^n \to X$. -->

#

- **Exemple 1** On considère le CW-complexe de dimension 1
donné par $X_0 = 1$ et
$X_1 =  X_0 \cup_\phi e_1$ où 
$e_1 = B_1 = [-1, 1]$ et $\phi : \partial e_1 \to X_0$ est
l’application constante.
    - D’après ce que l’on a établi plus haut
$X_1 \equiv e_1/\partial e_1 \equiv S_1$.
Ceci montre que le cercle $\mathbb{S}^1$ est un CW-complexes
ayant un point et une 1-cellule.

- **Exemple 2**– Plus généralement, la sphère $\mathbb{S}^n$ 
n admet une
structure de CW-complexe ayant un point et une n-cellule.   :

#


- **Exemple 3**.– L’espace projectif $\mathbb{R}P^2$ admet une structure de CW-complexe ayant un point, une 1-cellule et une 2-cellule.
Le 1-squelette est homéomorphe à $\mathbb{S}^1$ et le 2-squelette
est obtenu en attachant la 2-cellule avec 
$\phi : \partial e^2 \to X^1 \text{ donn\'ee par } z \mapsto z^2$

- **Exemple 4**.– Un complexe simplicial |K| a une structure
naturelle de CW-complexe donnée par sa filtration $|K^n|$ par
les n-simplexes.
    - Le point clé est que tout n-simplexe $\sigma_\alpha$ est (homéomorphe à) une n-boule. 
    - L’application de recollement $\phi_\alpha : \partial e^n_\alpha \to |K^{n-1}|$ est l’inclusion naturelle


#

- **Proposition**.– Soit X un CW-complexe alors
    -  X est séparé,
    -  l’adhérence de toute cellule $e_\alpha$ ne rencontre qu’un
nombre fini d’autres cellules,
    - X est compact ssi il se compose d’un nombre fini de
cellules.
- **Démonstration**– Voir le Hatcher, p. 521-523.
    - On peut comprendre maintenant la dénomination de ces
espaces. Les lettres "CW" sont les initiales de
Closure-finiteness et de Weak topology.
    - Les CW-complexes sont les « bons » espaces
topologiques. Kirby et Siebenmann démontrent que toute
variété topologique compacte de dimension n 6= 4 possède
une structure de CW-complexe.
