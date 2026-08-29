# Dual General Position in the Join of a Complete Graph and a Tree

> Internal working draft, 29 August 2026. This document makes no novelty or
> priority claim. The literature cutoff and coverage limitations are recorded
> in `notes/mixed_join_literature_positioning.md`.

## Abstract

Let $r\ge 1$ and let $T$ be a tree of order at least three. We classify the
dual general-position sets of the mixed join $K_r+T$ according to whether they
meet the universal clique. The apex-meeting branch is governed by partitions
of $T$ into two induced cliques, while the apex-avoiding branch is governed by
a tree parameter $\beta(T)$, where
$\beta(T)=\max\{|X|:X\subseteq V(T),\ \Delta(T[X])\le 1,
|N_T(x)\setminus X|\le 1\text{ for every }x\in X\}$. This gives

$$
\operatorname{gp}_d(K_r+T)=
\begin{cases}
r+2,&T\in\{P_3,P_4\},\\
\beta(T),&\text{otherwise}.
\end{cases}
$$

We characterize every $\beta$-feasible set by the degrees and labels of
neighboring vertices, and give a linear-time, linear-space rooted-tree dynamic
program that reconstructs a maximum set. Worked families include stars,
once-subdivided stars, and paths. Two bounded computations with distinct
checking logic test the implementation against exhaustive local search and a
definition-first shortest-path checker; these calculations are supporting
evidence, not proof.

## 1. Introduction

A set of vertices of a connected graph is in *dual general position* if it is
in general position and its complement is convex. Equivalently, no geodesic
contains three selected vertices, and every geodesic between two unselected
vertices stays outside the selected set. Tian and Klavžar introduced and
developed this variant of the general-position problem and proved the criterion
that combines these two conditions [1].

The behavior of dual general position under graph products was subsequently
studied by Dokyeesun, Klavžar, Kuziak, and Tian [2]. In particular, their work
posed the problem of determining the dual general position number of
lexicographic products with a complete first factor. Jiang's 2026 preprint
[3, Theorem 3.2] gives the formula

$$
\operatorname{gp}_d(K_m\circ G)=m q_2(G), \qquad m\ge 2,
$$

for every nonempty finite simple graph $G$, where $q_2(G)$ is the largest size
of one class in a partition of $V(G)$ into two sets that each induce a clique;
set $q_2(G)=0$ if no such partition exists. The same preprint [3, Theorem 5.1]
also treats complete joins whose factors are all nonempty and noncomplete. Its
Theorem 5.1 explicitly does not classify joins containing both a complete and
a noncomplete factor. Thus the mixed join $K_r+T$, with $T$ a noncomplete tree,
lies outside that theorem; it is also different from the lexicographic product
$K_m\circ T$.

One subfamily of the mixed-join problem is already known. The fan graph is
$F_n=K_1+P_n$, and Tian, Dokyeesun, and Klavžar [4, arXiv v2] proved, for
$n\ge 4$, that

$$
\operatorname{gp}_d(F_n)
=\left\lfloor\frac{2(n+1)}{3}\right\rfloor
=\left\lceil\frac{2n}{3}\right\rceil.
$$

Consequently, the fan case is prior work and is used here only as a consistency
check. The formula above is the one displayed in arXiv v2 of [4]. The exact
display in the version of record has not been independently checked and remains
`UNKNOWN`.

This note studies $K_r+T$ for $r\ge 1$ and for trees $T$ of order at least
three. For a tree $T$, define

$$
\beta(T)=\max\bigl\{|X|:\ \Delta(T[X])\le 1
\text{ and } |N_T(x)\setminus X|\le 1\text{ for every }x\in X\bigr\}.
$$

The main structural argument separates dual general-position sets that meet
the universal clique $V(K_r)$ from those that avoid it. The first branch is
controlled by a two-clique partition of the tree, while the second is exactly
the optimization problem defining $\beta(T)$. This yields

$$
\operatorname{gp}_d(K_r+T)=
\begin{cases}
r+2, & T\in\{P_3,P_4\},\\
\beta(T), & \text{otherwise}.
\end{cases}
$$

Sections 3--5 give a self-contained proof of both branches, a local
characterization of the $\beta$-feasible sets, and a linear-time dynamic
program that reconstructs a maximum set. Section 6 gives worked families, and
Section 7 records two bounded checks with distinct verification logic. The
computations are supporting evidence rather than proof. A bounded literature audit did not find
the full all-tree, arbitrary-$r$ result; because several subscription databases
were not directly checked and terminology may differ, its global novelty
remains `UNKNOWN`.

## 2. Preliminaries

All graphs in this note are finite and simple. For a graph $G$, its vertex and
edge sets are denoted by $V(G)$ and $E(G)$. If $X\subseteq V(G)$, then $G[X]$
is the subgraph induced by $X$, and $G-X$ abbreviates
$G[V(G)\setminus X]$. The open neighborhood of a vertex $x$ is $N_G(x)$, and
$\Delta(G)$ denotes the maximum degree of $G$; by convention, the empty graph
has maximum degree zero. A complete graph of order $r$ is denoted by $K_r$,
and $P_n$ denotes the path of order $n$.

