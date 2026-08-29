# The mixed join `K_r + T`: exact reduction and a linear-time tree DP

Date: 2026-08-28

## 1. Status and scope

This note gives an independent proof for the selected problem from
`notes/extension_feasibility_audit.md`.  All graphs below are finite and
simple.  Let `r >= 1`, let `T` be a tree of order at least three, put

```text
C = V(K_r),   H = K_r + T,
```

and write `+` for the complete join.  Thus every vertex in `C` is adjacent to
every other vertex of `H`, while two vertices in the tree side are adjacent in
`H` exactly when they are adjacent in `T`.

We use the verified Tian--Klavžar criterion: a set `X` is dual general position
if and only if `X` is general position and `H-X` is convex.  This is a checked
literature fact.  The theorems and algorithm below are proved in this project.

No novelty or priority claim is made.

## 2. The apex-meeting branch

Define

```text
q_2(T) = max |A|,
```

where the maximum is over partitions `V(T)=A disjoint-union B` for which both
`T[A]` and `T[B]` are cliques; set `q_2(T)=0` if there is no such partition.

### Lemma 2.1

Suppose `X cap C` is nonempty and put `S=X cap V(T)`.  Then `X` is a dual
general-position set of `H` if and only if both `T[S]` and
`T[V(T)\S]` are cliques.

### Proof

Choose `c in X cap C`.

Necessity for general position: if two vertices `u,v in S` were nonadjacent in
`T`, then they would be nonadjacent in `H`, and `u-c-v` would be a length-two
geodesic of `H` containing three vertices of `X`.  This is impossible.  Hence
`T[S]` is a clique.

Necessity for convexity: if two vertices `u,v in V(T)\S` were nonadjacent in
`T`, then `u-c-v` would be a length-two geodesic between two vertices of
`H-X`, but its middle vertex `c` would be outside `H-X`.  Hence `H-X` would not
be convex.  Therefore `T[V(T)\S]` is a clique.

Conversely, suppose the two tree sides are cliques.  The set `X` is a clique:
its tree part is a clique, its complete-factor part is a clique, and every
cross pair is adjacent.  Hence `X` is in general position.  Also `H-X` is a
clique, by exactly the same three observations applied to
`C\X` and `V(T)\S`.  Every clique is convex, so `X` is dual general position.
This proves both directions.  Empty complete-factor or tree subparts cause no
problem in the converse.  In the present scope the whole tree is noncomplete,
so necessity in fact rules out an empty tree side.  QED.

### Corollary 2.2

The apex-meeting branch exists exactly when `q_2(T)>0`, and its maximum size is

```text
r + q_2(T).
```

Indeed, Lemma 2.1 gives exactly a two-clique partition of `T`.  Once the tree
side has been chosen, adding all `r` vertices of `C` preserves the two clique
conditions and maximizes the complete-factor contribution.  Maximizing the
selected tree side gives `q_2(T)`.

## 3. The apex-avoiding branch

For a vertex set `S subseteq V(T)`, define the two local conditions

```text
Delta(T[S]) <= 1,
|N_T(x) \ S| <= 1 for every x in S.
```

Let `beta(T)` be the maximum cardinality of a set satisfying both conditions.

### Lemma 3.1

If `X subseteq V(T)`, so that `X cap C` is empty, then `X` is a dual
general-position set of `H` if and only if `X` satisfies the two local
conditions above.

### Proof

The graph `H` has diameter two.

First consider general position.  If a selected vertex `x` has two selected
tree neighbors `u` and `v`, then `u` and `v` are nonadjacent because a tree has
no triangle.  Thus `u-x-v` is a length-two geodesic containing three selected
vertices, so `X` is not in general position.

Conversely, any general-position violation consists of three distinct selected
vertices `u,x,v` with `x` on a `u`--`v` geodesic.  Since the diameter is two,
this geodesic has length two.  All three vertices lie on the tree side, so
`x` is adjacent in `T` to both `u` and `v`.  Thus a violation exists exactly
when some selected vertex has two selected tree neighbors.  This proves that
general position is equivalent to `Delta(T[X])<=1`.

Now put `Y=V(H)\X`.  The whole set `C` lies in `Y`.  A pair in `Y` involving a
vertex of `C` is adjacent, and so cannot witness failure of convexity.  A pair
of tree vertices in `Y` also cannot fail convexity when it is adjacent in
`T`.  Therefore convexity fails exactly when two nonadjacent unselected tree
vertices have a selected common neighbor.  In a tree, two distinct neighbors
of the same vertex are nonadjacent.  Consequently such a witness exists
exactly when some `x in X` has at least two neighbors in `V(T)\X`.  This proves
the second equivalence and hence the lemma.  QED.

### Corollary 3.2

The maximum size in the apex-avoiding branch is `beta(T)`.

## 4. Exact mixed-join formula

### Theorem 4.1

For every `r>=1` and every tree `T` of order at least three,

```text
gp_d(K_r + T) = beta(T),                         if q_2(T)=0;
gp_d(K_r + T) = max{beta(T), r+q_2(T)},          if q_2(T)>0.
```

### Proof

Every set either meets `C` or avoids `C`; these cases are disjoint and
exhaustive.  Corollaries 2.2 and 3.2 give the attainable maximum in each
existing branch.  Taking their maximum proves the formula.  QED.

