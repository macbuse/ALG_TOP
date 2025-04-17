

# Définitions du cours de topologie


- **Définition.**
Le **indice** d’une courbe fermée $\gamma$ autour de l’origine $(0, 0)$ 
est défini comme le nombre de fois que la courbe s’enroule 
autour de l’origine dans le sens antihoraire. 

La formule pour le "nombre d’enroulements" est :

$$\text{indice} = \frac{1}{2\pi} \int_{\gamma} \frac{x \, dy - y \, dx}{x^2 + y^2}$$

---


- **Définition** Un polyèdre convexe est un **solide de Platon** 
si et seulement si

1. Toutes ses faces sont des polygones 
réguliers convexes isométriques
1. Aucune de ses faces ne se coupe, 
excepté sur les arêtes
1. Le même nombre de faces se rencontre 
à chacun de ses sommets.


- **Définition :** une application $f:X \to Y$ est **nul homotope** 
si il existe une homotopie $H : X \times [0,1]
\to Y$
telle que $H(x,0) = f(x)$ et $H(x,1) = c$ 
pour une constante $c$.


- **Définition.** Un espace topologique X est dit *localement
compact* 
    1. s’il est séparé 
    1. et si tout point x élément de X admet un voisinage compact (autrement dit si x appartient à un ouvert relativement compact)

---

- Soit Y un espace topologique et soit $A \subset Y$. 
On considère la relation d’équivalence suivante
$$y_1 ∼ y_2 \Leftrightarrow y_1 = y_2 \text{ ou } (y_1, y_2) \in A$$

- L’espace quotient Y/∼ est donc formé 
    - de la classe [a] où a ∈ A 
    - et des classes d’équivalence [y] avec y ∈ Y \ A.

- **Définition**.– L’espace quotient est noté Y/A et est appelé espace quotient de $Y$ par $A$.

---

- Soient X et Y deux espaces topologiques, A ⊂ Y et
f : A → X une application continue. 
On définit une relation d’équivalence ∼ 
sur la somme disjointe $Z = X \sqcup Y$ par $z_1 ∼ z_2$

- si $z_1 = z_2$
- ou $(z_1 ∈ A \text{ et } z_2 = f(z_1))$
- ou $(z_2 ∈ A \text{ et } z_1 = f(z_2))$


- **Définition**– L’espace quotient est noté $X \cup_f Y = X \sqcup Y/∼$
et s’appelle le RECOLLEMENT DE X À Y LE LONG DE f.

---

- **Définition.** Un espace topologique X est dit **localement
compact**
    1. s’il est séparé 
    1. et si tout point x élément de X admet un voisinage compact (autrement dit si x appartient à un ouvert relativement compact)

---


**Définition :**
- Une **application de revêtement** (ou **revêtement topologique**) est un type de fonction continue entre espaces topologiques qui, intuitivement, représente une version « dépliée » ou « en couches » d’un espace. 

- $p: \tilde{X} \to X$ surjective est appelée **application de revêtement** 
 si, $\forall x \in X, \exists U_x \subset X$ un voisinage ouvert (**voisinage trivialisant**) tel que $p^{-1}(U_x)$ soit une union disjointe d'ouverts de $\tilde{X}$, chacun étant envoyé **homéomorphiquement** sur $U_x$ par $p$.  

 ---


- **Définition** $X$ est connexe $\text{card}(p^{-1}(x))=$  degré du revêtement.

---

- Soit Y un espace topologique et soit $A \subset Y$. 
On considère la relation d’équivalence suivante
$y_1 ∼ y_2 \Leftrightarrow y_1 = y_2 \text{ ou } (y_1, y_2) \in A$

- L’espace quotient Y/∼ est donc formé 
    - de la classe [a] où a ∈ A 
    - et des classes d’équivalence [y] avec y ∈ Y \ A.

- **Définition**.– L’espace quotient est noté Y/A 
et est appelé **espace quotient de $Y$ par $A$.**


---

- Soient X et Y deux espaces topologiques,
$A \subset Y$ et $f : A \to X$ une application continue. 
On définit une relation d’équivalence ∼ 
sur la somme disjointe $Z = X \sqcup Y$ par $z_1 ∼ z_2$

- si $z_1 = z_2$
 ou $(z_1 ∈ A \text{ et } z_2 = f(z_1))$
 ou $(z_2 ∈ A \text{ et } z_1 = f(z_2))$


- **Définition**– L’espace quotient est noté $X \cup_f Y = X \sqcup Y/∼$
et s’appelle le **recollement de $X$ à $Y$ le long de f.**

---

- **Définition.** Soit $f : X \rightarrow X$ un homéomorphisme.
La suspension de f est l’espace quotient de $X \times [0, 1]$ 
par la relation d’équivalence ∼ définie par :
$$(x, 0) ∼ (f(x), 1)$$

---

- **Définition.**
Un **simplexe** est le type de polytope le plus simple dans une dimension donnée. Plus précisément, un simplexe est l'enveloppe convexe de  $\{ p_0,\ldots p_n\}$ points affinement indépendants dans $\mathbb{R}^n$. Il généralise la notion de triangle ou de tétraèdre à des dimensions arbitraires.

---