Let $G$ be connected. The distance $d_G(u,v)$ is the minimum length of a
$u,v$-path, where length means the number of edges. A path of length
$d_G(u,v)$ is a *$u,v$-geodesic*. There may be more than one geodesic between
the same two vertices. The interval between $u$ and $v$ is

$$
I_G(u,v)=\{w\in V(G):w\text{ lies on some }u,v\text{-geodesic}\}.
$$

A set $Y\subseteq V(G)$ is *convex* if
$I_G(u,v)\subseteq Y$ for every $u,v\in Y$; equivalently, every geodesic
between two vertices of $Y$ lies entirely in $G[Y]$.

For $X\subseteq V(G)$, a pair $u,v\in V(G)$ is called
*$X$-positionable* if

$$
I_G(u,v)\cap X\subseteq\{u,v\}.
$$

Thus no internal vertex of any $u,v$-geodesic belongs to $X$. The set $X$ is
a *general-position set* if every pair of vertices in $X$ is
$X$-positionable. Equivalently, no three distinct vertices of $X$ lie on a
common geodesic.

A set $X\subseteq V(G)$ is a *dual general-position set* if every pair whose
two endpoints both lie in $X$, or both lie in $V(G)\setminus X$, is
$X$-positionable. The first family of pairs says exactly that $X$ is a
general-position set. By Tian and Klavžar [1, Theorem 3.1], the second family
is equivalently expressed by convexity of the complement. We will therefore
use the following criterion throughout:

$$
X\text{ is dual general position in }G
\quad\Longleftrightarrow\quad
X\text{ is general position and }G-X\text{ is convex}.
$$

The *dual general position number* is

$$
\operatorname{gp}_d(G)=
\max\{|X|:X\subseteq V(G)\text{ is a dual general-position set}\}.
$$

For vertex-disjoint graphs $G$ and $F$, their *complete join* $G+F$ is
obtained from their disjoint union by adding every edge with one endpoint in
$V(G)$ and the other in $V(F)$. In the rest of the note, $r\ge 1$, $T$ is a
tree of order at least three, and

$$
C=V(K_r),\qquad H=K_r+T.
$$

Every vertex of $C$ is adjacent to every other vertex of $H$. Two vertices on
the tree side are adjacent in $H$ exactly when they are adjacent in $T$.
Because such a tree is noncomplete, $H$ has diameter two.

We use two parameters on the tree side. First, define

$$
q_2(T)=\max\{|A|:V(T)=A\mathbin{\dot\cup}B,
\ T[A]\text{ and }T[B]\text{ are complete}\},
$$

and put $q_2(T)=0$ if no such partition exists. The two classes may be
interchanged, so $q_2(T)$ records the largest possible class in a partition of
the tree into two induced cliques. Second, define

$$
\beta(T)=\max\bigl\{|X|:X\subseteq V(T),\ \Delta(T[X])\le 1,
\ |N_T(x)\setminus X|\le 1\text{ for every }x\in X\bigr\}.
$$

The first constraint in the definition of $\beta(T)$ says that a selected
vertex has at most one selected tree neighbor. The second says that it also
has at most one unselected tree neighbor. These are conditions on the tree
$T$, not on the additional edges of the join $H$.

## 3. The two-branch structural theorem

We first classify dual general-position sets that contain at least one vertex
of the universal clique $C$. This is the *apex-meeting branch*.

### 3.1. Sets meeting the universal clique

**Lemma 3.1.** Let $X\subseteq V(H)$ satisfy $X\cap C\ne\varnothing$, and put

$$
S=X\cap V(T).
$$

Then $X$ is a dual general-position set of $H$ if and only if both $T[S]$ and
$T[V(T)\setminus S]$ are complete.

**Proof.** Choose a vertex $c\in X\cap C$. Suppose first that $X$ is a dual
general-position set. If two vertices $u,v\in S$ were nonadjacent in $T$,
then they would also be nonadjacent in $H$. Since $c$ is adjacent to every
vertex of $H$, the path $u,c,v$ would be a $u,v$-geodesic of length two
containing three vertices of $X$. This would contradict the general-position
property of $X$. Hence $T[S]$ is complete.

Now suppose that two vertices $u,v\in V(T)\setminus S$ were nonadjacent in
$T$. Again $u,c,v$ would be a $u,v$-geodesic of length two. Its endpoints
would lie in $H-X$, whereas its internal vertex $c$ would lie in $X$.
Consequently $H-X$ would not be convex, a contradiction. Thus
$T[V(T)\setminus S]$ is complete.

Conversely, suppose that both induced tree subgraphs are complete. The set
$X$ is then a clique: its vertices in $C$ are pairwise adjacent, its tree
part $S$ induces a clique, and every vertex of $C$ is adjacent to every vertex
of $T$. Therefore $X$ is in general position. The complement $H-X$ is also a
clique, because $C\setminus X$ is a clique,
$T[V(T)\setminus S]$ is a clique, and all edges between these two parts are
present. Every clique is convex, so the criterion from Section 2 shows that
$X$ is a dual general-position set. This proves the equivalence. $\square$

