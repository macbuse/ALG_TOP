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

# blank


#

- **Définition**.– Soient X et Y deux espaces topologiques et
$f, g : X \to Y$ deux applications continues. 
Une HOMOTOPIE ENTRE f ET g est une application continue
$H : X × [0, 1] \to  Y$ telle que
    - $\forall x \in X, H(x, 0) = f(x)$
    - $\forall x \in X, H(x, 1) = g(x)$

- Soit A ⊂ X. On dit que l’homotopie H est RELATIVE À A si
de plus
    - $\forall x \in A, \forall t \in [0, 1], H(x, t) = f(x) = g(x)$
- Observons que pour qu’une telle homotopie soit possible il
faut nécessairement $f|_A = g|_A$.

#



### Homotopies d’applications

- **Proposition.**– Deux applications $f, g : X \to \mathbb{R}^n$
homotopes sont homéomorphes.
n sont toujours homotopes.

**Démonstration.** Il suffit de considérer
$$H(x, t) = t f(x) + (1 − t)g(x)$$
- Cette démonstration reste valide si les applications
$f, g : X \to Y$ ou $Y \subset R^n$ sous-espace convexe

- Si $Y$ n’est pas un sous-espace convexe
alors l’interpolation linéaire entre f et g ne fournit plus une homotopie. Il faut en chercher une autre, si elle existe.

### Homotopies d'applications

- On définit une relation binaire $\simeq$  dans 
$C_0(X, Y)$ par
$f \simeq g \Leftrightarrow$ il existe une homotopie entre f et g

Similairement, $f \simeq_A g$ si l’homotopie est relative à A.

**Proposition**.– Les relations $\simeq$ et $\simeq_A$ sont des relations d’équivalence.

**Démonstration** : Notons que $\simeq$est un cas particulier de
$\simeq_A$ avec $A = \emptyset$. On ne considère donc que $\simeq_A$.
- La relation est réflexive. Il suffit de prendre H(x, t) := f(x).
- La relation est symétrique. Si H est une homotopie
relative joignant f à g alors 
$\tilde{H}(x, t) = H(x, 1 − t)$ est une
homotopie relative joignant g à f.

#

### Transivité

-  $H_1$ est une homotopie joignant $f$ à $g$, 
-  $H_2$ est une homotopie joignant $g$ à $h$, 

On suppose que $H_1$ et $H_2$ sont définies comme suit :
$$
\quad H_1(x,t) \text{ avec } H_1(x,0) = f(x) \text{ et } H_1(x,1) = g(x)
$$
$$
\quad H_2(x,t) \text{ avec } H_2(x,0) = g(x) \text{ et } H_2(x,1) = h(x)
$$

- alors on peut construire une homotopie $H$ joignant $f$ à $h$ en **concaténant** $H_1$ et $H_2$.

### **Construction de l'homotopie $H$**
On définit $H$ sur $X \times [0,1]$ par :
$$
H(x,t) =
\begin{cases}
H_1(x, 2t), & \text{si } 0 \leq t \leq \frac{1}{2} \\
H_2(x, 2t - 1), & \text{si } \frac{1}{2} \leq t \leq 1
\end{cases}
$$
L'idée est que :
- Pour $0 \leq t \leq \frac{1}{2}$, on suit $H_1$ mais en "accélérant" le temps ($t$ est multiplié par 2).
- Pour $\frac{1}{2} \leq t \leq 1$, on suit $H_2$ en ajustant aussi le paramètre de temps.

### **Vérifications**
- $H(x,0) = H_1(x,0) = f(x)$ ✅
- $H(x,1) = H_2(x,1) = h(x)$ ✅
- $H(x,\frac{1}{2}) = H_1(x,1) = g(x) = H_2(x,0)$, donc la transition entre $H_1$ et $H_2$ est bien continue ✅

#

-**Définition.**– Soit 
$f \in C^0 (X, Y).$ On dit que f est une
ÉQUIVALENCE D’HOMOTOPIE s’il existe une application
$g \in C^0 (X, Y).$ telle que
$f \circ g \simeq id_Y et g \circ f \simeq id_X$ .

Si une telle application existe, on dit g est un INVERSE
HOMOTOPIQUE DE f et que X et Y ont MÊME TYPE
D’HOMOTOPIE ou qu’ils sont HOMOTOPIQUEMENT
ÉQUIVALENTS. On note $X \simeq Y$.

Exemple 1.– L’espace $\mathbb{R}^n$ 
 et le singleton $\{O\} \subset \mathbb{R}^n$ ont
même type d’homotopie : l’inclusion 
$i : {O} \hookrightarrow \mathbb{R}^n$ est une équivalence
d’homotopie dont un inverse homotopique est
l’application constante 
$r : \mathbb{R}^n \to {O}$ telle que $r(x) = O$.


Exemple 2.– Les espaces $\mathbb{R}^n \setminus \{O\}$ et $S^{n−1}$
ont
même type d’homotopie : l’inclusion 
$i : S^{n−1} \hookrightarrow \mathbb{R}^n \setminus \{O\}$ est une
équivalence d’homotopie dont un inverse homotopique
est l’application 
$r : \mathbb{R}^n \setminus \{O\} \to S^{n−1}$ telle 
que $r(x) = \frac{x}{||x||}$.


.
# Rétractions
**Définition.** -  On dit qu’un espace X est CONTRACTILE s’il a
le type d’homotopie d’un singleton {pt}.


## Exemples.

Exemples.– Les domaines étoilés sont contractiles, en
particulier les domaines convexes et les cônes.


**Lemme**-  X est contractile ssi il existe 
$x_0 \in X$ telle que
l’application constante 
$x \to  cX (x) = x_0$ est homotope à $id_X$.

**Démonstration**. – 
X contractile signifie qu’il existe 
$x_0 \in X$ telle que
l’inclusion $i : \{x_0\} \to X$ est une équivalence
d’homotopie.



# Homotopie et rétractes


1) On suppose que X et Y sont homéomorphes. Montrer
qu’ils ont même type d’homotopie. Réciproque ?
2) 
- a) Soit [a, b] un segment de R. Montrer que [a, b] est un
rétract de R.

- b) Soit X un espace topologique (séparé), montrer que la
diagonale
∆X = {(x, x)| x ∈ X} ⊂ X × X
est un fermé de X × X.
- c) Soit r : X → X une rétraction sur A ⊂ X. Montrer que
l’ensemble de coïncidence S de idX et de r :
S = {x ∈ X | r(x) = idX (x)}
est un fermé de X.
- d) En déduire que A est un fermé de X.
- e) Montrer que ]a, b[ n’est le rétract d’aucun intervalle le
contenant strictement.
