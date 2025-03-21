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

# Algebraic Topology
<!-- _transition: glow -->
greg mc shane


<!-- # -->
<!-- <!-1- _transition: cube -1-> -->
<!-- - slides : google **greg mcshane github** -->
<!-- - click on **serfest** -->
<!-- - if there is a bug in my slides blame [this guy](https://github.com/yhatt) -->

# La mauvaise réponse de la maitresse

#


| Solide Platonicien   | Nombre de Faces | Nombre d'Arêtes | Nombre de Sommets |
|-----------------------|-----------------|------------------|-------------------|
| Tétraèdre             | 4               | 6                | 4                 |
| Cube (Hexaèdre)       | 6               | 12               | 8                 |
| Octaèdre              | 8               | 12               | 6                 |
| Dodécaèdre            | 12              | 30               | 20                |
| Icosaèdre             | 20              | 30               | 12                |
| Sphère             | ???             | ???              | ???
|



# Caractéristique d'Euler

- La caractéristique d'Euler $\chi$ est une **invariante topologique** 
des polyèdres convexes et d'autres objets géométriques. 


|Formule de la caractéristique d'Euler|
|-------------------------------------|
|$\chi = S - A + F$|


| Où :  |
|-------------------------------------|
| ( S ) est le nombre de sommets (vertices)|
| ( A ) est le nombre d'arêtes (edges) |
| ( F ) est le nombre de faces (faces) |

<!-- - \( S \) est le nombre de sommets (vertices), -->  
<!-- - \( A \) est le nombre d'arêtes (edges), -->  
<!-- - \( F \) est le nombre de faces (faces). -->  

#

Pour un polyèdre convexe, la caractéristique d'Euler vaut toujours $\chi = 2$, conformément au théorème d'Euler.

- Exemple avec un cube (hexaèdre) :  
  S = 8  ,  A = 12  ,   F = 6 . <br> 
En appliquant la formule :  $\chi = S - F+ A = 8 - 12 + 6 = 2$


# Cas des autres polyèdres convexes :

| Solide Platonicien   | Caractéristique d'Euler |
|-----------------------|-----------------|
| **Tétraèdre** | $\chi = 4 - 6 + 4 = 2$  |
| **Octaèdre** | $\chi = 6 - 12 + 8 = 2$  |
| **Dodécaèdre** | $\chi = 20 - 30 + 12 = 2$  |
| **Icosaèdre** | $\chi = 12 - 30 + 20 = 2$  |

La caractéristique d'Euler est aussi utile pour les surfaces plus complexes, mais sa valeur peut varier en fonction de la topologie <br> (par exemple, pour un tore, $\chi = 0$


# L'erreur de la maitresse

| Solide Platonicien   | Nombre de Faces | Nombre d'Arêtes | Nombre de Sommets |
|-----------------------|-----------------|------------------|-------------------|
| Cube (Hexaèdre)       | 6               | 12               | 8                 |
| Sphère (maitresse)             | 1|0|0 |
| Sphère (ballon)             | 1|0|1 |
| Cercle|0|1|1|