The converse also covers the allowed boundary case $X\cap C=C$, equivalently
$C\setminus X=\varnothing$. In the present scope, $T$ is noncomplete, so the
two tree parts in Lemma 3.1 cannot be empty in a feasible apex-meeting set:
otherwise the other tree part would induce all of $T$.

**Corollary 3.2.** A dual general-position set meeting $C$ exists if and only
if $q_2(T)>0$. When this branch exists, its maximum cardinality is

$$
r+q_2(T).
$$

**Proof.** By Lemma 3.1, the tree part $S$ of such a set and its complement
form a partition of $V(T)$ into two induced cliques. Thus the branch can exist
only if $q_2(T)>0$. Conversely, if
$V(T)=A\mathbin{\dot\cup}B$ is a partition into two induced cliques, then
Lemma 3.1 shows that $C\cup A$ is a dual general-position set meeting $C$.
This proves the existence equivalence.

For every set in this branch, $|X\cap C|\le r$ and $|S|\le q_2(T)$, so
$|X|\le r+q_2(T)$. Choose a two-clique partition whose larger designated
class has size $q_2(T)$ and include that class together with all $r$ vertices
of $C$. Lemma 3.1 gives a dual general-position set of size
$r+q_2(T)$, proving that the bound is attained. $\square$

### 3.2. Sets avoiding the universal clique

We next consider sets contained entirely in the tree side. In this branch the
whole universal clique belongs to the complement.

**Lemma 3.3.** Let $X\subseteq V(T)$, equivalently $X\cap C=\varnothing$.
Then $X$ is a dual general-position set of $H$ if and only if

$$
\Delta(T[X])\le 1
$$

and

$$
|N_T(x)\setminus X|\le 1\qquad\text{for every }x\in X.
$$

**Proof.** Recall that $H$ has diameter two. We first examine the
general-position condition. Suppose that some $x\in X$ has two distinct
neighbors $u,v\in X$ in the tree. Since a tree contains no triangle, $u$ and
$v$ are nonadjacent. Hence $u,x,v$ is a $u,v$-geodesic of length two in $H$,
and all three of its vertices belong to $X$. Thus $X$ is not in general
position.

Conversely, suppose that $X$ is not in general position. Then some geodesic
contains three distinct vertices of $X$. Because $H$ has diameter two, these
three vertices must occur as $u,x,v$ on a length-two $u,v$-geodesic, with
$x$ as its internal vertex. All three lie in $V(T)$, and adjacency between
two tree-side vertices in $H$ is the same as adjacency in $T$. Therefore
$u$ and $v$ are two selected tree neighbors of $x$. We have proved that
$X$ is in general position if and only if no selected vertex has two selected
tree neighbors, which is exactly the condition $\Delta(T[X])\le 1$.

It remains to characterize convexity of the complement. Put
$Y=V(H)\setminus X$. Since $X\subseteq V(T)$, the entire clique $C$ lies in
$Y$. Any pair of vertices of $Y$ with at least one endpoint in $C$ is
adjacent. Likewise, two tree-side vertices of $Y$ that are adjacent in $T$
are adjacent in $H$. Such adjacent pairs have geodesics of length one and
cannot witness a failure of convexity. Consequently $Y$ can fail to be
convex only when two nonadjacent unselected tree vertices have a geodesic of
length two whose internal vertex lies in $X$.

Because every vertex of $X$ is on the tree side, such a geodesic exists
exactly when some $x\in X$ has two distinct neighbors
$u,v\in V(T)\setminus X$. Indeed, if such $u$ and $v$ exist, then they are
nonadjacent because $T$ has no triangle, so $u,x,v$ is a length-two geodesic
with endpoints in $Y$ and internal vertex outside $Y$. Conversely, every
length-two geodesic witnessing nonconvexity has a selected internal vertex
adjacent in $T$ to its two unselected endpoints. It follows that $Y$ is
convex if and only if $|N_T(x)\setminus X|\le 1$ for every $x\in X$.

Combining the general-position and convexity equivalences with the criterion
from Section 2 proves the lemma. $\square$

**Corollary 3.4.** The maximum cardinality of a dual general-position set
that avoids $C$ is $\beta(T)$.

**Proof.** Lemma 3.3 says that the dual general-position sets in this branch
are exactly the subsets of $V(T)$ satisfying the two constraints in the
definition of $\beta(T)$. Taking the maximum of their cardinalities gives
$\beta(T)$. $\square$

### 3.3. Combining the two branches

**Theorem 3.5.** For every $r\ge 1$ and every tree $T$ of order at least
three,

$$
\operatorname{gp}_d(K_r+T)=
\begin{cases}
\beta(T),&q_2(T)=0,\\
\max\{\beta(T),r+q_2(T)\},&q_2(T)>0.
\end{cases}
$$

