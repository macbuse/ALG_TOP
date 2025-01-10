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

# Plan

- [Caractéristique d'Euler](#caractéristique-d'Euler)
- Indice d'un point par rapport à un lacet
- Revetements
- Groupes, homologie et homotopie

# La mauvaise réponse de la maitresse

- [caractéristique d'Euler](https://analysis-situs.math.cnrs.fr/-Caracteristique-d-Euler-Poincare-92-.html)
- **solides de platoniciens** avec les éléments classiques selon le *Timée* de Platon   

[the 5 elements according to the Timaeus](https://en.wikipedia.org/wiki/Timaeus_(dialogue)#The_elements)


# 

| **Solide**     | **Élément**    | **Description**                                              | **Faces** | **Faces**       | 
|--------------------------|----------------|--------------------------------------------------------------|-----------|---------------------------|
| **Tétraèdre**             | Feu            | Pointu et énergique                 | 4         | Triangle équilatéral       | Transformation, énergie et chaleur             |
| **Cube (Hexaèdre)**       | Terre          | Solide et immuable | 6         | Carré                      |
| **Octaèdre**              | Air            | Léger, mobile,  | 8         | Triangle équilatéral       | 
| **Icosaèdre**             | Eau            | Fluide, coulant et adaptable | 20        | Triangle équilatéral       | 
| **Dodécaèdre**            | Éther (ou Cosmos) | Représentant l’univers et les cieux                        | 12        | Pentagone régulier         | 

# Notes supplémentaires :
- **L’éther** (ou **aether**) était souvent considéré comme le « cinquième élément » ou la **quintessence**, représentant la substance des sphères célestes et du divin.  
- Le **nombre de faces** et leurs propriétés symétriques rendaient ces solides uniques et leur donnaient des correspondances avec les caractéristiques des éléments.  
- Le **dodécaèdre** était particulièrement mystique pour les Grecs, car il symbolisait l’ensemble du cosmos.


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

- La caractéristique d'Euler $\chi$ est une **invariante topologique** des polyèdres convexes et d'autres objets géométriques. 


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
| Sphère (carte)             | 2|1|1 |
| Cercle|0|1|1|

#

<img src="./balloon.webp" width="600">

# Craster parabolic

<img src="https://upload.wikimedia.org/wikipedia/commons/9/9c/Craster_parabolic_projection_SW.jpg" width="1000">


#
## indice d'un point par rapport à un lacet

![](./Winding_Number_Around_Point.svg)


# Definition et formule

Le **indice** d’une courbe fermée $\gamma$ autour de l’origine $(0, 0)$ 
est défini comme le nombre de fois que la courbe s’enroule 
autour de l’origine dans le sens antihoraire. 

La formule pour le "nombre d’enroulements" est :

$$\text{indice} = \frac{1}{2\pi} \int_{\gamma} \frac{x \, dy - y \, dx}{x^2 + y^2}$$


#

- $\gamma$ est donnée sous forme paramétrique par 
- $\gamma(t) = (x(t), y(t))$ pour $t \in [a, b]$, 

<!-- | | -->
<!-- |-------------------------------------| --> 
<!-- |$\text{indice} = \frac{1}{2\pi} \int_{a}^{b} \frac{d\theta(t)}{dt} \, dt$| -->

 $$\text{indice} = \frac{1}{2\pi} \int_{a}^{b} \frac{d\theta(t)}{dt} \, dt$$

où $\theta(t) = \tan^{-1}\left(\frac{y(t)}{x(t)}\right)$ est l’angle polaire du point $(x(t), y(t))$.

$$\frac{d}{dt}\theta(t) =\frac{d}{dt} \tan^{-1}\left(\frac{y(t)}{x(t)}\right) =  \frac{x \dot{y} - y \dot{x}}{x^2 + y^2}$$

#

- $\gamma$ est un cercle de centre l'origine, de rayon $R>0$
- $\gamma(t) = R(\cos(t),\sin(t))$ pour $t \in [0,2\pi]$, 
- $\gamma'(t) = (\dot{x},\dot{y}) = R(-\sin(t),\cos(t))$ 


 $$\frac{d}{dt}\theta(t) =  \frac{x \dot{y} - y \dot{x}}{x^2 + y^2} =
\frac{\cos^2(t) + \sin^2(t)}{\cos^2(t) + \sin^2(t)} = 1$$


$$\Rightarrow \text{indice} = \frac{1}{2\pi} \int_{0}^{2\pi} 1\, dt  = 1$$

# 

[animation](https://commons.wikimedia.org/wiki/File:Winding_Number_Animation_Small.gif?uselang=fr)

# 

L'origine de l'indice est une lettre de Gauss à un ami, 
le
mathématicien allemand Bessel:

$$\int_1^z \frac{dw}{w} = \log(z) = \log(|z|) + i\arg(z)$$
<!-- $$\gamma(t) = x(t) + iy(t)$$ --> 

<!-- $$ -->
<!-- \text{indice} = \frac{1}{2\pi i} \int_{a}^{b} \frac{\gamma'(t)}{\gamma(t)} \, dt -->
<!-- $$ -->

<!-- où $\gamma'(t)$ désigne la dérivée de $\gamma(t)$ par rapport à $t$. -->

Cette dernière forme est souvent utilisée en analyse complexe. Elle calcule combien de fois la courbe entoure l’origine en intégrant la dérivée logarithmique de la fonction complexe le long de la courbe.
