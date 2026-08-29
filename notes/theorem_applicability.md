# Theorem Applicability Checklist for $K_m \circ T$

## Purpose and scope

Sections A1--A9 preserve the applicability audit of the pre-Jiang verified
literature.  They explain why those earlier results alone did not solve
$K_m\circ T$.  A post-audit update at the end records the now independently
verified Jiang formula and tree corollary.  This note makes no novelty or
peer-review claim.

Unless a boundary case is stated explicitly, assume:

- $m\ge 2$;
- $T$ is a finite connected tree;
- $|V(T)|\ge 3$, so $T$ is not complete.

Labels used below:

- **APPLIES DIRECTLY**: all hypotheses are satisfied, so the cited conclusion may be used.
- **NECESSARY CONDITION ONLY**: the result restricts possible dual sets but does not determine the maximum.
- **SPECIAL CASE ONLY**: the result covers only a small boundary case.
- **DOES NOT APPLY**: at least one hypothesis fails, or the result concerns a different invariant.
- **UNKNOWN AFTER APPLICATION**: the result applies, but further classification is still needed.

## Boundary cases already covered by existing results

### $m=1$

$K_1\circ T\cong T$. A tree is a block graph, and the verified block-graph result gives $gp_d(T)=s(T)$, where $s(T)$ is the number of simplicial vertices. For a nontrivial tree, these are exactly its leaves.

Status: **SPECIAL CASE ONLY**. The intended product problem normally concerns $m\ge 2$.

### $T=K_1$

$K_m\circ K_1\cong K_m$. The verified block-graph result gives $gp_d(K_m)=m$.

Status: **SPECIAL CASE ONLY**.

### $T=K_2$

The second factor is complete. Core-paper Theorem 5.8(ii), with $G=K_m$ and $n=2$, gives

$$
gp_d(K_m\circ K_2)=2gp_d(K_m)=2m.
$$

Status: **SPECIAL CASE ONLY**.

## Audit of the verified theorems

### A1. Dual-set characterization

Result: Tian and Klavžar, Theorem 3.1: a set $X$ is dual general position if and only if $X$ is a general position set and the induced subgraph on $V(G)\setminus X$ is convex.

Applicability: **APPLIES DIRECTLY; NECESSARY CONDITION ONLY**.

For $K_m\circ T$, every candidate $X$ must pass two logically separate tests:

1. $X$ must be in general position;
2. its complement must be convex.

This does not determine the largest possible size of $X$.

### A2. Simplicial-vertex sufficient condition

Result: Tian and Klavžar, Corollary 3.2: every subset of the simplicial vertices is a dual general position set.

Related result: core-paper Lemma 5.1 says that, for connected factors of order at least two, $K_m\circ T$ has no simplicial vertices when $T$ is not complete.

Applicability: **APPLIES DIRECTLY, BUT GIVES NO NONEMPTY SET**.

The corollary therefore supplies no nonempty lower-bound construction in the main range. Importantly, the absence of simplicial vertices does **not** imply $gp_d(K_m\circ T)=0$.

### A3. Convex induced subgraphs of a lexicographic product

Result: Anand et al., Theorem 2.1: in a nontrivial connected $G\circ H$, a proper non-complete induced subgraph $Y$ is convex exactly when its projection is convex, it is $\Lambda$-complete, and $H$ is complete.

Applicability: **APPLIES DIRECTLY; NECESSARY CONDITION ONLY**.

Here $H=T$ is not complete. Hence $K_m\circ T$ has no proper, non-complete convex induced subgraph. Applied to a dual candidate $X$:

- if the complement $Y=(K_m\circ T)-X$ is nonempty, proper, and convex, then $Y$ cannot be non-complete;
- consequently, such a complement must induce a complete graph.

The theorem does not cover the empty complement, the whole product, or complete induced subgraphs. It also does not check whether $X$ is in general position.

### A4. Nonadjacent two-vertex sets

Result: Tian and Klavžar, Proposition 3.10: for nonadjacent vertices $x,y$, the set $\{x,y\}$ is dual general position if and only if both vertices are simplicial.

Applicability: **APPLIES DIRECTLY**.

Because the product has no simplicial vertices in the main range, no nonadjacent two-vertex set can be dual general position.

