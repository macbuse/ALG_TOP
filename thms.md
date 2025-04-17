

- **Proposition de transfert de continuité au quotient.**
Soit f : Y → Z une application continue telle que 
pour tout $(y_1, y_2) \in Y$  on ait $y_1 ∼ y_2 \Rightarrow   f(y_1) = f(y_2)$
Alors l’application $\bar{f} : Y/∼ \,\rightarrow   Z$ donnée par $\bar{f}([y]) = f(y)$ 
est bien définie et continue.

---


- **Proposition.**– Deux applications $f, g : X \to \mathbb{R}^n$
 sont toujours homotopes. Autrement dit, l’ensemble $[X, \mathbb{R}^n]$ est l'unique composante connexe par arc de $C^0(X, \mathbb{R}^n)$.


 ---

- **On définit** une relation binaire $\simeq$  dans 
$C^0(X, Y)$ par $f \simeq g \Leftrightarrow$ il existe une homotopie entre f et g
- Similairement, $f \simeq_A g$ si l’homotopie est relative à A.

- **Proposition**.– Les relations $\simeq$ et $\simeq_A$ sont des relations d’équivalence.


---


- **Proposition.**– $r : X \to A$ est une rétraction par déformation
alors c'est une équivalence d'homotopie et donc $A \simeq X$.

---

- **Lemme**-  X est contractile ssi il existe 
$x_0 \in X$ telle que l’application constante 
$x \mapsto  c_X (x) = x_0$ est homotope à $id_X$.

- **Proposition.** – Si Y est contractile et si $f, g \in C^0(X, Y)$ 
alors f et g sont homotopes $f \simeq g$. 

---

- **Proposition 1.**– Soient 
$\gamma_1, \delta_1 \in L(X, x_0, x_1)$ et $\gamma_2, \delta_2 \in L(X, x_1, x_2)$. 
Alors $
(\gamma_1 \simeq_\partial \delta_1 \text{ et } \gamma_2 \simeq_\partial \delta_2) \Rightarrow \gamma_1 * \gamma_2 \simeq_\partial \delta_1 * \delta_2.
$

---

- **Notations.** 
    1. On note $c_{x_0} \in \Omega(X, x_0)$ le **lacet constant** :
$c_{x_0}(s) = x_0,\,\forall s \in [0, 1]$

    2.  Soit $\gamma \in L(X, x_0, x_1)$, on note $\bar{\gamma}$ le **chemin inversé** :
$\bar{\gamma}(s) = \gamma(1 - s),\,\forall s \in [0, 1]$

- **Proposition 2.**– Soit $\gamma \in L(X, x_0, x_1)$. 
Alors $\gamma * \bar{\gamma} \simeq_\partial c_{x_0} \text{ et } \bar{\gamma} * \gamma \simeq_\partial c_{x_1}.$


---


- **Proposition 3 .** Soient 
$\gamma_0 \in L(X, x_0, x_1)$, $\gamma_1 \in L(X, x_1, x_2)$ et $\gamma_2 \in L(X, x_2, x_3)$. 
Alors $
(\gamma_0 * \gamma_1) * \gamma_2 \simeq_\partial \gamma_0 * (\gamma_1 * \gamma_2).$

---

- **Proposition 4.**– Soit $\gamma \in L(X, x_0, x_1)$ 
Alors $\gamma * c_{x_1} \simeq_\partial \gamma \text{ et } c_{x_0} \gamma \simeq_\partial \gamma.$

---

- **Proposition 5**.– Soit $u : [0, 1] \to X$ un chemin joignant $x_0$ à $x_1$.
On note $x_0 := u(0)$ et $x_1 := u(1)$. Alors, l’application
$$\beta_u :\pi_1(X, x_0) \to \pi_1(X, x_1)$$
$$[γ] \mapsto [\bar{u} ∗ γ ∗ u]$$
- est isomorphisme de groupes.

- **Corollaire 1**.– Soient X connexe par arcs et $x_0, x_1 ∈ X$. 
Alors $\pi_1(X, x0)$ et $\pi_1(X, x1)$ sont isomorphes.
---

- Soient $f : X → Y$ une application continue,
et $x_0 ∈ X$ et $y_0 = f(x_0)$. On définit une application
$$f_* : \pi_1(X, x_0) \to \pi_1(Y, y_0)$$
$$f([\gamma]) := [f \circ \gamma].$$
- cette application est bien définie 
car si $\gamma \simeq_\partial \delta$ alors $f \circ \gamma \simeq_\partial f \circ \delta$.

- **Proposition 6.**– L’application $f_∗$ est un morphisme de
groupes.