**Proof.** Every vertex set $X\subseteq V(H)$ either meets $C$ or avoids
$C$, and the two cases are disjoint. If $q_2(T)=0$, Corollary 3.2 says that
the apex-meeting branch is empty, while Corollary 3.4 gives an attainable
maximum of $\beta(T)$ in the apex-avoiding branch. If $q_2(T)>0$, both
branches exist: their attainable maxima are respectively $r+q_2(T)$ by
Corollary 3.2 and $\beta(T)$ by Corollary 3.4. Taking the larger of these two
values proves the formula. $\square$

For trees, the occurrence of the second line of Theorem 3.5 has a particularly
short classification.

**Lemma 3.6.** If $T$ is a tree of order at least three, then

$$
q_2(T)=
\begin{cases}
2,&T\in\{P_3,P_4\},\\
0,&\text{otherwise}.
\end{cases}
$$

**Proof.** A tree contains no triangle. Hence every clique in $T$ has at most
two vertices. If $V(T)$ can be partitioned into two sets that each induce a
clique, then $|V(T)|\le 4$.

There is only one tree of order three up to isomorphism, namely $P_3$. Its
two adjacent vertices and its remaining vertex form a two-clique partition,
so $q_2(P_3)=2$.

At order four, both classes in a two-clique partition must have size two and
therefore must be edges. Thus the two classes form a perfect matching. The
two trees of order four are $P_4$ and $K_{1,3}$. The path $P_4$ has a perfect
matching, obtained by taking its first and last edges, whereas two disjoint
edges cannot occur in $K_{1,3}$ because every edge contains its center.
Consequently $q_2(P_4)=2$ and $q_2(K_{1,3})=0$. Trees of larger order cannot
admit such a partition, proving the lemma. $\square$

We also need the two corresponding values of $\beta$.

**Lemma 3.7.** We have $\beta(P_3)=2$ and $\beta(P_4)=3$.

**Proof.** Let the vertices of $P_3$ occur in the order $v_1,v_2,v_3$.
The set $\{v_1,v_3\}$ is $\beta$-feasible: it is independent, and each of
its vertices has only the neighbor $v_2$ outside the set. Hence
$\beta(P_3)\ge 2$. The full vertex set is not feasible because its induced
subgraph has maximum degree two. Since it is the only set of size three,
$\beta(P_3)=2$.

Now let $v_1,v_2,v_3,v_4$ be the vertices of $P_4$ in path order. The set
$\{v_1,v_2,v_4\}$ is $\beta$-feasible: its induced graph consists of the edge
$v_1v_2$ and the isolated vertex $v_4$, while $v_2$ and $v_4$ each have
exactly one neighbor outside the set and $v_1$ has none. Thus
$\beta(P_4)\ge 3$. The full vertex set is not feasible because its induced
subgraph has maximum degree two, so $\beta(P_4)\le 3$. Therefore
$\beta(P_4)=3$. $\square$

Combining Theorem 3.5 with Lemmas 3.6 and 3.7 yields the announced form.

**Corollary 3.8.** For every $r\ge 1$ and every tree $T$ of order at least
three,

$$
\operatorname{gp}_d(K_r+T)=
\begin{cases}
r+2,&T\in\{P_3,P_4\},\\
\beta(T),&\text{otherwise}.
\end{cases}
$$

**Proof.** If $T\notin\{P_3,P_4\}$, Lemma 3.6 gives $q_2(T)=0$, so the
first line of Theorem 3.5 yields $\operatorname{gp}_d(K_r+T)=\beta(T)$.
For $T\in\{P_3,P_4\}$, the second line gives

$$
\operatorname{gp}_d(K_r+T)=\max\{\beta(T),r+2\}.
$$

Here $\beta(P_3)=2$ and $\beta(P_4)=3$ by Lemma 3.7, while $r+2\ge 3$.
Thus the displayed maximum is $r+2$ in both cases. $\square$

## 4. The tree parameter $\beta(T)$

Call a set $X\subseteq V(T)$ *$\beta$-feasible* if it satisfies the two
constraints in the definition of $\beta(T)$. Those constraints admit the
following equivalent description using only the degrees in the original tree
and the labels of the immediate neighbors.

**Proposition 4.1.** A set $X\subseteq V(T)$ is $\beta$-feasible if and only
if both of the following conditions hold:

1. no vertex of degree at least three in $T$ belongs to $X$; and
2. every vertex $x\in X$ of degree two in $T$ has exactly one neighbor in
   $X$.

Selected vertices of degree zero or one have no additional restriction. In
particular, the statement includes these boundary degrees even though a
degree-zero vertex does not occur under the standing assumption that $T$ has
order at least three.

**Proof.** For each selected vertex $x\in X$, put

$$
s_X(x)=|N_T(x)\cap X|,
\qquad
u_X(x)=|N_T(x)\setminus X|.
$$

Then

$$
s_X(x)+u_X(x)=\deg_T(x).
$$