This rules out one type of two-vertex candidate, but says nothing about larger sets.

### A5. Adjacent two-vertex sets

Result: Tian and Klavžar, Theorem 3.9 gives equivalent conditions for an adjacent pair $\{x,y\}$ to be dual general position.

Applicability: **UNKNOWN AFTER APPLICATION**.

The theorem can be used to test individual adjacent pairs, but its neighborhood and distance conditions have not yet been classified in $K_m\circ T$. Therefore it is currently `UNKNOWN` which adjacent pairs work in general.

### A6. Zero result for products whose factors have no simplicial vertices

Result: core-paper Theorem 5.8(i): if both factors have no simplicial vertices, then the dual general position number of their lexicographic product is zero.

Applicability: **DOES NOT APPLY**.

The first factor $K_m$ has only simplicial vertices, so a required hypothesis fails. The fact that the product itself has no simplicial vertices cannot replace the theorem's assumptions on both factors.

### A7. Complete second factor

Result: core-paper Theorem 5.8(ii): $gp_d(G\circ K_n)=n\,gp_d(G)$.

Applicability: **SPECIAL CASE ONLY**.

Among trees, the complete possibilities are only $K_1$ and $K_2$. Thus this theorem does not cover trees of order at least three. The factor order cannot be swapped because the lexicographic product is generally not commutative.

### A8. Block-graph equality

Result: Tian and Klavžar show that for a connected block graph $G$, the standard, outer, dual, and total general position numbers all equal the number of simplicial vertices.

Applicability: **DOES NOT APPLY TO THE PRODUCT WITHOUT AN EXTRA ARGUMENT**.

It applies to the tree $T$ itself because trees are block graphs. It does not automatically apply to $K_m\circ T$; no verified result currently says that this product is a block graph.

### A9. Results about total or outer general position

The core paper contains lexicographic-product results for total and outer general position.

Applicability: **DOES NOT APPLY TO THE TARGET INVARIANT**.

These are different parameters. A formula for $gp_t$ or $gp_o$ cannot be relabeled as a formula for $gp_d$.

## Combined safe conclusions from the pre-Jiang verified papers

For $m\ge 2$ and $|V(T)|\ge 3$, the verified literature safely implies only the following restrictions:

1. A dual set $X$ must be in general position and must have a convex complement.
2. If that complement is nonempty and proper, it must induce a complete graph; a proper non-complete complement is impossible.
3. The product has no simplicial vertices, so the standard simplicial-vertex construction gives no nonempty dual set.
4. No nonadjacent two-vertex set is dual general position.
5. Adjacent two-vertex candidates still require the exact test from Theorem 3.9.

These statements did not by themselves determine $gp_d(K_m\circ T)$.  They are
retained as a historical applicability record and are superseded for the exact
value by the post-audit result below.

## Post-audit update (2026-08-28)

Jiang v1.0.1 Theorems 3.1--3.2 and Proposition 3.3 passed the project's
independent proof audit.  For every nonempty finite simple graph $G$ and
$m\ge2$,

$$
gp_d(K_m\circ G)=m q_2(G),
$$

where $q_2(G)$ is the maximum size of one side of a partition of $V(G)$ into
two induced cliques, with value zero when no such partition exists.  The
complete proof-step audit is in `proofs/jiang_v1_0_1_audit.md`.

For trees, an independent corollary proof gives

$$
gp_d(K_m\circ T)=
\begin{cases}
m,&T=K_1,\\
2m,&T\in\{K_2,P_3,P_4\},\\
0,&\text{otherwise}.
\end{cases}
$$

The proof is in `proofs/tree_corollary.md`.

The earlier adjacent-pair and convex-complement questions are no longer needed
to determine the maximum, although they can still be studied as structural
subquestions.

## Current status

- Restricted tree formula: **INTERNALLY PROOF-VERIFIED**.
- Supplement reproduction and independent small-instance checks: **PASSED**.
- Jiang v1.0.1 peer-review status: **no peer-reviewed version identified**.
- Novelty or priority claims for this project: **not made**.

The next step recorded at this historical stage was to identify and
literature-audit an extension outside the complete-first-factor theorem's
scope. That step was completed by the mixed-join feasibility and positioning
audits. The active unique next step is maintained only in `PROJECT_STATUS.md`.
