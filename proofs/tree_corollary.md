# Independently derived tree corollary

Date: 2026-08-28

## Statement

Let `T` be a finite nonempty tree and let `m >= 2`.  Then

```text
gp_d(K_m circ T) = m,    if T = K_1;
gp_d(K_m circ T) = 2m,   if T is K_2, P_3, or P_4;
gp_d(K_m circ T) = 0,    for every other tree T.
```

This statement is a direct corollary of the independently audited formula
`gp_d(K_m circ G) = m q_2(G)` and the elementary structure of cliques in a
tree.  It is a proof, not an inference from the computational experiments.

## Proof

An admissible side for a graph `G` is a set `A` such that both `G[A]` and
`G[V(G)\A]` are complete.  Thus `q_2(T)>0` precisely when the vertices of `T`
can be partitioned into two (possibly empty) cliques.

A tree has no triangle.  Therefore every clique in a tree has at most two
vertices.  If the vertices of `T` can be partitioned into two cliques, then
`|V(T)| <= 4`.

- If `T=K_1`, its full vertex set is an admissible side, so `q_2(T)=1`.
- If `T=K_2`, its full vertex set is a clique, so `q_2(T)=2`.
- The only three-vertex tree is `P_3`.  Its edge and remaining singleton form
  two cliques, so `q_2(P_3)=2`.
- Suppose `T` has four vertices.  An admissible partition must have two
  vertices on each side, and each side must be an edge.  Hence `T` must have a
  perfect matching.  Two disjoint matching edges together with the third edge
  required to make a four-vertex tree connected form `P_4`.  Conversely, the
  two end edges of `P_4` give the required partition, so `q_2(P_4)=2`.  The
  other four-vertex tree, `K_{1,3}`, has no perfect matching and therefore has
  `q_2=0`.
- If `|V(T)| >= 5`, two cliques of size at most two cannot cover all vertices,
  so `q_2(T)=0`.

Multiplying these values by `m` in the audited general formula proves the
statement.

The case `m=1` is separate because `K_1 circ T` is isomorphic to `T`; it is not
covered by the complete-first-factor formula above.
