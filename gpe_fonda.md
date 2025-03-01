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



# Homotopie
<!-- _transition: glow -->
greg mc shane

# 

**Hatcher Chapitre 0**

1. $X$ espace topologique, separé,  connexe par arcs, localement compact.
1. $\pi_1(X, x_0) := \Omega(X, x_0)/ \simeq_\partial = 
\text{lacets}/\text{homotopie}$
    1. $\tilde{X}$ espace recouvrant universel de $X$
    1. $X = \tilde{X}/\pi_1(X, x_0)$


#


### La concaténation des chemins
- **Définition**.– Soit X un espace topologique et 


$x_0, x_1 \in X$.
On appelle CHEMIN JOIGNANT 
$x_0$ À $x_1$ tout application
continue $\gamma : [0, 1] \to X$ telle que
$\gamma(0) = x_0$ et $\gamma(1) = x_1$.
On appelle LACET BASÉ EN $x_0$ tout chemin tel que
$\gamma(0) = \gamma(1) = x_0$.
Notations.– On note
$L(X, x_0, x_1)$ l’ensemble des chemins joignant $x_0$ à $x_1$ et
$\Omega(X, x_0)$ l’ensemble des lacets basés en $x_0$.


#


 - Sur ces espaces, on note $\simeq_\partial$ la relation d’**homotopie pointée,** c’est-à-dire que 
$\gamma_1 \simeq_\partial \gamma_2$ signifie qu’il existe une
homotopie $H : [0, 1] \times [0, 1] \to X$ telle que
$\forall t \in [0, 1], H(0, t) = x_0$ et $H(1, t) = x_1$
et $H(s, 0) = \gamma_1(s)$ et $H(s, 1) = \gamma_2(s)$.



#

Soit
$x_0, x_1, x_2 \in X$. Si $\gamma_1 : [0, 1] \to X$ est un chemin de
$x_0$ à $x_1$ et $\gamma_2 : [0, 1] \to X$ est un chemin de $x_1$ à
$x_2$, alors la concaténation de $\gamma_1$ et $\gamma_2$ est le
chemin $\gamma_2 * \gamma_1 : [0, 1] \to X$ défini par
$$
\gamma_2 * \gamma_1(t) = \begin{cases}
\gamma_1(2s) & \text{si } 0 \leq s \leq \frac{1}{2}, \\
\gamma_2(2s-1) & \text{si } \frac{1}{2} \leq s \leq 1.
\end{cases}
$$

**Proposition 1.**– Soient 
$\gamma_1, \delta_1 \in L(X, x_0, x_1)$ et
$\gamma_2, \delta_2 \in L(X, x_1, x_2)$. alors
$$
(\gamma_1 \simeq_\partial \delta_1 \text{ et } \gamma_2 \simeq_\partial \delta_2) \Rightarrow \gamma_1 * \gamma_2 \simeq_\partial \delta_1 * \delta_2.
$$

#

- **Proposition 1.**– Soient 
$\gamma_1, \delta_1 \in L(X, x_0, x_1)$ et
$\gamma_2, \delta_2 \in L(X, x_1, x_2)$. alors
$$
(\gamma_1 \simeq_\partial \delta_1 \text{ et } \gamma_2 \simeq_\partial \delta_2) \Rightarrow \gamma_1 * \gamma_2 \simeq_\partial \delta_1 * \delta_2.
$$

- **Démonstration**.– Soient 
$H_1$ (resp. $H_2$) l’homotopie entre $\gamma_1$
et $\gamma_2$ (resp. entre $\delta_1$ et $\delta_2$). L’application

$$
H(s, t) = \begin{cases}
H_1(2s, t) & \text{si } s \in [0, \frac{1}{2}], \\
H_2(2s - 1, t) & \text{si } s \in [\frac{1}{2}, 1]
\end{cases}
$$

définit une homotopie entre $\gamma_1 * \gamma_2$ et $\delta_1
* \delta_2$. $\blacksquare$

#


**Notations.** 

1. On note 
$c_{x_0} \in \Omega(X, x_0)$ le lacet constant
$$\forall s \in [0, 1], c_{x_0}(s) = x_0$$
2.  Soit 
$\gamma \in L(X, x_0, x_1)$, on note $\bar{\gamma} le chemin
$$\forall s \in [0, 1], \bar{\gamma}(s) = \gamma(1 - s)$$


