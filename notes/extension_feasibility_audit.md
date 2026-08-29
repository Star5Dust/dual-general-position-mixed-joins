# Bounded literature-and-feasibility audit for post-Jiang extensions

Date: 2026-08-28

## 1. Scope and status labels

This audit performs only the target-selection stage required by
`PROJECT_STATUS.md`.  It starts from the two directions explicitly left outside
Jiang v1.0.1:

1. mixed complete joins containing complete and noncomplete factors;
2. lexicographic products with a noncomplete first factor `F`.

It does not claim novelty, priority, or a proof that any candidate is open in
the entire literature.  The labels below have the following meanings:

- **LITERATURE FACT**: stated in a checked source;
- **DIRECT LOGICAL DEDUCTION**: derived from checked definitions or theorems;
- **COMPUTATIONAL EVIDENCE**: obtained by exhaustive search on the stated finite
  matrix and not a proof;
- **NOT FOUND IN THIS BOUNDED AUDIT**: a search result with explicit coverage
  limits, not an openness theorem;
- `UNKNOWN`: the available evidence does not settle the issue.

## 2. Exact boundary left by Jiang v1.0.1

### Literature facts

Jiang Theorem 5.1 treats

```text
H = G_1 + ... + G_s,
```

when `s >= 2` and every factor is nonempty and noncomplete.  The theorem gives
a layer/factor classification and the corresponding `gp_d` formula.  The
complement bars in its bipartiteness condition were visually verified on PDF
page 8; plain-text extraction drops some bars.

PDF page 9 then states explicitly that:

- the join of all-complete factors is complete and handled separately;
- mixed joins with both complete and noncomplete factors are not classified;
- arbitrary lexicographic products `F circ G` are not classified.

The conclusion asks for broader first factors `F` whose dual
general-position sets in `F circ G` have an explicit layer description.

### Current record check

The Zenodo API record `22116770` was checked again on 2026-08-28.  It still
reports title *Dual General Position in Lexicographic Products with a Complete
First Factor*, version `v1.0.1`, publication date 2026-08-27, DOI
`10.5281/zenodo.22116770`, concept DOI `10.5281/zenodo.22081165`, and resource
type `publication/preprint`.  No related journal identifier was present in the
record.  This is only a metadata check; future revisions or peer review remain
`UNKNOWN`.

## 3. Bounded literature search

### Fresh query matrix

Search cutoff: 2026-08-28.

| Source | Query or check | Result used in this audit |
|---|---|---|
| arXiv API | exact phrase `"dual general position"` | 3 records: the 2025 foundation, the strong/lexicographic product paper, and the removal paper |
| arXiv API | exact phrase plus `lexicographic` | 1 record: the strong/lexicographic product paper |
| arXiv API | exact phrase plus `join` | 0 records |
| DataCite API | `titles.title:"dual general position"` | 3 records, all the Jiang concept/version records |
| DataCite API | the title-field phrase plus `lexicographic` | the same 3 Jiang records |
| DataCite API | the title-field phrase plus `join` | 0 records |
| General web search | exact combinations with `mixed joins`, `arbitrary first factor`, `K_r`, `tree`, `path`, and `lexicographic product` | only already-known foundation/product/removal sources and irrelevant uses of the words were identified |
| Local survey v5 | Section 3.5 and exact `dual`/`join` screening | covers the foundation, product paper, Sierpiński graphs, glued trees, and removal work; no mixed-join or path-first dual formula was identified |
| OpenAlex | fresh exact-phrase request | unavailable in this audit because every attempt returned HTTP 429; no zero count is inferred |
| Semantic Scholar | exact/narrow requests | one request returned HTTP 429 and another was heavily noisy; it added no new relevant paper |

The earlier project-wide topic search is preserved in
`notes/literature_notes.md`, but its formerly referenced detailed file
`notes/literature_search_log.md` is still missing.  This audit does not invent
or reconstruct that missing log.

### Literature conclusion and limits

No paper directly determining either `gp_d(K_r + T)` or
`gp_d(P_n circ T)` was found in this bounded audit.  This is labelled **NOT
FOUND IN THIS BOUNDED AUDIT**, not “proved open.”