---

- **Théorème 1.** – L’ensemble $\pi_1(X, x_0)$ muni du produit $\cdot$ est un groupe (non commutatif en général).
- **Théorème 2.**– Soient X et Y connexes par arcs. 
Si X et Y ont même type d’homotopie alors 
$\pi_1(X, x_0)$ et $\pi_1(Y, y_0)$ sont isomorphes 
pour tout choix $(x_0, y_0) ∈ X \times Y$ .


---

- **Proposition.**– Deux applications $f, g : X \to \mathbb{R}^n$
 sont toujours homotopes. Autrement dit, l’ensemble $[X, \mathbb{R}^n]$ est l'unique composante connexe par arc de $C^0(X, \mathbb{R}^n)$.

---


- **On définit** une relation binaire $\simeq$  dans 
$C^0(X, Y)$ par $f \simeq g \Leftrightarrow$ il existe une homotopie entre f et g
- Similairement, $f \simeq_A g$ si l’homotopie est relative à A.

- **Proposition**.– Les relations $\simeq$ et $\simeq_A$ sont des relations d’équivalence.

---

- **Proposition.**– $r : X \to A$ est une rétraction par déformation
alors c'est une équivalence d'homotopie et donc $A \simeq X$.

---

- **Lemme**-  X est contractile ssi il existe 
$x_0 \in X$ telle que l’application constante 
$x \mapsto  c_X (x) = x_0$ est homotope à $id_X$.

- **Proposition.** – Si Y est contractile et si $f, g \in C^0(X, Y)$ 
alors f et g sont homotopes $f \simeq g$. 
Autrement dit, l’ensemble $[X, Y]$ est un singleton.

---


- **Proposition 1.**– Soient 
$\gamma_1, \delta_1 \in L(X, x_0, x_1)$ et $\gamma_2, \delta_2 \in L(X, x_1, x_2)$. 
Alors $
(\gamma_1 \simeq_\partial \delta_1 \text{ et } \gamma_2 \simeq_\partial \delta_2) \Rightarrow \gamma_1 * \gamma_2 \simeq_\partial \delta_1 * \delta_2.$

- **Proposition 2.**– Soit $\gamma \in L(X, x_0, x_1)$. 
Alors $\gamma *\bar{\gamma} \simeq_\partial c_{x_0} \text{ et } \bar{\gamma} * \gamma \simeq_\partial c_{x_1}.$



- **Proposition 3 .** Soient 
$\gamma_0 \in L(X, x_0, x_1)$, $\gamma_1 \in L(X, x_1, x_2)$ et $\gamma_2 \in L(X, x_2, x_3)$. 
Alors $
(\gamma_0 * \gamma_1) * \gamma_2 \simeq_\partial \gamma_0 * (\gamma_1 * \gamma_2).$
- **Proposition 4.**– Soit $\gamma \in L(X, x_0, x_1)$ 
Alors $\gamma * c_{x_1} \simeq_\partial \gamma \text{ et } c_{x_0} \gamma \simeq_\partial \gamma.$


- **Proposition 5**.– Soit $u : [0, 1] \to X$ un chemin joignant $x_0$ à $x_1$.
On note $x_0 := u(0)$ et $x_1 := u(1)$. Alors, l’application
$$\beta_u :\pi_1(X, x_0) \to \pi_1(X, x_1)$$
$$[γ] \mapsto [\bar{u} ∗ γ ∗ u]$$
- est isomorphisme de groupes.

- **Corollaire 1**. Soient X connexe par arcs et $x_0, x_1 ∈ X$. 
Alors $\pi_1(X, x0)$ et $\pi_1(X, x1)$ sont isomorphes.
- **Proposition 6.** L’application $f_∗$ est un morphisme de
groupes.
- **Proposition 7.** On a $(id_X)_∗ = id_{\pi_1(X, x_0)}$ 



---



- **Théorème de l’injectivité de $p_∗$**  
Soit $p : (E, x_0) → (B,b_0)$ un revêtement. 
    - L’application induite $p_∗ : \pi_1(E, x_0) \to \pi_1(B, b_0)$ est injective. 
    - Le sous-groupe image $p_∗(\pi_1(E, x_0))$ est
constitué des classes de lacets de B, basés en $b_0$, 
et dont les relèvements sont des lacets de E.


---


- **Théorème de point fixe de Brouwer.**
Soit $f : D^n \to D^n$ une application continue.
Alors il existe $x_0 \in D^n$ tel que $f(x_0) = x_0$.
- **Lemme**
$\not \exists$ une retraction $r : D^n \to S^{n-1}$.