- **Définition.**
- Un **complexe simplicial** $K$ est une famille de simplexes
qui satisfait les deux conditions suivantes :
1. **Fermeture par faces** : Si un simplexe $\sigma \in K$, alors toutes les faces de $\sigma$ appartiennent également à $K$. Une face d’un simplexe est tout sous-ensemble de ses sommets.
2. **Propriété d’intersection** : Si deux simplexes $\sigma_1, \sigma_2 \in K$ alors, leur intersection est 
    - soit vide, 
    - soit une face commune aux deux simplexes.

- **Définition**.– Si $\sup \{\text{dim } \sigma_\alpha\} = k < +\infty$ 
on dit que K est un complexe simplicial de dimension k.

---


- **Définition.**– La donnée d’un espace topologique X et d’un
point base $x_0\in X$ est appelé un ESPACE POINTÉ et noté $(X, x_0)$.
- **Définition.**– Étant donnés deux espaces pointés 
$(X, x_0)$ et $(Y, y_0)$, on appelle BOUQUET DE X ET DE Y et 
$X \vee Y$ le recollement $X \cup_f Y$ où $A = \{y_0\}$ et $f(y_0) = x_0$
 On dit également que X ∨ Y est la SOMME POINTÉE de X
et de Y.

---

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

---

- **Définition**.– Soient X et Y deux espaces topologiques et
$f, g : X \to Y$ deux applications continues. 
Une HOMOTOPIE ENTRE f ET g est une application continue
$H : X × [0, 1] \to  Y$ telle que
    - $\forall x \in X, H(x, 0) = f(x)$
    - $\forall x \in X, H(x, 1) = g(x)$

- Soit A ⊂ X. On dit que l’homotopie H est RELATIVE À A si
de plus
    - $\forall x \in A, \forall t \in [0, 1], H(x, t) = f(x) = g(x)$

---

- **Définition.** Soit $f \in C^0 (X, Y).$ On dit que f est 
une **équivalence d’homotopie** s’il existe une application
$g \in C^0 (X, Y).$ telle que $f \circ g \simeq id_Y$ et $g \circ f \simeq id_X$ .

- Si une telle application existe, on dit 
    - que g est un **inverse homotopique** de f 
    - et que X et Y ont **même type d’homotopie**
    ou qu’ils sont **homotopiquement équivalents.** 
    - on note $X \simeq Y$.

---

- **Définition.**– Soit $i : A \hookrightarrow X$ une inclusion, $r \in C^0 (X, A)$ est 
    - une RÉTRACTION PAR DÉFORMATION si $i \circ r \simeq id_X$ 
    - une RÉTRACTION **FORTE** PAR DÉFORMATION si $i \circ r \simeq_A id_X$ .

---


- **Définition.** -  On dit qu’un espace X est CONTRACTILE s’il a le type d’homotopie d’un singleton $\{pt\}$.

---

- **Définition**.– Soit X un espace topologique et $x_0, x_1 \in X$. 
- On appelle **chemin joignant** $x_0$ à $x_1$ tout application continue 
$\gamma : [0, 1] \to X$ telle que $\gamma(0) = x_0$ et $\gamma(1) = x_1$.
- On appelle **lacet basé en** $x_0$ tout chemin tel que
$\gamma(0) = \gamma(1) = x_0$.

#

- **Notations.**– On note
    - $L(X, x_0, x_1)$ l’ensemble des chemins joignant $x_0$ à $x_1$ et
    - $\Omega(X, x_0)$ l’ensemble des lacets basés en $x_0$.

- **Définition.–** On dit qu’un espace topologique X est
**connexe par arcs** si tout couple de point 
$(x_1, x_2) \in X \times X$
peut être joint par un chemin X, autrement dit si 
$L(X, x_1, x_2)$ est non vide.

---


- On note : $\pi_1(X, x_0) := \Omega(X, x_0)/ \simeq_\partial$
et on munit cet ensemble d'un produit ” · ” par
$$[γ_1] \cdot [γ_2] := [γ_1 ∗ γ_2].$$

---


- **Définition.** Un espace topologique X est dit **simplement connexe** s’il est connexe par arcs et s’il existe 
$x_0 ∈ X$ tel que $\pi_1(X, x_0) = {[c_{x_0}]}$


---

- **Définition**.– Soient X et Y deux espaces topologiques et
$f, g : X \to Y$ deux applications continues. 
Une HOMOTOPIE ENTRE f ET g est une application continue
$H : X × [0, 1] \to  Y$ telle que
    - $\forall x \in X, H(x, 0) = f(x)$
    - $\forall x \in X, H(x, 1) = g(x)$

- Soit A ⊂ X. On dit que l’homotopie H est RELATIVE À A si
de plus
    - $\forall x \in A, \forall t \in [0, 1], H(x, t) = f(x) = g(x)$

---

- **Définition**.– Soient p un revêtement et f : Y → B une application continue. Un **relèvement** de f est toute application continue 
$\tilde{f} : Y \to E$ telle que $p \circ \tilde{f} = f.$

---


- Définition : **semilocalement simplement connexe** : 
Chaque point x ∈ X a un voisinage U tel que l'application induite par l'inclusion $U ↪ X$, $\pi_1(U, x)→\pi_1(X, x)$ est triviale 

---