Coverage limitations include indexing delay for the very recent Jiang
preprint, the OpenAlex and Semantic Scholar failures above, lack of direct
MathSciNet/Scopus/Web of Science access, and the possibility of papers whose
title/abstract does not use the queried terminology.  A systematic novelty
claim is therefore not authorized.

## 4. Candidate screening

Assume throughout that graphs are finite and simple and that `+` denotes the
complete join.

| Candidate | Direct-coverage audit | Feasibility verdict |
|---|---|---|
| `gp_d(P_3 circ T)` for noncomplete trees `T` | **Already covered.** Since `P_3 = K_1 + 2K_1`, associativity of graph substitution gives `P_3 circ T` as the join of `T` and two disjoint copies of `T`.  Both join factors are nonempty and noncomplete, so Jiang Theorem 5.1 applies. | Reject as an extension target. |
| `gp_d(K_r + T)` for `r >= 1` and trees `T` of order at least 3 | Jiang Theorem 5.1 excludes the complete factor `K_r`; the all-complete branch does not apply because `T` is noncomplete.  The verified foundation gives a general convex-complement test but no formula for this family. | **Select.** It is the smallest explicit mixed-join gap and already shows nontrivial behavior. |
| `gp_d(P_n circ T)` for `n >= 4` and trees `T` of order at least 3 | Jiang's complete-first-factor theorem does not apply.  The noncomplete-factor join theorem does not supply a decomposition because the complement of `P_n` is connected for `n >= 4`.  Core-paper Theorem 5.8(i) fails because paths and trees have simplicial leaves; Theorem 5.8(ii) fails because `T` is noncomplete. | Viable but not selected.  Keep dormant to avoid parallel expansion. |

## 5. Minimal mathematics for the selected mixed join

Let `C = V(K_r)`, let `T` be a tree of order at least 3, and let
`H = K_r + T`.  Define

```text
beta(T) = max |X|,
```

where the maximum is over `X subseteq V(T)` such that every `x in X` has

```text
at most one neighbor in X, and
at most one neighbor in V(T) \ X.
```

Equivalently, `Delta(T[X]) <= 1` and
`|N_T(x) \ X| <= 1` for every selected vertex `x`.

### Feasibility reduction — direct logical deduction

The following is a checked proof skeleton, but it has not yet received a
separate formal proof note or independent implementation audit and is therefore
not promoted to a canonical theorem at this stage.

1. Suppose a nonempty dual set `X` meets `C`.  A selected complete-factor
   vertex lies on a length-two geodesic between any two nonadjacent tree
   vertices.  General position therefore forces `T[X intersect V(T)]` to be
   complete, while convexity of the complement forces the unselected tree side
   to be complete.  Conversely these two clique conditions make both `X` and
   its complement cliques.  A maximum set in this branch contains all `r`
   vertices of `K_r` and has size `r + q_2(T)`.  This branch exists only when
   `q_2(T) > 0`.
2. Suppose `X` avoids `C`.  The graph `H` has diameter two.  Because a tree is
   triangle-free, `X` is in general position exactly when no selected tree
   vertex has two selected neighbors, that is, `Delta(T[X]) <= 1`.  The
   complement contains all of `C`; it is convex exactly when no selected tree
   vertex is a common neighbor of two unselected tree vertices, that is, when
   each selected vertex has at most one unselected tree neighbor.  Hence the
   maximum in this branch is `beta(T)`.

The resulting target reduction is

```text
gp_d(K_r + T) = max{beta(T), r + q_2(T)},  if q_2(T) > 0;
gp_d(K_r + T) = beta(T),                   if q_2(T) = 0.
```

For trees of order at least 3, the already proved tree corollary says
`q_2(T) > 0` only for `P_3` and `P_4`.  Thus the unsolved substance of the
selected target is to characterize and compute `beta(T)` on arbitrary trees,
not to reuse the complete-first-factor formula.

## 6. Preserved counterexample

Take `T = K_{1,3}`.  Its three leaves form a dual general-position set of
`K_r + T`: no third leaf lies on a geodesic between two leaves, and the
complement, consisting of `K_r` plus the star center, is a clique.  The center
cannot belong to an apex-avoiding feasible set because it has three neighbors,
and a set meeting `K_r` would require a two-clique partition of `T`, which does
not exist.  Therefore