The condition $\Delta(T[X])\le 1$ says exactly that $s_X(x)\le 1$ for every
$x\in X$, while the second constraint in the definition of $\beta(T)$ says
that $u_X(x)\le 1$. Hence a selected vertex can have degree at most two in
$T$. If its degree is two, the two nonnegative integers $s_X(x)$ and
$u_X(x)$ sum to two and are both at most one, so they must both equal one.
This proves the necessity of conditions 1 and 2.

Conversely, assume conditions 1 and 2. If $x\in X$ has degree two, then it
has one selected and one unselected neighbor, so
$s_X(x)=u_X(x)=1$. If $x\in X$ has degree zero or one, then both neighbor
counts are automatically at most one. Condition 1 excludes every other
degree for a selected vertex. Thus $s_X(x)\le 1$ and $u_X(x)\le 1$ for every
$x\in X$, which are precisely the two defining constraints of a
$\beta$-feasible set. $\square$

This equivalence concerns every feasible set, not only the maximum ones. One
immediate consequence gives a useful general lower bound.

**Corollary 4.2.** If $L(T)$ is the set of leaves of a tree $T$, then
$L(T)$ is $\beta$-feasible. Consequently,

$$
\beta(T)\ge |L(T)|.
$$

**Proof.** Every vertex in $L(T)$ has degree one. Proposition 4.1 therefore
imposes no additional condition on the set consisting of all leaves. The
inequality follows from the definition of $\beta(T)$. $\square$

The first constraint $\Delta(T[X])\le 1$ alone defines a weaker
maximum-degree-one problem. Every $\beta$-feasible set satisfies that
constraint, but the converse is false. In $K_{1,3}$, for example, the center
together with one leaf induces a single edge and satisfies the weaker
constraint. It is not $\beta$-feasible, because the selected center has two
unselected neighbors. Thus a result or algorithm for the weaker problem cannot
simply be substituted for $\beta(T)$ without enforcing the additional
outside-neighbor constraint. The bounded literature audit did not identify an
established name for this stricter parameter; this note makes no claim that the
parameter itself is new.

## 5. Linear-time computation and reconstruction

We now give a dynamic program that computes $\beta(T)$ and reconstructs an
attaining set. Root $T$ at an arbitrary vertex $\rho$. For a vertex $v$, let
$T_v$ be the subtree induced by $v$ and all its descendants, and let
$\operatorname{Ch}(v)$ be the set of children of $v$. We use the label $1$
for a selected vertex and $0$ for an unselected vertex.

For a nonroot vertex $v$ and labels $a,b\in\{0,1\}$, define $F_v(a,b)$ as
the largest number of selected vertices in $T_v$ among all labelings with the
following properties:

- $v$ has label $a$;
- the parent of $v$ has label $b$; and
- every selected vertex in $T_v$ satisfies the two constraints defining a
  $\beta$-feasible set, where the specified parent label is used when checking
  the constraint at $v$.

For the root, write $F_\rho(a,\bot)$, where $\bot$ records that no parent
exists. An impossible state has value $-\infty$.

Fix a state at $v$ and assign a proposed label
$t_u\in\{0,1\}$ to every child $u\in\operatorname{Ch}(v)$. Put

$$
s=\sum_{u\in\operatorname{Ch}(v)}t_u,
\qquad
d=|\operatorname{Ch}(v)|+\mathbf 1_{\{v\ne\rho\}},
$$

and define

$$
p=
\begin{cases}
0,&v=\rho,\\
b,&v\ne\rho.
\end{cases}
$$

Thus $d=\deg_T(v)$, while $p+s$ is the number of selected neighbors of $v$.
If $a=1$, the proposed child labels are admissible exactly when

$$
p+s\le 1
\qquad\text{and}\qquad
d-(p+s)\le 1. \tag{5.1}
$$

The first inequality bounds the selected neighbors of $v$ and the second
bounds its unselected neighbors. If $a=0$, there is no constraint at $v$
itself, because the definition of $\beta$ imposes the two neighbor bounds only
on selected vertices.

The recurrence is therefore

$$
F_v(a,b)
=a+
\max_{(t_u:u\in\operatorname{Ch}(v))}
\sum_{u\in\operatorname{Ch}(v)}F_u(t_u,a), \tag{5.2}
$$

where all child-label vectors are allowed when $a=0$, and only the vectors
satisfying (5.1) are allowed when $a=1$. For the root, the same formula is
used with $b=\bot$ and $p=0$. If the admissible family is empty or a proposed
vector uses an impossible child state, its contribution is $-\infty$. The
answer is

$$
\beta(T)=\max\{F_\rho(0,\bot),F_\rho(1,\bot)\}. \tag{5.3}
$$

**Theorem 5.1.** The recurrence (5.2) computes the exact values of all states,
and (5.3) equals $\beta(T)$. If one maximizing child-label vector is stored
for every finite state, a maximum $\beta$-feasible set can be reconstructed.

