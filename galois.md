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



# Correspondance galoisienne
<!-- _transition: glow -->
greg mc shane

# 

**Hatcher Chapitre 1.3 pp 63-68**


#

- **Théorème de l’injectivité**  
Soit $p : (E, x_0) \to (B,b_0)$ un revêtement. 
    - L’application induite $p_∗ : \pi_1(E, x_0) \to \pi_1(B, b_0)$ est injective. 
    - Le sous-groupe image $p_∗(\pi_1(E, x_0))$ est
constitué des classes de lacets de B, basés en $b_0$, 
et dont les relèvements sont des lacets de E.


# 


- La correspondance galoisienne naît de la fonction qu'attribue à chaque espac e couvrant p
$(\tilde{X}, \tilde{x_0})\to(X, x_0$)$ le sous gpe $p_∗(\pi_1(\tilde{X}, \tilde{x_0}) < \pi_1(X,x_0)$

- Cette fonction est-elle surjective ? Autrement dit, nous demandons 
si chaque sous-groupe de $\pi_1(X,x_0)$ est réalisé comme $p_∗(\pi_1(\tilde{X}, \tilde{x_0})$ pour un revetement p
- En particulier, est-ce que le sous-groupe trivial réalisé. 
Puisque $p_∗$ est toujours injectif, cela revient à se demander si X possède un espace de recouvrement simplement connexe. 

#   


<!-- Une condition nécessaire pour que X ait un revêtement simplement connexe --> 

- Définition : **semilocalement simplement connexe** : 
Chaque point x ∈ X a un voisinage U tel que l'application induite par l'inclusion $U ↪ X$, $\pi_1(U, x)→\pi_1(X, x)$ est triviale 

- Supposons que $p : \tilde{X} \to X$ soit un revêtement avec $\tilde{X}$ simplement connexe. 
- Tout point x ∈ X possède un voisinage U ayant une revetement $\tilde{U } ↪ \tilde{X}$ et la restriction $p: \tilde{U} \to U$ est un homéomorphisme.
- le relevé d'un lacet $\gamma\subset U$ est nul homotopique dans $\tilde{X}$ puisque $\pi_1(\tilde{X}) = 0$ ie $\exists \tilde{H}$ une homotopie entre $\tilde{\gamma}$ et une application constante. La composition $p\circ \tilde{H}$ est une homotopie
entre $\gamma$ et une application constante dans U.

#

- A locally simply-connected space is certainly semilocally simply-connected. For example, CW complexes have the much stronger property of being locally contractible, as Hatcher shows in the Appendix. 

- An example of a space that is not semilocally simplyconnected is the shrinking wedge of circles, the subspace $X ⊂ \mathbb{R}$ consisting of the circles of radius 1/n centered at the point ( 1/n, 0) for n = 1, 2, ···,. 
- On the other hand, if we take the cone CX = (X×I)/(X× {0}) on the shrinking wedge of circles, this is semilocally simply-connected since it is contractible, but it is not locally simply-connected

#

### Construction

- Soit X 
    - connexe par arcs, 
    - localement connexe par arc 
    - semilocalement simplement connexe

#

### Construction

- Soit X connexe par arcs, localement connexe par arc et semilocalement simplement connexe
- **Observation :**
    - classes d'homotopie des chemins $\gamma \in L(X, x_0)$
    - = classes d'homotopie des chemins $\tilde{\gamma} \in L(\tilde{X}, \tilde{x_0})$
- $\tilde{X} = \{(x, [\gamma]) | x \in X, \gamma \in L(X, x_0), \gamma(0) = x_0\}$
- [γ] =  la classe d'homotopie de γ par rapport aux homotopies qui fixent les points terminaux γ(0) et γ(1).

- La fonction $p : \tilde{X}\to X,\,[γ] \mapsto  γ(1)$ est bien définie. X est connexe par arcs, γ(1) peut être n'importe quel point de X , donc p surjectif.


#

- Notons
$\mathcal{U} := \{ U \subset X,\,\text{ ouvert, connexe par arcs et } \pi_1(U) ↪ \pi_1(X) \text{ trivial} \}$


- Si l'application $p_{*} : \pi_1(U, x)→\pi_1(X, x)$ est triviale pour un point x ∈ U , alors elle l'est pour tout point y ∈ U.
- Si $V\subset U$ est un ouvert connexe par arcs alors $V\in
\mathcal{U}$.
- Il s'ensuit que $\mathcal{U}$ est une base pour la topologie sur X si X est localement connexe par arcs  et semilocalement simplement connexe.
- **Rappel :**  une base d'une topologie est un ensemble d'ouverts tel que tout ouvert de la topologie soit une réunion d'éléments de cet ensemble.

#

- Soit $U ∈ \mathcal{U}$ et un chemin γ dans X de $x_0 \in U$ 
    - $U_{[\gamma]} := \{ [\gamma.\eta],\, \eta \text{ un chemin} \subset U, \eta[0]= \gamma(1) \}$
- $p : U_{[γ]} \to U$ est surjectif puisque U est connexe par arcs
-  injectif puisque différents choix de η joignant γ(1) à un x ∈ U fixe sont tous homotopes dans X
- $U_{[\gamma]}= U_{[\gamma']}$ if $[\gamma']\in U_{[\gamma]}
  $ 
- si $\gamma' = \gamma\cdot \eta$ alors les éléments de $U_{[\gamma']}$ 
ont la forme $[\gamma'\cdot \eta \cdot \mu]$ donc $U_{[\gamma']}\subset U_{[\gamma]}$
- de meme $[\gamma\cdot\mu]= [\gamma\cdot\eta\cdot\bar{\eta}\cdot\mu]= [\gamma'\cdot\bar{\eta}\cdot\mu]\in U_{[\gamma]}$

#

- $\mathcal{U}$ est une base de la topologie sur $\tilde{X}$, 

- Soient $U_{[\gamma]}, V_{[\gamma']}$ $[\gamma'']\in U_{[\gamma]} \cap V_{[\gamma']}$,
alors $U_{[\gamma]} =  U_{[\gamma'']}$ et $V_{[\gamma']} =
V_{[\gamma'']}$
- Donc si $W\in \mathcal{U}, \gamma''(1)\in W \subset U \cap V$ 
alors $W_{[\gamma'']} \subset  U_{[\gamma'']}\cap V_[\gamma'']$ et $[\gamma''] \in  W_{[\gamma'']}$

