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