**Proof.** We prove the state claim by induction on the height of $v$ in the
rooted tree. If $v$ is a leaf, it has no child subtrees. When $v$ is selected,
(5.1) checks exactly the label of its parent, if one exists; when $v$ is
unselected, it has no constraint of its own. Thus (5.2) lists exactly the
feasible labelings of the one-vertex subtree and counts its selected vertex
by the term $a$.

Now assume that the claim holds for every child of $v$. Fix the label $a$ of
$v$ and, if $v$ is not the root, the parent label $b$. Once the child labels
are fixed, different child subtrees have no edges between them. By the
induction hypothesis, $F_u(t_u,a)$ is the exact largest contribution from
$T_u$ under its two boundary labels. Therefore the best total contribution
from the child subtrees is the sum appearing in (5.2).

It remains only to check the constraint at $v$. If $a=0$, no such constraint
exists, so every combination of feasible child states is allowed. If $a=1$,
then $p+s$ and $d-(p+s)$ are exactly the selected- and unselected-neighbor
counts of $v$. Hence (5.1) accepts precisely the combinations for which $v$
satisfies the two $\beta$ constraints. The recurrence thus neither omits a
feasible labeling nor includes an infeasible one, and the additional term
$a$ counts $v$ exactly once. This proves the state claim by induction.

At the root, every labeling of the whole tree has exactly one of the two root
labels, so taking the maximum in (5.3) gives precisely $\beta(T)$. To
reconstruct an attaining set, choose a maximizing root label. At each visited
state, add $v$ to the set if $a=1$, read its stored maximizing child-label
vector, and continue to each child $u$ in state $(t_u,a)$. These boundary
labels are compatible by construction, and the preceding induction shows
that every stored child state attains its recorded value. The resulting set
is therefore $\beta$-feasible and has cardinality $\beta(T)$. $\square$

**Proposition 5.2.** The value computation and the reconstruction can both be
implemented in $O(|V(T)|)$ time using $O(|V(T)|)$ space.

**Proof.** In a state with $a=0$, the child labels are independent, so for
each child $u$ we choose the larger of $F_u(0,0)$ and $F_u(1,0)$. The work is
therefore proportional to the number of children. In a state with $a=1$,
(5.1) is impossible when $d\ge 3$, because the two bounded neighbor counts
sum to $d$. Every remaining selected state has at most two children, so at
most four child-label vectors need to be examined. There are only constantly
many states per vertex. Summing the child counts over all vertices gives
$|V(T)|-1$, and hence the bottom-up computation takes linear time.

Storing a constant number of state values per vertex and one chosen label for
each relevant parent--child state uses linear space. The top-down
reconstruction visits every vertex once and therefore also takes linear time.
$\square$

## 6. Known subfamilies and worked examples

The examples below illustrate the local structure of $\beta(T)$ and the two
different branches of the main theorem. Their values are derived from the
preceding proofs; no computation is being used as proof.

### 6.1. Stars and the preserved counterexample

Let $T=K_{1,k}$ with center $z$ and $k\ge 3$ leaves. Proposition 4.1 forces
$z$ to be unselected because $\deg_T(z)=k\ge 3$. On the other hand, the set
of all $k$ leaves is $\beta$-feasible. It follows that

$$
\beta(K_{1,k})=k.
$$

The star $K_{1,k}$ is neither $P_3$ nor $P_4$ when $k\ge 3$, so Corollary 3.8
gives

$$
\operatorname{gp}_d(K_r+K_{1,k})=k
\qquad (r\ge 1,\ k\ge 3). \tag{6.1}
$$

Thus the value is independent of the size of the universal clique. In
particular,

$$
\operatorname{gp}_d(K_r+K_{1,3})=3
$$

for every $r\ge 1$. This is the counterexample retained from the feasibility
stage: $q_2(K_{1,3})=0$, so the unsupported extrapolation
$r+q_2(T)$ would give $4$ when $r=4$, whereas the correct value is $3$. The
maximum set in the apex-avoiding branch consists of the three leaves.

### 6.2. Once-subdivided stars

Let $S_k$ be obtained from $K_{1,k}$ by subdividing every edge exactly once,
where $k\ge 3$. Write $z$ for the center, $u_i$ for the degree-two vertex on
the $i$th arm, and $v_i$ for the corresponding leaf. Again $z$ is forced to
be unselected. The set

$$
X=\{u_i,v_i:1\le i\le k\}=V(S_k)\setminus\{z\}
$$

is $\beta$-feasible: every selected $u_i$ has the selected neighbor $v_i$
and the unselected neighbor $z$, while each $v_i$ has degree one. Since the
only remaining vertex is the forced-unselected center, this set is maximum
and

$$
\beta(S_k)=2k.
$$

The tree $S_k$ has order $2k+1\ge 7$, so $q_2(S_k)=0$ by Lemma 3.6. Hence

$$
\operatorname{gp}_d(K_r+S_k)=2k
\qquad (r\ge 1,\ k\ge 3). \tag{6.2}
$$

This family also has a value independent of $r$, but unlike an ordinary star
its maximum set contains both leaves and degree-two vertices.

### 6.3. Paths and the known fan subfamily