```text
gp_d(K_r + K_{1,3}) = 3  for every r >= 1,
q_2(K_{1,3}) = 0.
```

In particular, at `r = 4` the naive expression `r + q_2(T)` gives 4 while the
correct value is 3.  This is a mathematical counterexample to both of the
following unsupported extrapolations:

- every maximum dual set must meet the complete factor;
- Jiang's join formula extends to mixed joins by simply adding a complete
  factor contribution.

The counterexample and its reproduction data are retained in
`results/extension_feasibility_audit.json`.

## 7. Bounded computational evidence

Script:

```text
experiments/audit_extension_candidates.py
```

Command:

```powershell
.\.venv\Scripts\python.exe .\experiments\audit_extension_candidates.py --output .\results\extension_feasibility_audit.json
```

Environment: CPython 3.13.5, NetworkX 3.6.1.  The direct side reuses the
definition-first shortest-path checker in `src/dual_gp_independent.py`.

Results:

- mixed joins: all 23 nonisomorphic trees of orders 3 through 7, with
  `r = 1,2,3,4`, for 92 comparisons total;
- the direct value and the two-branch reduction above agreed in all 92 cases;
- mismatch count: 0;
- arbitrary-first-factor screening: 17 small products with first factor
  `P_4`, `P_5`, or `P_6` and labelled noncomplete second factors of order 2 or
  3; all 17 direct values were zero;
- the 17 zeros are not promoted to a conjecture or proof.

Project test command after adding the bounded audit implementation:

```powershell
.\.venv\Scripts\python.exe -m pytest -q tests
```

Result: 23 passed.  These computations support feasibility and target choice;
they do not prove the mixed-join reduction or any path-first formula.

## 8. Unique selected problem and verification route

### Selected restricted problem

For `r >= 1` and a finite tree `T` of order at least 3, determine
`gp_d(K_r + T)` by giving a rigorous structural characterization and an exact,
polynomial-time computable description of `beta(T)`, together with a
classification or reconstruction method for maximum dual sets.

### Why this one

- It lies exactly in Jiang's explicitly excluded mixed-join case.
- Existing checked theorems do not directly determine it.
- The preserved star counterexample shows that it is not a cosmetic extension
  of `q_2`.
- The two-branch reduction isolates one concrete tree parameter and gives a
  bounded proof and verification route.

### Unique next step

Formalize and independently verify the two-branch mixed-join lemma, then build
a rooted-tree dynamic program for `beta(T)` with exhaustive tests against the
definition-first checker on a bounded family of nonisomorphic trees.  Do not
start the dormant `P_n circ T` direction in parallel.

No novelty claim and no formal conjecture are made at the end of this audit.

## 9. Post-selection completion update (2026-08-28)

The unique next step from this historical target-selection audit has now been
completed.  The provisional two-branch reduction was promoted to a formally
proved project theorem in `proofs/mixed_join_tree.md`.  The proof includes both
directions of each branch, the `q_2(T)=0` boundary, `r=1`, and the preserved
`K_{1,3}` counterexample.

The exact result is

```text
gp_d(K_r + T) = r+2,       if T is P_3 or P_4;
gp_d(K_r + T) = beta(T),   otherwise,
```

for `r>=1` and trees of order at least three.  The note also proves the local
characterization of beta-feasible sets and a rooted-tree DP with `O(|V(T)|)`
time and storage that reconstructs a maximum set.

The independent implementation is `src/mixed_join_tree.py`.  The bounded
audit in `results/mixed_join_dp_audit.json` records 985 DP-versus-subset-search
comparisons on all nonisomorphic trees of orders 3--12, 11,003 rerooting
comparisons, and 184 formula-versus-shortest-path comparisons for tree orders
3--8 and `r=1,2,3,4`; all mismatch and reconstruction-failure counts are zero.
These computations verify the implementation but are not the proof.

The earlier “unique next step” in Section 8 is therefore historical and has
been superseded by `PROJECT_STATUS.md`.
