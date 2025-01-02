<!--
theme: gaia
class: gaia lead
headingDivider: 1
paginate: true
header: NUS SINGAPORE 2024
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

# Surface automorphisms and elementary number theory
<!-- _transition: glow -->
greg mc shane


<!-- # -->
<!-- <!-1- _transition: cube -1-> -->
<!-- - slides : google **greg mcshane github** -->
<!-- - click on **serfest** -->
<!-- - if there is a bug in my slides blame [this guy](https://github.com/yhatt) -->


#

- elementary number theory (Fermat, Markoff, Button)
- hyperbolic geometry (Farey, Ford, Penner)
- try not to talk about continued fractions



* some is joint work with V. Sergiescu
* $\Gamma = \mathrm{PSL}(2,\mathbb{Z})$ two index 6 subgroups
* $\Gamma(2) = \ker (\Gamma →\mathrm{PSL}(2,\mathbb{Z}/2\mathbb{Z})) \simeq \mathbb{Z}*\mathbb{Z}$
* $\Gamma' = [\Gamma,\Gamma] = \ker (\Gamma →\mathbb{Z}/6\mathbb{Z})\simeq \mathbb{Z}*\mathbb{Z}$ 
* $\mathbb{H}/\Gamma(2) =$ three punctured sphere, automorphisms $\simeq \mathfrak{S}_3$
* $\mathbb{H}/\Gamma' =$ modular torus, automorphisms $\simeq \mathbb{Z}/6\mathbb{Z}$ 

# Problem 0

![w:330](../shoulder.jpg)

# Problem 1
<!-- _transition: slide -->
**Markoff numbers** are integers that appear a **Markoff triple** 
$$(1,1,1),(1,2,1),(2,5,1),(5,13,1)$$
which are solutions of a Diophantine equation 
the so-called **Markoff cubic**

* $$x^2 + y^2 + z^2 - 3x y z = 0.$$


<!-- # --> 
<!-- _transition: wipe -->
<!-- ## infinity of Markoff triples: $z=1$ -->

<!-- $\begin{pmatrix} 3 & -1 \\ 1 & 0 \end{pmatrix}$ -->
<!-- is an automorph of --> 
<!-- $$x^2 + y^2  - 3x y.$$ -->

<!-- So $( v_n,v_{n+1},1)$ is a Markoff triple where -->

<!-- $\begin{pmatrix} x \\ y \end{pmatrix}=  \begin{pmatrix}v_{n+1} \\ v_n \end{pmatrix} = \begin{pmatrix} 3 & -1 \\ 1 & 0 \end{pmatrix}^n \begin{pmatrix}1 \\ 1 \end{pmatrix}$ -->

#
### Odd index Fibonacci numbers are Markoff numbers
<!-- _transition: slide -->
$1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181 \ldots$

$(1,1,1),(1,2,1),(2,5,1),(5,13,1),(13,34,1),(34,89,1)$

<!-- # -->
<!-- ### Odd index Pell numbers are Markoff numbers -->
<!-- <!-1- _transition: cube -1-> -->
<!-- $0, 1, 2, 5, 12, 29, 70, 169, 408, 985, 2378, 5741, 13860,\ldots$ -->

<!-- $(1,5,2), (5,29,2),(29,169,2)\ldots$ -->

#

### Odd index Fibonacci numbers are sums of squares

<!-- _transition: cube -->
<!-- https://oeis.org/A000057 -->

 $F_{2n+1} = F_{n+1}^2 + F_n^2$


<!-- and satisfy divisibility relations -->

 <!-- $F_{2n} = (F_{n+1} + F_{n-1})F_n \Rightarrow F_n | F_{2n}$ -->

<!-- $\begin{pmatrix} -->
<!-- F_{n+1} & F_{n} \\ -->
<!-- F_{n} & F_{n-1} --> 
<!-- \end{pmatrix} -->
<!-- = \begin{pmatrix} -->
<!-- 1 & 1\\ -->
<!-- 1 & 0 -->
<!-- \end{pmatrix}^n \Rightarrow -->
<!-- \begin{pmatrix} -->
<!-- F_{2n+1} & F_{2n} \\ -->
<!-- F_{2n} & F_{2n-1} --> 
<!-- \end{pmatrix}= -->
<!-- \begin{pmatrix} -->
<!-- F_{n+1} & F_{n} \\ -->
<!-- F_{n} & F_{n-1} --> 
<!-- \end{pmatrix}^2$ -->




#
<!-- _transition: slide -->
### Frobenius uniqueness conjecture

The largest integer in a triple determines the two other numbers.

- Only partial results
- m = Markoff number =  z > y > x 

* Jack Button for [m prime](https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/S0024610798006292)
* Zhang [An elementary proof...](https://arxiv.org/abs/math/0606283)
* Lang, Tan [A simple proof....](https://arxiv.org/abs/math/0508443)
* Baragar [m, 3m - 2, 3m + 2 prime](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/88B0E426FFCBEA8B3A345C1074B8CC59/S0008439500018828a.pdf/on-the-unicity-conjecture-for-markoff-numbers.pdf)
<!-- * [ Bugeaud, Reutenauer, Siksek](https://core.ac.uk/download/pdf/82088222.pdf) -->
<!-- * Conclusion too hard!!! -->


# Problem 2:
<!-- _transition: cube -->

## Give a geometric proof of


<!-- **Theorem (Fermat)** -->

 If $p$ an odd prime and 4 divides $p − 1$ then 
$p=c^2 + d^2$ for coprime integers $c,d$.

<!-- * Button's theorem follows from "unicity" of $c,d$ -->
<!-- * unique factorisation $p = (ci+d)(-ci+d)\in \mathbb{Z}[i]$ -->
#
<!-- _transition: slide -->
## References etc


- First proof Euler (reciprocity, descent)
- Heath-Brown, Fermat’s two squares theorem. Invariant (1984) 
- Zagier, A one-sentence proof that every prime p = 1 (mod 4) is a sum of two squares, 1990
- Dolan, S.,  A very simple proof of the two-squares theorem, Math Gaz, 106(564). (2021) [text](https://www.cambridge.org/core/journals/mathematical-gazette/article/abs/10538-a-very-simple-proof-of-the-twosquares-theorem/D0CB1CB39CBA0E98905401EA21DCB743)
- Elsholtz, Combinatorial Approach to Sums of Two Squares and Related Problems.  (2010) 

#
## Zagier: one sentence

<!-- _transition: glow -->
![w:1200](./zagier.png) 


# Reciprocal arcs
<!-- _transition: cube -->
![bg left 55%](./ptorusx.svg)

* modular torus = quotient of $\mathbb{H}$ by  $\Gamma'< \text{PSL}(2, \mathbb{Z})$
* pair of ideal triangles glued up
* elliptic involution swaps triangles fixes midpoint of diagonal arc
* swaps opposite  edges and leaves diagonals invariant 
* **Def** reciprocal arc = arc invariant by ell. inv.

# and this


$$\frac{1}{m} = \mathrm{Im} \frac{ai +b}{ci+d}  = \frac{1}{c^2 + d^2}$$


# Problem 3:

### Martin Aigner
<!-- _transition: wipe -->

![bg left](./Martin_Aigner.jpg)

* [Proofs from THE BOOK](https://en.wikipedia.org/wiki/Proofs_from_THE_BOOK#:~:text=Proofs%20from%20THE%20BOOK%20is,proof%20of%20each%20mathematical%20theorem)
* 100 years of uniqueness
* [Convexity and Aigner's Conjectures](https://arxiv.org/abs/2101.03316)
<!-- * Prove his conjectures with one figure? -->


#
<!-- _transition: slide -->
There is a natural map (we'll see why shortly)

$\mathbb{Q}\cup \infty \rightarrow \text{Markoff numbers},\,\, p/q \mapsto m_{p,q}$

![w:1000](./aigner_mono.png)


#
### Aigner's monotonicity conjectures

- M. Rabideaua, R. Schiffler, Continued fractions and orderings on the Markov numbers, Advances in Mathematics Vol 370,  2020. [arxiv 1801.07155](https://arxiv.org/abs/1801.07155)
- C Lagisquet and E. Pelantová and S. Tavenas and L. Vuillon, On the Markov numbers: fixed numerator, denominator, and sum conjectures. Advances in Applied Mathematics Volume 130, September 2021 [arxiv 2010.10335](https://arxiv.org/abs/2010.10335)
- Kyungyong Lee, Li Li, Michelle Rabideau, Ralf Schiffler, On the ordering of the Markov numbers [arxiv 2010.13010](https://arxiv.org/abs/2010.13010)






#
<!-- _transition: wipe -->
## Aigner's conjectures proof

![w:800](./lines.png)

#
<!-- _transition: cube -->
## Sketch of proof


**Definition:** Let $c$ be an essential closed curve and $\ell_c$ denote its length.

$\gamma \in H^1(T,\mathbb{Z}), \, \| \gamma \| := \inf_{ c \in \gamma} \ell_c/2$


**Natural map:** $(p/q) \leftrightarrow \gamma_{p/q} = q\alpha + p \beta \in H_1(\mathbb{H}/\Gamma')$

**Theorem** The shortest representative for a non trivial homology class is always a multiple of a closed simple geodesic.

* $m_{p/q} = \frac23 \cosh\left(\frac12\ell_{\gamma_{p/q}} \right)= \frac23 \cosh(\| q\alpha + p\beta \|_s)$
* **important** $t ↦ \frac23 \cosh(t)$ monotone increasing on $[0,\infty[$



#
<!-- _transition: wipe -->
## Aigner's conjectures proof

![w:800](./lines.png)


# Labeling Markoff numbers
<!-- _transition: cube -->


* Markoff number = $m_{p/q}$
* Farey "tree" of coprime integers $p,q$
* Markoff tree of solutions to the cubic
* Bass-Serre tree of a free product 
* Mapping class group of the torus $\simeq PSL(2,\mathbb{Z}) \simeq \mathbb{Z}/2 * \mathbb{Z}/3$

# 
### Tree structure for triples

comes from Bass-Serre tree of
 $PSL(2,\mathbb{Z})$ 

![bg left 100%](./Markoff_tree_full.svg)


# 
<!-- _transition: slide -->
## arcs 


![bg left 55%](./ptorusx.svg)

* $\gamma$ simple closed geodesic 
* $\gamma^*$ arc  on a punctured torus(disjoint from the closed geodesic)
* $\lambda$-lengths of arc
<!-- * snake graph and its perfect matchings -->
<!-- * "lengths" that verify a Ptolemy inequality -->

# Farey diagram

<!-- _transition: slide -->
<!-- $\mathbb{Q}\cup \infty \subset$ circle/projective line -->

![bg left](./sami.jpg)

* $(a,c)\text{ primitive} \mapsto a/c \in \mathbb{Q}\cup\infty$
* $\begin{pmatrix} a & b \\ c & d \end{pmatrix} \mapsto$  arc $(a/c, b/d)$ 
* $a/b, c/d$ **Farey neighbors** iff $|ad - bc | =  1$
* obvious transitive $SL(2,\mathbb{Z})$  action on Farey neighbors

# $\lambda$-lengths

<!-- _transition: slide -->
<!-- $\mathbb{Q}\cup \infty \subset$ circle/projective line -->

![bg left](./sami.jpg)

## Definition
 **arc** = Poincaré geodesic joining $a/c, b/d \in \mathbb{Q}\cup \infty$
* **$\lambda$-length of  arc** $= |ad - bc|$ 
* $\lambda$-length of arc on $\mathbb{H}/\Gamma'$ 
or $\mathbb{H}/\Gamma(n)$ is the length of a lift to $\mathbb{H}$

#

## Ptolemy identity

<!-- _transition: slide -->

![w:800](./ptolemy.svg)

#

## Ptolemy identity is homogeneous

- (Ptolemy) $z^+  z^- = x^2 + y^2$ 
- $\lambda$-lengths only defined up to a multiplicative constant
* ie a choice of horoballs based at the parabolic points $p/q$


#
<!-- _transition: fade -->
![w:600](./sami.jpg)
[source](https://www.math.mcgill.ca/sdouba/seminar/sami)

<!-- # -->
<!-- ![width:600px](./pozzi.jpg.png) -->
<!-- [source](https://www.mathi.uni-heidelberg.de/~pozzetti/trees/4.pdf) -->

#
<!-- _transition: cube -->
![width:600px](./farey_tree.png)

[source](https://www3.nd.edu/~math/rtg/GTS/www3.nd.edu/_jquigle2/GSTS%20FA18/Week1P.pdf)

<!-- # -->
<!-- ## Visualizing using natural map -->

<!-- $\mathbb{Q}\cup \infty \rightarrow$ Markoff numbers -->

<!-- $p/q \mapsto m_{p/q} = \frac23 \cosh\left(\frac12\ell_{\gamma_{p/q}} \right)= \frac23 \cosh(\| (q,p) \|_s)$ -->

<!-- * $SL(2, \mathbb{Z})$ action on $\mathbb{Q}\cup \infty$ --> 
<!-- * mapping class group action on simple curves on $\mathbb{H}/\Gamma'$ -->

# 
### Tree structure

<!-- _transition: cube -->
comes from Bass-Serre tree of
 $PSL(2,\mathbb{Z})$ 

![bg left 100%](./Markoff_tree_full.svg)


#
<!-- _transition: slide -->
## Role of the character variety 

H. Cohn Approach to Markoff’s Minimal Forms Through Modular Functions (1955)

* modular torus = quotient of upper half plane $\mathbb{H}$ by  commutator subgroup of $\Gamma'< \text{PSL}(2, \mathbb{Z})$, acting by Mobius transformations
*  relates Markoff numbers to lengths of simple closed geodesics

# 
<!-- _transition: cube -->
![bg left 55%](./ptorusx.svg)

- modular torus = quotient of upper half plane $\mathbb{H}$ by  commutator subgroup of $\Gamma'< \text{PSL}(2, \mathbb{Z})$
* length geodesic $\ell_\gamma$
* $\lambda$-length arc  $\ell_{\gamma^*}$ 
* after normalising $\ell_{\gamma^*} = 2\cosh(\ell_\gamma/2)$

#
<!-- _transition: fade -->
## Character variety

 modular torus = $\mathbb{H}/\Gamma'$ 

* $\Gamma'\simeq$ fundamental group of the torus $\simeq \mathbb{Z}*\mathbb{Z} = \langle a,b \rangle$
* representation  $\hat{\rho}:\langle a,b \rangle \rightarrow\text{SL}(2, \mathbb{R})$ 



* **Definition** *character map* $\chi : \rho \mapsto ( tr \hat{\rho}(a),  tr \hat{\rho}(b),  tr \hat{\rho}(ab) )$
* $|tr \hat{\rho}(c)| = 2\cosh(\ell_\gamma/2)$
* $\Rightarrow \chi(\hat{\rho})\leftrightarrow \text{triple of simple closed geodesics}$ 
* $aba^{-1}b^{-1}=$   loop round puncture $\Rightarrow tr \hat{\rho}(aba^{-1}b^{-1}) = -2$

#


<!-- {: style="text-align: left"} -->
<!-- _transition: fade -->



**Theorem:** (Cohn and many others) The semi-algebraic set:

$(x,y,z) \in \mathbb{R}_+,\,0 = tr \hat{\rho} (aba^{-1}b^{-1}) + 2 = x^2 + y^2 + z^2 - x y z = 0.$

* identified with the Teichmueller space of the punctured torus.
* group  of the automorphisms is induced by the action of the mapping class group

* the permutation $(x,y,z) \mapsto (y,z,x)$
* the (Vieta) involution $(xy-z,z,y)$
* $\Rightarrow$ recursively enumerate  lengths all simple closed curves



#
<!-- _transition: fade -->

![bg left 100%](./Markoff_tree_full.svg)

 $x^2 + y^2 + z^2 - x y z = 0.$
* $z^2 - (x y) z +  (x^2 + y^2)  
 = 0.$
* roots $z^+, \, z^-$ satisfy both Vieta relations
*  (trace) $z^+ + z^- = xy$ 
*  (Ptolemy) $z^+  z^- = x^2 + y^2$ 


#
<!-- _transition: fade -->

![bg left 100%](./Markoff_tree_full.svg)

## Lemma A:
$\ell_{\gamma^*} = 2\cosh(\ell_\gamma/2)$

- Proof:

-  (trace) $z^+ + z^- = xy$ 
-  (Ptolemy) $z^+  z^- = x^2 + y^2$ 
* normalise so that $\lambda$-lengths are $(3,3,3)$ then do an induction $\Box$

#
<!-- _transition: fade -->
## (Geometric) uniqueness conjecture

The multiplicity of any number in the complementary regions to the tree is at most **6**.

![bg left 100%](./Markoff_tree_full.svg)



# Button's Theorem and $\lambda$-lengths

<!-- _transition: cube -->
#
<!-- _transition: slide -->
## Button's Theorem

If $z$ is a Markoff number which is prime
then there is a unique triple $z > y > x$

$x^2 + y^2 + z^2 - 3x y z = 0.$

#
<!-- _transition: cube -->
### Theorem (Fermat)

Let $p$ be a prime then $p=c^2 + d^2$ has a solution over $\mathbb{Z}$ iff 
1. $p = 2$ 
1. $p − 1$ is a multiple of 4.

* Button's theorem follows from "unicity" of $c,d$
* unique factorisation $p = (ci+d)(-ci+d)\in \mathbb{Z}[i]$
* The multiplicity of any number in the complementary regions to the tree is at most **6**


# Why 6?

<!-- _transition: cube -->
 $\Gamma = \mathrm{PSL}(2,\mathbb{Z})$ and  $\Gamma' = [\Gamma,\Gamma]$ 
* $\mathbb{H}/\Gamma' =$ modular torus
* loop around the cusp $z \mapsto z + 6$
* automorphism group $\Gamma/\Gamma' \simeq \mathbb{Z}/6\mathbb{Z}$
* "generator" of the automorphism group is $z \mapsto z + 1$
* $z \mapsto -1/z$ normalises $\Gamma'$ so induces an involution of $\mathbb{H}/\Gamma'$
* := **elliptic involution** has 3 fixed points which lift to the $\Gamma$ orbit of i.

#
<!-- _transition: cube -->
![bg left 50%](./ptorusx.svg)

* elliptic involution swaps triangles fixes midpoint of diagonal
* $z \mapsto -1/z$ normalises induces an involution of $\mathbb{H}/\Gamma'$
* the fixed points lift to the $\Gamma.\{i\}$

<!-- # -->
<!-- <!-1- _transition: slide -1-> -->
<!-- ![w:650](./farey_tree.png) -->


<!-- # -->
<!-- <!-1- _transition: slide -1-> -->
<!-- ![w:550](./ford_circles.gif) -->
<!-- **Ford circles** -->

#
<!-- _transition: cube -->
## Ford circles

![w:600](./ford_circles_again.png)
  $\mathrm{SL}(2,\mathbb{Z})$ orbit of $F := \{ z, \mathrm{Im}\, z > 1\}$ are the Ford circles


<!-- <!-1- # Definitions -1-> -->
<!--  **arc** = Poincaré geodesic joining $a/c, b/d \in \mathbb{Q}\cup \infty$ -->
<!-- * **$\lambda$-length of  arc** $= |ad - bc|$ --> 
<!-- * $\lambda$-length of arc on $\mathbb{H}/\Gamma'$ is the length of a lift to $\mathbb{H}$ -->


<!-- * $\mathrm{SL}(2,\mathbb{Z})$ acts by Mobius transformations on $\mathbb{H}$ -->
<!-- * orbit of $F := \{ z, \mathrm{Im}\, z > 1\}$ are the Ford circles -->
<!-- <!-1- - $\begin{pmatrix} a & b \\ c & d \end{pmatrix}.z = \frac{az+b}{cz+d}$ -1-> --> 

<!-- # -->
<!-- <!-1- _transition: slide -1-> -->
<!-- ![w:500](./ford_circles_again.png) -->

<!-- * $p/q$ point of tangency with $\mathbb{R}$, diameter = $1/q^2$ -->
<!-- *   hyperbolic midpoint of the arc joining $F$ to this Ford circle is at euclidean height $1/q$ -->
<!-- <!-1- - ie diameter is the square of the inverse of the denominator of $p/q$ -1-> -->

<!-- # -->
<!-- <!-1- _transition: cube -1-> -->
<!-- ![bg left 100%](./lambda.svg) -->

<!-- - $p/q$ point of tangency with $\mathbb{R}$, diameter = $1/q^2$ -->
<!-- -   hyperbolic midpoint of the arc joining $F$ to this Ford circle is at euclidean height $1/q$ -->
<!-- <!-1- - ie diameter is the square of the inverse of the denominator of $p/q$ -1-> -->

# 

-  $\mathrm{SL}(2,\mathbb{Z})$ orbit of $F := \{ z, \mathrm{Im}\, z > 1\}$ are the Ford circles

## Proposition (Penner)
<!-- _transition: slide -->

- **arc** joining $a/c, b/d$ has **$\lambda$-length** $= |ad - bc|$ 
- **$2 \log \lambda$-length** = length of the portion outside Ford circles tangent to the real line at its endpoints

## Corollary
If one of the Ford circles is $F$ then 
the **midpoint** of the arc is at Euclidean height $1/(\lambda-\text{length})$


#
<!-- _transition: cube -->
![bg left 100%](./lambda.svg)
## Corollary
One of the Ford circles is $F$ then 
the **midpoint** of the arc is at Euclidean height $1/(\lambda-\text{length})$

<!--  $\mathrm{SL}(2,\mathbb{Z})$  transitive on $\mathbb{P}(\mathbb{Q}^2)$, --> 
<!-- * can suppose $a/c= \infty=1/0$ and $b/d = k/(ad - bc)$ -->
<!-- * joins Ford circle  $F$  tangent at $\infty$ and another of diameter $1/(ad - bc)^2$ -->
<!-- * hyperbolic length of portion outside these is $2\log(ad - bc)$ -->
<!-- <!-1- - the **midpoint** of this vertical arc is at height $1/|ad - bc|$ -1-> -->


#
<!-- _transition: cube -->
![bg left 50%](./ptorusx.svg)

 blue arc $\gamma^*$  unique arc  disjoint from blue curve $\gamma$  


<!-- # -->
<!-- <!-1- _transition: slide -1-> -->
### Lemma A'
Normalisation, fundamental triple $=(1,1,1)$
$m = \ell_{\gamma^*}= \frac23 \cosh(\ell_\gamma/2)$.


### Corollary B
Every Markoff number $m$ is a sum of squares ie $m=c^2 + d^2$

#
<!-- _transition: slide -->
## Geometric proof of Corollary B

* simple close geodesic $\gamma$ is invariant under the elliptic involution
* the unique arc $\gamma^*$ disjoint from $\gamma$ is invariant
* $⇒ \exists$  a fixed point of the elliptic involution on $\gamma^*$
* $⇒ \exists$ a lift of $\gamma^*$ which is a vertical line and which meets  $\Gamma.\{i\}$
* since $\lambda$-length of $\gamma^*$ = m this point is at euclidean height $1/m$

#
<!-- _transition: cube -->
## and  so we have the equation

$$\text{height } = \frac{1}{m} = \mathrm{Im} \frac{ai +b}{ci+d}  = \frac{1}{c^2 + d^2}$$


# by the same argument.... 
<!-- _transition: cube -->


**Lemma C** Let $m$ be a positive integer. 
The "number of  ways" of writing $m$  as 
$m = c^2 + d^2$ with $c,d$ coprime,
is equal to the number of arcs satisfying:

joins $\infty$ to $0<  k/m < 1$ 
integers $k$ and $m$   coprime
arc meets the orbit  $\Gamma.\{i\}$

# Counting solutions
<!-- _transition: slide -->
The "number of  ways" of writing $m$  as $m = c^2 + d^2$.

* four choices for the signs $\pm c, \pm d$ 
* swap $c$ and $d$, only swapping $c,d$ "counts" 

<!-- # Example -->
<!-- _transition: slide -->

* **Example:** $5 = 2^2 + 1^2= 1^2 + 2^2$
* $$\begin{pmatrix} 1& 0 \\ 2& 1 \end{pmatrix}.i = \frac{i}{2i+1} = \frac25 + \frac{i}{5},\,\,\, \begin{pmatrix} 1& 1 \\ 1& 2 \end{pmatrix}.i = \frac{i+1}{i+2} = \frac35 + \frac{i}{5}$$

<!-- text_align: top -->

#
<!-- _transition: cube -->
**Lemma C'** Let $m$ be a positive integer. 
The "number of  ways" of writing $m$  as 
$m = c^2 + d^2$ with $c,d$ coprime,
is equal to the number of arcs 

1. on the modular surface 
1. of $\lambda$-length $m$ 
1. which pass through the cone point of of order 2.

#

<!-- _transition: slide -->
### Corollary B
Every Markoff number $m$ is a sum of squares ie $m=c^2 + d^2$

# 
## Recursion for (complex) Markoff numbers


  (Ptolemy) $z^+  z^- = x^2 + y^2$ 

In fact the Ptolemy relation factorises over $\mathbb{C}$
$$z^+ z^- = (x + i y)(x - i y) = x^2 + y^2 $$
yields a recursion for a set of Gaussian integers $\{\hat{m}\}$
such that each Markoff number $m$ is the **norm** of $\hat{m}$

$$\hat{z}^+ \hat{z}^- = x^2 + y^2 = |\hat{x}|^2 + i|\hat{y}|^2$$

* **Example:** Fibonacci numbers $F_{2n+3}F_{2n-1} = 1 + F_{2n-1}^2$


# 

 Fibonacci numbers $F_{2n+3}F_{2n-1} = F_{2n-1}^2 + 1$
```
x, y = 1 + 0J, 1 + 1J

fib = []
for k in range(10):
    z = y*y.conjugate() + 1J
    u = x*z/ (x*x.conjugate())
    fib.append(f'{u}')
    x, y = y, u
    
' '.join(fib)
```
$$2+1i, 2+3i, 5+3i, 5+8i, 13+8i, 13+21i, 34+21i, 34+55i, 89+55i, 89+144i$$

* Just showing that $F_{2n+1} = F_{n+1}^2 + F_n^2$. 


#
<!-- _transition: cube -->
<iframe src="./button.html" height="600" width="700"></iframe>

**Back to Button** exactly 6 simple arcs of $\lambda$-length $m$ on $\mathbb{H}/\Gamma'$ 

# Proof of Button

<!-- _transition: slide -->
 every Markoff number $m$ is the sum of two squares
* if $m$ is prime then there are two ways of doing this
* $\Rightarrow$ there are $\leq 12$ oriented simple arcs of $\lambda$ length $m$ on $\mathbb{H}/\Gamma'$
* $\Rightarrow$ multiplicity of $m$ in the Markoff tree $\leq 6$

<!-- # In fact.... -->


 <!-- <p style = "text-align: left"> --> 
<!-- if m is a Markoff number and --> 
<!-- </p> -->

<!-- - $m = p^k$ -->
<!-- - or $m = 2p^k$ -->

 <!-- <p style = "text-align: left"> --> 
<!-- then m satisfies the uniqueness conjecture -->
<!-- </p> -->

# Sums of squares
<!-- _transition: cube -->
## Button's Theorem

If $z$ is a Markoff number which is prime<br>
then there is a unique triple $z > y > x$

* $x^2 + y^2 + z^2 - 3x y z = 0.$
* $\bar{x}^2 + \bar{y}^2 = 0.$ in $\mathbb{F}_z$
* $(\bar{x}/\bar{y})^2 = -1$ in $\mathbb{F}_z$
*  $\Rightarrow p = 2$ or $p − 1$ is a multiple of 4.


#

<!-- _transition: slide -->


**Theorem F1:** Let $p$ be a prime then
$x^2 + y^2= p$
has a solution over $\mathbb{Z}$
if $p = 2$ or $p − 1$ is a multiple of 4.


**Theorem F2:** Let $p$ be a prime then
$x^2  + xy + y^2= p$
has a solution over $\mathbb{Z}$ 
iff $p = 3$ or $p − 1$ is a multiple of 6.

**Theorem F3:** Let $p$ be a prime then
$x^2 + 2y^2= p$
has a solution over $\mathbb{Z}$
if $p = 1,3 \mod 8$.

#

* $x^2 + y^2= p \rightarrow$ 
* arcs of $\lambda$-length $p$ on $\mathbb{H}/\Gamma(2)$
* $x^2  + xy + y^2= p \rightarrow$ 
* immersed ideal triangles of $\lambda$-length $p$ on $\mathbb{H}/\Gamma(2)$
* $x^2 + 2y^2= p\rightarrow$ arcs of $\lambda$-length $p$ on $\mathbb{H}/\Gamma_0(2)$

#

An immersed ideal triangles with sides of $\lambda$-length $3$ on $\mathbb{H}/\Gamma(2)$

![w:600](./immersed.png)

#
<!-- _transition: slide -->
## two groups of order 4

Acting on $\mathbb{F}_p^*$

$\begin{array}{lll}
x &\mapsto& -x \\
x &\mapsto& 1/x
\end{array}$

Acting on $\mathbb{H}$

$\begin{array}{lll}
z &\mapsto& -\bar{z} \\
z &\mapsto& 1/\bar{z}
\end{array}$

#
## Zagier

<!-- _transition: glow -->
![w:1200](./zagier.png) 

<!-- # -->
<!-- <!-1- _transition: cube -1-> -->
<!-- ## Let's begin then... -->

#
<!-- _transition: slide -->
### Burnside Lemma 

- $G$ acting on $X$ then $|G| |X/G| = \sum_{g} |X^g|$


- $X^g$ :=  fixed points of the element $g$ 
- $X/G$ :=  the orbit space.


* **proposition** 
If $p$ is a prime of the form $4k+1$ 
then $x^2 = -1$ has a solution over $\mathbb{F}_p$ 
* Follows from Wilson's Theorem

#
<!-- _transition: slide -->
**"Geometric" proof:** Group acting on $X = \mathbb{F}_p^*$:

$\begin{array}{ll}
x &\mapsto& x &&
x &\mapsto& -x \\
x &\mapsto& 1/x &&
x &\mapsto& -1/x
\end{array}$

* **Count fixed points**

* identity $|X^g| = p-1$ 
* $x \mapsto -x, |X^g| = 0$  
* $x \mapsto 1/x, |X^g| = 2$  
* $x \mapsto -1/x, |X^g| = \ldots$ ?  

#
<!-- _transition: glow -->
### Apply Burnside

- $|G| |X/G| = \sum_{g} |X^g|$
- $4 |X/G| = (p-1) + 2 + |X^{(x\mapsto -1/x)}|$

* if p=1 mod 4, then
* $0 =0+2+|X^{(x\mapsto -1/x)}| \mod 4$ 
* $\Rightarrow  |X^{(x\mapsto -1/x)}| \neq 0$
* $\Rightarrow  \exists x\in\mathbb{F}_p^*,\, x^2 = -1$
* $\Box$


<!-- # -->
<!-- <!-1- _transition: cube -1-> -->
<!-- ## QED -->

#
### Theorem F2: sum of 2 squares


$\begin{array}{ll}
z &\mapsto& z &&
z &\mapsto& -\bar{z} \\
z &\mapsto& 1/\bar{z}&&
z &\mapsto& -1/z
\end{array}$

Acting on $\mathbb{H}$ or the Farey diagram
or on the arcs of $\mathbb{H}/\Gamma(2)$


<!-- # -->
<!-- ## Recall -->
<!-- <!-1- _transition: cube -1-> -->


<!-- ![bg left 100%](./sami.jpg) -->


<!-- - **arc** = Poincaré geodesic joining $a/b, c/d \in \mathbb{Q}\cup \infty$ -->
<!-- - **$\lambda$- length of  arc** $= |ad - bc|$ --> 


#
<!-- _transition: cube -->

- $\Gamma(2) = \ker (\mathrm{SL}(2,\mathbb{Z})\rightarrow  \mathrm{SL}(2,\mathbb{F}_2))$
- $\mathbb{H}/\Gamma(2)$  three punctured sphere 
- standard fundamental domain 
* = pair of ideal triangles
* all edges $\lambda$-length 1



![bg left 100%](./fund_dom_gamma2.png)


#
<!-- _transition: cube -->
![bg left 100%](./3sphere.svg)

 $i, 1+i, \frac12 ( 1 + i)$ are midpoints of 3 arcs 
 of $\lambda$-length 1

* $i$  fixed point of 3 different involutions
* one dotted arc has $\lambda$-length $1 = 1^2 + 0^2$
* other dotted arc has $\lambda$-length $2 = 1^2 + 1^2$

#
<!-- _transition: cube -->
## Lemma C'

Let $m$ be a positive integer. 
The "number of  ways" of writing $m$  as a  sum of squares
$$m = c^2 + d^2$$
with $c,d>0$ coprime integers is equal to the number of arcs 
$\{  k/m + i t,\, t>0  \}$
$0 \leq k < m-1$ coprime to $m$ which meet $\Gamma.\{i\}$


<!-- - Let $n$ be a positive integer. -->
<!-- - The number of  ways of writing $n$  as a  sum of squares $n = c^2 + d^2$ with $c,d$ coprime integers -->
<!-- - is equal to the number of  integers $0 \leq k < n-1$ coprime to $n$ such that the line $\{  k/n + i t,\, t>0  \}$ contains  a point in the $\Gamma$  orbit of $i$. -->


#
<!-- _transition: slide -->
subgroup of automorphisms 
fixing the cusp labeled $\infty$:

 <!-- $\simeq \mathbb{Z}/2\mathbb{Z} \oplus \mathbb{Z}/2\mathbb{Z}$ -->

* a reflection $V$ that 
swaps $0,\infty$ 
fixes the arc of $\lambda$-length = 2
* another reflection $U$ that 
fixes $0,\infty$ 
fixes the arc of $\lambda$-length = 1
* both fix the midpoint $i$

![bg left 100%](./3sphere.svg)


#
<!-- _transition: cube -->
### group lifts to 

![bg left 100%](./fund_dom_gamma2.png)

- $U': z \mapsto -\bar{z}$
- $V' : z \mapsto 1/\bar{z}$
* $U'\circ V' : z \mapsto z \mapsto -1/z$
* $U' \circ V'$ fixes $i$

#
<!-- _transition: cube -->
### The set $X$

- arcs joining cusps $0/1, \infty = 1/0$ with $\lambda$-length $p$
- "lift to vertical lines" with endpoints $2k/p\in \Gamma(2).\{0/1\}$ 
- $|X| = p - 1$ as before

<!-- - whose fixed point is $i+1$. -->

#
<!-- _transition: slide -->
## Fixed points I

First the automorphism $U$ 
* fixes $0,\infty$ 
* fixes the arc of $\lambda$-length = 1
* swaps the upper and lower ideal triangles
* $\Rightarrow$ has no fixed points in $X$

![bg left 100%](./3sphere.svg)



#
<!-- _transition: cube -->

The automorphism $V$ induced by $V'$ 
fixes two and exactly two arcs in $X$.

 Can then apply Burnside Lemma to prove Theorem F2

 $4 |X/G| = (p-1) + 2 + |X^{U\circ V}|$

* **Proof:**
* suppose that there is an invariant arc that starts at $a/b$
* then it must end at $V'(a/b) = b/a$ 
* its $\lambda$- length is $|a^2 - b^2| = p$
* $p$ prime $\Rightarrow$ two solution $a-b= \pm 1, a+b= \pm p$ 
$\Box$


# Questions/Remarks
<!-- _transition: glow -->

 Can other elementary results for quadratic forms?
* $x^2  + xy + y^2= p$ if $p − 1$ is a multiple of 6.
using immersed "equilateral" ideal triangles.
*  (Elsholtz) $x^2 + 2y^2 = p$ if $p =  3 \mod 8$ 
 using arcs $\mathbb{H}/\Gamma_0(2)$ where $\Gamma_0(n) := \left\{\begin{pmatrix} 1 & * \\ 0 & 1 \end{pmatrix} \mod n \right\}$

* Baragar ? [m, 3m - 2, 3m + 2 prime](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/88B0E426FFCBEA8B3A345C1074B8CC59/S0008439500018828a.pdf/on-the-unicity-conjecture-for-markoff-numbers.pdf)
* More detailed analysis of the spectrum of $\lambda$-lengths?
**Orthotree, orthoshapes and ortho-integral surfaces**
Nhat Minh Doan





# 
<!-- _transition: cube -->
![w:800](./thatsallfolks.png)

#


