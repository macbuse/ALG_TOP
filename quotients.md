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

# Quotients II

#

<!-- _transition: slide -->
## 4 types d'espaces quotients

1. quotient par un sous ensemble $A \subset Y$.
1. recollement de $X$ à $Y$ le long de $f$.
1. quotient par un groupe d'homéomorphismes.
1. suspension d'un homéomorphisme.


#

<!-- _transition: slide -->
### Exemple : action d'un groupe

<!-- Propriété bis (rappel).– Si Y est relativement compact et -->
<!-- la relation d’équivalence ∼ fermée alors Y/∼ est séparé. -->

- Soient $X$ un espace muni d'une action d'un groupe $G$ 
par homéomorphisme. L'action est :

- **libre** si pour tout $x \in X$,
$g \in G$ on a $g \neq e \Rightarrow g.x \neq x$.
- **propre** si pour tout compact $K \subset X$,
l'ensemble $\{g \in G, g.K \cap K \neq \emptyset\}$ est compact (fini).
- **l'orbite de $x$ sous $G$** est noté $G\cdot x := \{g.x, g \in G\}$.
- **les orbites de l'action** noté $G/X$ est l'espace quotient de $X$ par $G$.

#

<!-- _transition: slide -->
- L’espace quotient Y/∼ n’est pas nécessairement séparé.
- Un espace topologique est dit **séparé** si tout couple de
points distincts admet des voisinages disjoints.
- Le **saturé** d’un ensemble F ⊂ Y est l’ensemble
$p^{-1}(p(F))$, c’est-à-dire tous les points de Y qui sont en
relation par ∼ à un point de F.
- La relation d’équivalence ∼ est dite **fermée** si le saturé
de toute partie fermée est fermée.

| Propriété |
|---|
| Si Y est compact et la relation d’équivalence ∼ fermée <br> alors Y/∼ est séparé.|

#

<!-- _transition: cube -->
| Propriété |
|---|
| Si Y est compact et la relation d’équivalence ∼ fermée <br> alors Y/∼ est séparé.|

**Exemples**

- $H < G$ un sous-groupe fermé de $G$ 
 $x \sim y  \Leftrightarrow x^{-1}y \in H$
alors $G/H$ est séparé.
- $\mathbb{R}/\mathbb{Z} = \mathbb{S}^1$ est séparé.
- $\mathbb{R}^n/\mathbb{Z}^n = \mathbb{T}^n$ est séparé.
- $\mathbb{R}/\mathbb{Q}$ n'est pas séparé.

# Le cercle $\mathbb{S}^1$

- Soit Y = [0, 1] et ∼ la relation d’équivalence définie par
    - x ∼ y ⇔ x = y ou x = 0 et y = 1 ou x = 1 et y = 0.

| proposition |
|---|
| L’espace quotient Y/∼ est homéomorphe au cercle $\mathbb{S}^1$.|

- **Démonstration.** L’application $f : Y \rightarrow    \mathbb{S}^1$ définie par 
f(x) = exp(2iπx) est continue et constante sur les classes
d’équivalence. Elle induit donc une application continue.


# Ruban de Möbius

<!-- _transition: cube -->
<!-- -  l'anneau $X = \{ z \in \mathbb{C}, 1/2 \leq |z| \leq  2\}$ --> 
<!-- est un revêtement double du ruban de Möbius --> 
<!-- - $G = \langle  z\mapsto 1/z \rangle$ est un groupe de homéomorphismes de $X$. -->

- bande $X = \{-1 < \text{Im }(z) < 1\}\subset \mathbb{C}$ (pas un groupe)
- $G = \langle g:z \mapsto \bar{z} + 2\pi  \rangle$ est un groupe de homéomorphismes de $X$.
    - $X/G$ est un ruban de Möbius 
    - $X/H,\,H= \langle g^2 \rangle$ un cylindre.
- take a paper strip and twist it once before joining the ends.

$$
\begin{matrix}
  X &  &  \\
  \downarrow{p_H} & \searrow{p_G}  &\\ 
 X/H  \xrightarrow{\bar{p}} & X/G
\end{matrix}
\;p_G = \bar{p}\circ p_H$$  

# 
#### My mother's mirrors
<!-- _transition: cube -->
![bg left](https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Kneeling_for_Infinity_%28Self-portrait%29.jpg/800px-Kneeling_for_Infinity_%28Self-portrait%29.jpg)

- The infinity mirror (also sometimes called an infinite mirror) is a configuration of two or more parallel or angled mirrors, which are arranged to create a series of smaller and smaller reflections that appear to recede to infinity.
    - [wiki](https://en.wikipedia.org/wiki/Infinity_mirror)
    - [flat universe](https://www.youtube.com/watch?v=QcLfb0PhfO0&t=623s)

#


- **Proposition de transfert de continuité au quotient.**
Soit f : Y → Z une application continue telle que 
pour tout $(y_1, y_2) \in Y$  on ait $y_1 ∼ y_2 \Rightarrow   f(y_1) = f(y_2)$
Alors l’application $\bar{f} : Y/∼ \,\rightarrow   Z$ donnée par $\bar{f}([y]) = f(y)$ 
est bien définie et continue.



$$
\begin{matrix}
  Y & &  \\
  \downarrow{\pi} & \searrow{f}  &\\ 
Y / \sim & \xrightarrow{\bar{f}} & Z
\end{matrix}
\;f = \bar{f}\circ \pi$$  

#

- **Démonstration.** Le caractère bien défini provient du fait
que f est constante sur chaque classe d’équivalence.
- Soit U un ouvert de Z. L’image réciproque $\bar{f}^{-1}(U) \subset Y/~$ est  ouvert  si et seulement si $\pi^{−1}(\bar{f}^{−1}(U)) \subset Y$ est ouvert. 
Or par construction $f = \bar{f}\circ \pi$  :
$$\pi^{−1}(\bar{f}^{−1}(U)) = (\bar{f}\circ \pi)^{−1}(U) = f^{−1}(U)$$
- est **ouvert** car f **continue**. $\Box$

# Exercices

1. Démontrer la proposition : 

| Propriété |
|---|
| Si Y est compact et la relation d’équivalence ∼ fermée <br> alors Y/∼ est séparé.|


#

Pour les courbes dans la figure ci-dessous, 
1. dire si l'application $z \mapsto |z|$ est un revetement sur lecercle.
1. si oui calculer le degré 

![degree height:400](./IMAGES/degrees.png)

#

- Un graphe est le donnée d'un ensemble de sommets $V$ et d'un
ensemble d'arêtes $E$.
Soient $p:\tilde{X} \rightarrow X$ un revêtement ou $X$ est une surface (tore, sphere, bouteille de Klein etc) et $\Gamma\subset X$ un graphe plongé dans $X$ de sorte que le complementaire de $\Gamma$ dans $X$ est une réunion de disques ouverts.

- Justifier la formule suivante :

$$\chi(\tilde{X}) = \text{degré de p} \times \chi(X)$$

#

Regarder les vidéos suivantes :

1. [crosscap video](https://www.youtube.com/watch?v=gx7P8lf6JXQ)

1. [crosscap](https://www.youtube.com/watch?v=RV-0uao7RdY)


#

![bg left height:600](./square_identifications.png)

- Calculer le caractère d'Euler du carré avec les identifications.

- On admet que le premier carré avec les identifications est
homéomorphe à un tore.

- Quelle est la nature topologique du second carré avec les
identifications ? et du troisième ?




# Bibliographie

- [prove me wrong](https://prove-me-wrong.com/mathematical-art/math-visualization-portfolio/)