### Tree specialization

A tree is triangle-free, so each clique in a two-clique partition contains at
most two vertices.  A tree of order at least three can therefore have positive
`q_2` only at orders three and four.  The unique order-three tree is `P_3`, and
it has a `2+1` clique partition.  At order four, a `2+2` clique partition is a
perfect matching; among the two trees of order four, only `P_4` has one.
Therefore

```text
q_2(T)=2 for T in {P_3,P_4}, and q_2(T)=0 otherwise.
```

Directly from the definition, `beta(P_3)=2` and `beta(P_4)=3`.  Since
`r+2>=3`, Theorem 4.1 simplifies to

```text
gp_d(K_r + T) = r+2,       if T is P_3 or P_4;
gp_d(K_r + T) = beta(T),   otherwise.
```

This is an exact formula once `beta(T)` is computed by the dynamic program
below.

## 5. A local reformulation of `beta`

For a selected vertex `x`, its selected and unselected neighbor counts add to
`deg_T(x)`.  Hence the two beta constraints are equivalent to the following:

1. a vertex of degree at least three cannot be selected;
2. a selected vertex of degree two has exactly one selected and one unselected
   neighbor;
3. a selected vertex of degree zero or one has no additional restriction.

Both implications are immediate: the original two upper bounds imply the
three cases, and the three cases give both upper bounds.  This is a structural
characterization of all beta-feasible sets, not just of maximum ones.

## 6. Rooted-tree dynamic program

Root `T` at an arbitrary vertex `rho`.  For a vertex `v`, let `T_v` be its
descendant subtree and let `Ch(v)` be its children.  Labels are binary:
`1` means selected and `0` means unselected.

For a nonroot vertex define `F_v(a,b)` as the largest number of selected
vertices in `T_v` among labelings in which `v` has label `a`, its parent has
label `b`, and every selected vertex in `T_v` satisfies both beta constraints.
The parent label is needed only to check the constraint at `v`.  For the root,
write `F_rho(a,bot)` and omit the nonexistent parent.

For a proposed vector of child labels `(t_u : u in Ch(v))`, set

```text
s = sum t_u,
d = |Ch(v)| + indicator(v is not the root),
p = 0 for the root, and p=b otherwise.
```

The recurrence is

```text
F_v(a,b) = a + max sum_{u in Ch(v)} F_u(t_u,a),
```

where the maximum is over all child-label vectors when `a=0`, and, when
`a=1`, only over vectors satisfying

```text
p+s <= 1,          d-(p+s) <= 1.
```

An impossible state has value minus infinity.  The root answer is

```text
beta(T) = max{F_rho(0,bot), F_rho(1,bot)}.
```

Recording one maximizing child-label vector in every finite state reconstructs
an attaining set by a top-down pass.

### Theorem 6.1 (correctness)

The recurrence returns `beta(T)`, and the recorded choices reconstruct a
maximum beta-feasible set.

### Proof

Proceed by induction on the height of `v`.

For a leaf, the displayed inequalities check exactly its possible parent
neighbor, so the recurrence lists precisely all feasible labels and assigns
the correct value `a`.

Assume the claim for every child of `v`.  Once the labels of `v` and its
parent are fixed, different child subtrees have no edges between them.  By the
induction hypothesis, `F_u(t_u,a)` is the exact best contribution of each
child subtree under its boundary labels.  If `v` is unselected, it has no beta
constraint of its own, so the child choices are independent and every vector
is allowed.  If `v` is selected, `p+s` and `d-(p+s)` are exactly its numbers of
selected and unselected neighbors.  The two displayed inequalities therefore
admit exactly the feasible vectors, neither omitting a feasible labeling nor
including an infeasible one.  Adding `a` counts `v` once.  Thus the recurrence
is exact for `v`.

Induction reaches the root.  Every labeling of the whole tree belongs to one
of its two root states, so their maximum is exactly `beta(T)`.  Following
recorded maximizing vectors chooses compatible exact optima in every subtree,
and hence reconstructs an attaining feasible set.  QED.

### Complexity

For an unselected state, each child independently chooses the better of two
states.  For a selected state, degree at least three is infeasible because the
two permitted neighbor counts sum to at most two.  Otherwise there are at most
two children and at most four label vectors.  There are only constantly many
states per vertex.  The total time and storage are therefore both `O(|V(T)|)`.

## 7. Boundary and counterexample audit

- `r=1` is included: the complete factor is a single universal apex, and every
  proof step above still applies.
- The theorem assumes `|V(T)|>=3`; the smaller complete-tree cases are outside
  this scoped statement and are not silently folded into it.
- Empty selected sets and empty subparts are accepted by the local conditions
  and clique conventions.  They do not affect a maximum for the present
  nonempty trees.
- If `T=K_{1,3}`, its center has degree three and is forced unselected, while
  all three leaves may be selected.  Hence `beta(T)=3`, `q_2(T)=0`, and
  `gp_d(K_r+T)=3` for every `r>=1`.  The previously preserved counterexample is
  therefore recovered rather than discarded.

The proof is independent of the bounded computations.  Computational checks
are recorded separately and are evidence, not proof.