We first determine $\beta$ on paths directly from Proposition 4.1.

**Proposition 6.1.** For every $n\ge 3$,

$$
\beta(P_n)=\left\lceil\frac{2n}{3}\right\rceil.
$$

**Proof.** List the path vertices in order as $v_1,\ldots,v_n$. A
$\beta$-feasible set cannot contain three consecutive vertices: the middle
one would be a selected degree-two vertex with two selected neighbors,
contrary to Proposition 4.1. Partitioning the path order into consecutive
blocks of three, followed by a remainder of size zero, one, or two, therefore
gives

$$
|X|\le
\begin{cases}
2q,&n=3q,\\
2q+1,&n=3q+1,\\
2q+2,&n=3q+2.
\end{cases}
$$

These three bounds equal $\lceil 2n/3\rceil$. They are attained by the binary
selection words

$$
(110)^q,\qquad (110)^q1,\qquad (110)^q11,
$$

respectively, where a $1$ means that the corresponding path vertex is
selected. In each word, every selected internal vertex has exactly one
selected neighbor, while the two endpoints have degree one. Proposition 4.1
therefore shows that the indicated sets are $\beta$-feasible. $\square$

Corollary 3.8 now yields, for every $r\ge 1$ and $n\ge 3$,

$$
\operatorname{gp}_d(K_r+P_n)=
\begin{cases}
r+2,&n\in\{3,4\},\\
\left\lceil\dfrac{2n}{3}\right\rceil,&n\ge 5.
\end{cases} \tag{6.3}
$$

When $r=1$, the graph $K_1+P_n$ is the fan $F_n$. For $n=4$, the first line
of (6.3) gives $3=\lceil 8/3\rceil$, and for $n\ge 5$ the second line applies.
Thus, for every $n\ge 4$, the present theorem recovers

$$
\operatorname{gp}_d(F_n)
=\left\lceil\frac{2n}{3}\right\rceil
=\left\lfloor\frac{2(n+1)}{3}\right\rfloor.
$$

The equality of the ceiling and floor expressions follows immediately by
considering $n$ modulo three. This is exactly the formula stated in arXiv v2 of
[4], so the fan calculation is a consistency check and not a novelty claim.
Formula (6.3) additionally makes clear that for paths of order
at least five, the value stays unchanged when the single fan apex is replaced
by an arbitrary clique $K_r$; the exceptional paths $P_3$ and $P_4$ belong to
the apex-meeting branch and retain their $r+2$ dependence.

## 7. Computational verification and reproducibility

The proofs in Sections 3--6 do not depend on computation. The calculations
reported here test the implementation and search for small counterexamples;
finite agreement is supporting evidence and is not a proof of any theorem.

### 7.1. Two verification routes

The project keeps the following two main comparisons separate. They use
distinct checking logic but share the audit driver and NetworkX-generated tree
instances.

First, `src/mixed_join_tree.py` implements the rooted-tree recurrence from
Section 5 and reconstructs one maximizing set. It does not import the
shortest-path checker. The audit compares its value with a separate exhaustive
search over all subsets satisfying the two defining local constraints of
$\beta(T)$. The comparison covers every nonisomorphic tree of orders 3 through
12 generated by NetworkX, a total of 985 trees. For each tree, the audit also
checks that the reconstructed set has the reported size and satisfies the two
local constraints. Finally, it recomputes the value with every possible root
to test root invariance.

Second, `src/dual_gp_independent.py` provides a definition-first checker that
does not use the mixed-join theorem, the $\beta$ characterization, or the tree
DP. It constructs $K_r+T$ explicitly, computes all-pairs distances by fresh
breadth-first searches, enumerates vertex subsets, and tests general position
together with convexity of the complement. The audit compares the maximum
found by this checker with the formula implemented from Corollary 3.8. It
covers all 46 nonisomorphic trees of orders 3 through 8 and
$r\in\{1,2,3,4\}$, giving 184 comparisons.

The archived report `results/mixed_join_dp_audit.json` records:

| Check | Scope | Number checked | Failures |
|---|---|---:|---:|
| DP value versus exhaustive subset search | all nonisomorphic trees, orders 3--12 | 985 | 0 |
| root-invariance comparison | every possible root of the same 985 trees | 11,003 | 0 |
| reconstructed maximum set | one reconstruction for each of the 985 trees | 985 | 0 |
| mixed-join formula versus shortest-path definition | all nonisomorphic trees, orders 3--8, and $r=1,2,3,4$ | 184 | 0 |

The earlier target-selection screen in
`results/extension_feasibility_audit.json` contains 92 overlapping small
mixed-join comparisons and the explicitly retained $K_{1,3}$ data. Those
historical checks are not added to the table totals, because doing so would
double-count instances from the larger audit.

### 7.2. Environment and commands

The archived matrix was produced under CPython 3.13.5 and NetworkX 3.6.1. A
fresh rerun on 29 August 2026 used Windows 11 build 26100, CPython 3.13.5,
NetworkX 3.6.1, and pytest 9.1.1. From the repository root, the relevant
PowerShell commands are

