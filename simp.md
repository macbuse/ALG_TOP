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


| Solide Platonicien   |  complexe simplicial | 
|-----------------------|-----------------|
| Tétraèdre             |  OUI| 
| Cube (Hexaèdre)       |                | 
| Octaèdre              |                |
| Dodécaèdre            |               | 
| Icosaèdre             |               | 
| Sphère             | OUI/NON             | 


#

### Espaces quotients
- On considère un espace topologique Y ainsi que relation
d’équivalence ∼ entre les points de Y. On note
$p : Y \rightarrow Y/∼$
la surjection canonique de Y sur son espace quotient.
- On définit une topologie sur Y/∼ en décrétant que 
$U \subset Y/∼$ est ouvert si $p^{-1}(U) \subset Y$ est ouvert
- Pour cette topologie, la surjection canonique p est
tautologiquement continue.

#

- L’espace quotient Y/∼ n’est pas nécessairement séparé.
- Un espace topologique est dit SÉPARÉ si tout couple de
points distincts admet des voisinages disjoints.
- Le **saturé** d’un ensemble F ⊂ Y est l’ensemble
$p^{-1}(p(F))$, c’est-à-dire tous les points de Y qui sont en
relation par ∼ à un point de F.
- La relation d’équivalence ∼ est dite FERMÉE si le saturé
de toute partie fermée est fermée.

| Propriété |
|---|
| Si Y est compact et la relation d’équivalence ∼ fermée <br> alors Y/∼ est séparé.|

# 

### Espaces quotients

- La compacité est une hypothèse contraignante. 
Elle peut être remplacée par une propriété plus faible, 

- **Définition.** Un espace topologique X est dit *localement
compact* 
    1. s’il est séparé 
    1. et si tout point x élément de X admet un voisinage compact (autrement dit si x appartient à un ouvert relativement compact)

- Exemples. Sont relativement compacts, tous les
compacts, tous les espaces homéomorphes à $\mathbb{R}^n$ , toutes
les variétés topologiques, tous les espaces discrets.



# 
Propriété bis (rappel).– Si Y est relativement compact et
la relation d’équivalence ∼ fermée alors Y/∼ est séparé.

#


- **Proposition de transfert de continuité au quotient.**
Soit f : Y → Z une application continue telle que 
pour tout $(y_1, y_2) \in Y$  on ait $y_1 ∼ y_2 \Rightarrow   f(y_1) = f(y_2)$
Alors l’application $\bar{f} : Y/∼ \,\rightarrow   Z$ donnée par $\bar{f}([y]) = f(y)$ 
est bien définie et continue.


- **Démonstration.** Le caractère bien défini provient du fait
que f est constante sur chaque classe d’équivalence.
- Soit U un ouvert de Z. L’image réciproque $\bar{f}^{-1}(U) \subset Y/~$ est  ouvert  si et seulement si $p^{−1}(\bar{f}^{−1}(U)) \subset Y$ est ouvert. 
Or par construction :
$p^{−1}(\bar{f}^{−1}(U)) = (\bar{f}\circ p)^{−1}(U) = f^{−1}(U)$ est ouvert car f continue.

#
### Exemple : le cercle $\mathbb{S}^1$

- Soit Y = [0, 1] et ∼ la relation d’équivalence définie par
    - x ∼ y ⇔ x = y ou x = 0 et y = 1 ou x = 1 et y = 0.

| proposition |
|---|
| L’espace quotient Y/∼ est homéomorphe au cercle $\mathbb{S}^1$.|

- **Démonstration.** L’application $f : Y \rightarrow    \mathbb{S}^1$ définie par 
f(x) = exp(2iπx) est continue et constante sur les classes
d’équivalence. Elle induit donc une application continue.