#

### Inverses de chemins


- **Proposition 2.**– Soit 
$\gamma \in L(X, x_0, x_1)$. alors
$$\gamma * \gamma^- \simeq_\partial c_{x_0} \text{ et } \gamma^-
* \gamma \simeq_\partial c_{x_1}.$$


- **Démonstration**.– L’application 

$$H(s, t) = \begin{cases}
\gamma(2s) & \text{si } s \leq \frac{1}{2} - \frac{t}{2}, \\
\gamma(2 - 2s) & \text{si } s \geq \frac{1}{2} + \frac{t}{2}
\end{cases}$$

définit une homotopie entre $\gamma * \gamma^-$ et $c_{x_0}$.
$\blacksquare$

#

### Associativité de la concaténation

- **Proposition 3 .** Soient 
$\gamma_0 \in L(X, x_0, x_1)$, $\gamma_1 \in L(X, x_1, x_2)$ et
$\gamma_2 \in L(X, x_2, x_3)$. alors
$$
(\gamma_0 * \gamma_1) * \gamma_2 \simeq_\partial \gamma_0 * (\gamma_1 * \gamma_2).$$

Démonstration.– L’application 
$H: [0, 1] \times [0, 1] \to X$ définie par

$$
H(s, t) = \begin{cases}
\gamma_0(2s) & \text{si } s \leq \frac{1}{2} - \frac{t}{4}, \\
\gamma_1(4s - t - 1) & \text{si } \frac{1}{2} - \frac{t}{4} \leq s
\leq \frac{1}{2} + \frac{t}{4}, \\
\gamma_2(4s - t - 2) & \text{si } s \geq \frac{1}{2} + \frac{t}{4}
\end{cases}
$$
est une homotopie entre $(\gamma_0 * \gamma_1) * \gamma_2$
et $\gamma_0 * (\gamma_1 * \gamma_2)$. $\blacksquare$

#

### elément neutre

- **Proposition 3.**– Soient 
$\gamma \in L(X, x_0, x_1)$ alors
$$\gamma * c_{x_1} \simeq_\partial \gamma \text{ et } c_{x_0}
* \gamma \simeq_\partial \gamma.$$

On va démontrer la première égalité
<!-- l’autre étant similaire. -->

- **Démonstration.** L’application 
$H: [0, 1] \times [0, 1] \to X$ définie par 

$$H(s, t) = \begin{cases}
\gamma_0(\frac{2s}{t+1}
) & \text{si } s \in [0,\frac{t+1}{2}], \\
x_1 & \text{si } s \in [\frac{t+1}{2}, 1]
\end{cases}$$
est une homotopie entre $(\gamma * c_{x_1})$ et $\gamma$

D’après la proposition 2 :

$c_{x_0} * \gamma \simeq_\partial \gamma^- * \gamma
\simeq_\partial c_{x_1} * \gamma \simeq_\partial \gamma$

D’après la proposition 3:
$$\gamma * c_{x_1} 
\simeq_\partial \gamma *( {\bar{\gamma}*\gamma}) 
\simeq_\partial (\gamma * {\bar{\gamma})*\gamma} 
\simeq_\partial  c_{x_0} * \gamma \simeq_\partial \gamma$$


# Le groupe fondamental

#

###  Définition

- On note : 
$$\pi_1(X, x_0) := \Omega(X, x_0)/ \simeq_\partial$$

et on munit cet ensemble d'un produit ” · ” par
$$[γ_1] \cdot [γ_2] := [γ1 ∗ γ2].$$

-  La **Proposition 1** montre que ce produit est bien défini, il
ne dépend pas des éléments choisis pour représenter
chaque classe.

#

$$\pi_1(X, x_0) := \Omega(X, x_0)/ \simeq_\partial$$

- **Théorème 1.** – L’ensemble 
$\pi_1(X, x_0)$ muni du produit · est un groupe (non commutatif en
général).

- **Démonstration**.– 
    - **Proposition 4** montre que l’élément
neutre est la classe $[c_{x_0}]$ du lacet constant. 
    -  **Proposition 2**
que tout élément $[γ]$ a pour inverse $[\bar{γ}]$ 
    - **Proposition 3** l’associativité.