```powershell
.\.venv\Scripts\python.exe -m pip install -r .\requirements.txt
.\.venv\Scripts\python.exe -m pytest -q .\tests
.\.venv\Scripts\python.exe .\experiments\audit_mixed_join_dp.py --output .\results\mixed_join_dp_audit.json
```

The fresh test run returned `29 passed`. In addition to the bounded matrices,
the tests cover named values, invalid inputs, reconstruction feasibility, and
a path of order 2,500 to ensure that reconstruction does not rely on Python
recursion. The fresh audit rerun reproduced all four zero-failure rows in the
table above.

For exact artifact identification, the SHA-256 hashes recorded on 29 August
2026 are:

| Artifact | SHA-256 |
|---|---|
| `src/mixed_join_tree.py` | `D3DDAB46510B217BF9C442CC57302953C4D0C29F208DD7ADE06381F2D90A8B9D` |
| `src/dual_gp_independent.py` | `D7BA1C520DC6991E78CB8BAE609A598E6BBF950DA03C1EAC9BA4D30D1EFFF231` |
| `experiments/audit_extension_candidates.py` | `A463CE202995000F324BDB7F90D2821B1B97AB38911E3E8941DFFC381F8393F6` |
| `experiments/audit_mixed_join_dp.py` | `93BA42DB963CAB3F2EE34DAC9CF36511FF6332A84543F44A22ACD48BBB974D44` |
| `results/mixed_join_dp_audit.json` | `C4489D2A7202AD1413EED2FBC551E6CBDFEB6FC5BB10FF32F4899B747C3F4E90` |

The `requirements.txt` file lists the required packages but does not pin exact
versions. The explicit versions and hashes above are therefore part of the
reproducibility record. None of these finite checks establishes correctness
beyond the stated test ranges.

## 8. Conclusion and limitations

For $r\ge 1$ and a tree $T$ of order at least three, dual general-position
sets in $K_r+T$ split into two exhaustive classes. A set meeting the universal
clique exists precisely when the tree can be partitioned into two induced
cliques, and the maximum in that branch is $r+q_2(T)$. A set avoiding the
universal clique is dual general position precisely when it satisfies the two
local constraints defining $\beta(T)$, and the maximum in that branch is
$\beta(T)$. Since a tree in the present scope has a two-clique partition only
when it is $P_3$ or $P_4$, the combined formula is

$$
\operatorname{gp}_d(K_r+T)=
\begin{cases}
r+2,&T\in\{P_3,P_4\},\\
\beta(T),&\text{otherwise}.
\end{cases}
$$

The local characterization of $\beta$ excludes selected vertices of degree at
least three and requires every selected degree-two vertex to have exactly one
selected neighbor. The rooted-tree dynamic program turns this characterization
into a linear-time, linear-space algorithm that also reconstructs a maximum
set. Stars, once-subdivided stars, and paths illustrate the resulting structure.
For $r=1$, the path calculation recovers the formula stated in arXiv v2 of
[4]; that subfamily is prior work and is not presented as a new result.

Several limitations are essential. Jiang's closest general result [3] was
available only as a preprint in the bounded search completed on 29 August 2026;
whether a peer-reviewed version will appear remains `UNKNOWN`. The bounded
computations in Section 7 support the implementation
but do not prove the theorem. The literature audit did not directly cover
MathSciNet, Scopus, or Web of Science, and some open indexes were unavailable;
therefore the global novelty and priority of the all-tree, arbitrary-$r$
mixed-join result remain `UNKNOWN`. The exact formula display in the
version-of-record body of [4] also remains `UNKNOWN`, although its arXiv v2
display was checked.

Finally, this note treats only $K_r+T$ with $r\ge 1$ and $|V(T)|\ge 3$. It
does not classify joins with an arbitrary first factor, general mixed complete
joins with several factors, or lexicographic products $P_n\circ T$. Those
directions are outside the present scope, and no claim about their resolution
or novelty is made here.

## References

[1] J. Tian and S. Klavžar, “Variety of general position problems in
graphs,” *Bulletin of the Malaysian Mathematical Sciences Society* 48 (2025),
Article 5, DOI: `10.1007/s40840-024-01788-z`.

[2] P. Dokyeesun, S. Klavžar, D. Kuziak, and J. Tian, “General position
problems in strong and lexicographic products of graphs,” *Computational and
Applied Mathematics* 45 (2026), Article 97, DOI:
`10.1007/s40314-025-03547-7`.

[3] W. Jiang, “Dual General Position in Lexicographic Products with a Complete
First Factor,” Zenodo preprint v1.0.1 (27 August 2026), DOI:
`10.5281/zenodo.22116770`.

[4] J. Tian, P. Dokyeesun, and S. Klavžar, “On the variety of general
position problems under vertex and edge removal,” *Discrete Applied
Mathematics* 388 (2026), 56–64, DOI: `10.1016/j.dam.2026.02.044`; arXiv:
`2510.01294v2`.
