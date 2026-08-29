# Collaborator reading guide: dual general position in `K_r + T`

Date: 29 August 2026

## Purpose and claim status

The manuscript `drafts/mixed_join_research_note_v7.tex` gives a self-contained
classification and algorithm for the mixed join `K_r+T`, where `r>=1` and `T`
is a tree of order at least three. The result is internally proved and its
implementation has passed two bounded checks with different verification
logic. It has **not** been peer reviewed, and this project makes **no global
novelty or priority claim**. V5 incorporated the adjudicated minor corrections
from four external web-AI attempts; v6 additionally adjudicates the GLM 5.3
adversarial report and closes its valid reproducibility and exposition issues.
The two evidence records are `notes/external_ai_review_adjudication.md` and
`notes/glm_5_3_review_adjudication.md`. AI review does not substitute for human
peer review. V7 changes only the availability wording by naming the verified
public repository; the mathematics is unchanged from v6. V7 was compiled
locally through three MiKTeX-pdfTeX passes. Its
native log is warning-free, all fonts are embedded, and all 14 rendered pages
passed visual inspection.

## Result at a glance

For a tree `T`, define

$$
\beta(T)=\max\bigl\{|X|:\Delta(T[X])\le 1,
\ |N_T(x)\setminus X|\le 1\text{ for every }x\in X\bigr\}.
$$

The main formula is

$$
\operatorname{gp}_d(K_r+T)=
\begin{cases}
r+2,&T\in\{P_3,P_4\},\\
\beta(T),&\text{otherwise}.
\end{cases}
$$

Before specializing to trees, the structural form is `beta(T)` when
`q_2(T)=0` and `max{beta(T),r+q_2(T)}` when `q_2(T)>0`, where `q_2(T)`
is the maximum possible size of one class in a partition of the tree into two
induced cliques.
For trees in the stated scope, positive `q_2` occurs exactly for `P_3` and
`P_4`, where it equals two.

Every beta-feasible set has an equivalent local description: vertices of
degree at least three are not selected, and every selected degree-two vertex
has exactly one selected neighbor. Selected vertices of degree zero or one
have no further restriction. A four-boundary-state rooted-tree dynamic program
computes `beta(T)` and reconstructs a maximum set in linear time and space.

## Proof dependency map

The proof is deliberately split by whether a candidate set meets the
universal clique `C=V(K_r)`:

```text
Tian--Klavzar criterion: general position + convex complement
        |
        +-- Lemma 3.1: X meets C
        |       -> both tree parts must be cliques
        |       -> Corollary 3.2: branch maximum r + q_2(T)
        |
        +-- Lemma 3.3: X avoids C
                -> two local neighbor constraints
                -> Corollary 3.4: branch maximum beta(T)

two branch maxima -> Theorem 3.5
tree two-clique classification + beta(P_3), beta(P_4) -> Corollary 3.8
local beta characterization -> rooted-tree recurrence -> Theorem 5.1
```

No computational result is used in this chain of proofs.

## Suggested review order and high-value checks

1. **Lemma 3.1.** Verify that one selected universal vertex forces the selected
   tree part to be a clique by general position and the unselected tree part
   to be a clique by convexity. Check the converse and empty complete-factor
   subparts.

2. **Lemma 3.3.** Verify that diameter two and triangle-freeness exhaust the
   violations in the `C`-avoiding branch. Convexity quantifies over every
   geodesic: one selected-middle geodesic is fatal even if a different
   geodesic also remains outside the selected set.

3. **Lemmas 3.6--3.7 and Corollary 3.8.** Check the order-at-most-four
   two-clique classification, why `P_4` but not `K_{1,3}` qualifies, and the
   separate values `beta(P_3)=2`, `beta(P_4)=3`.

4. **Proposition 4.1.** Check degree-zero/one boundaries and the degree-two
   equivalence. Do not substitute the weaker induced-maximum-degree-one
   optimization: the depth-two complete binary tree has `beta=4`, while its
   root and four leaves give a five-vertex feasible set for the weaker problem.

5. **Theorem 5.1 and Proposition 5.2.** Check that the parent label is the only
   required boundary datum, that selected and unselected states impose the
   right constraints, and that reconstruction is compatible. For complexity,
   check the degree-at-least-three exclusion, four-vector bound, and constant
   storage per state.

6. **Introduction and limitations.** Check the separation of Jiang's two
   results, this mixed join, and the prior fan subfamily; keep every novelty
   statement conditional.

## Prior-work boundary

- Tian and Klavzar's checked criterion supplies the equivalence between dual
  general position and "general position plus convex complement."
- Jiang's v1.0.1 Zenodo preprint is the closest recent work. It covers
  `K_m circ G` and complete joins whose factors are all nonempty and
  noncomplete; it does not classify a join containing both a complete and a
  noncomplete factor.
- The fan graph `F_n=K_1+P_n` is prior work. For `n>=4`, the checked arXiv v2
  gives `gp_d(F_n)=floor(2(n+1)/3)=ceil(2n/3)`. The manuscript uses this only as
  a consistency check.
- The bounded search did not find the full all-tree, arbitrary-`r` mixed-join
  theorem. MathSciNet, Scopus, and Web of Science were not directly checked;
  therefore global openness, novelty, and priority remain `UNKNOWN`.

## Computational evidence and reproducibility

The two routes use different checking logic, but they share audit-driver
infrastructure and NetworkX tree generation; "independent" here does not mean
two completely disjoint software stacks.

The tree DP was compared with exhaustive beta-feasibility search on all 985
nonisomorphic trees of orders 3--12. The audit also made 11,003 root-invariance
comparisons and checked one reconstructed maximum set for each of the 985
trees. Separately, a definition-first shortest-path checker compared the final
mixed-join formula on all 46 nonisomorphic trees of orders 3--8 and
`r in {1,2,3,4}`, for 184 comparisons. It also checked the reconstructed
tree-side set directly on the same 184 joins. Every recorded failure count is
zero, and the current test suite reports 30 passing tests. The first route
shares the formalization of `beta(T)` and therefore tests the DP
implementation, while the second route directly tests the theorem and
reconstructed-set feasibility from shortest paths. These remain finite checks
and counterexample searches, not proofs.

Primary reproducibility files are:

- `src/mixed_join_tree.py`;
- `src/dual_gp_independent.py`;
- `experiments/audit_mixed_join_dp.py`;
- `experiments/audit_extension_candidates.py` (a runtime dependency imported
  by the main audit);
- `results/mixed_join_dp_audit.json`;
- `tests/`, `requirements-lock.txt`, and `REPRODUCIBILITY.md`;
- `artifacts/mixed_join_v6_reproducibility.zip` (the fixed archive available
  through the public repository).

## Delivery set and unresolved checks

Read in this order:

1. `drafts/mixed_join_research_note_v7.tex`, its compiler PDF at
   `output/pdf/mixed_join_research_note_v7.pdf`, and the native log identified
   in `drafts/TEX_VERSION_HISTORY.md`;
2. `notes/glm_5_3_review_adjudication.md` and
   `notes/external_ai_review_adjudication.md`;
3. `artifacts/mixed_join_v6_reproducibility.zip`;
4. `drafts/TEX_VERSION_HISTORY.md` (immutable-version and Drive mapping);
5. `proofs/mixed_join_tree.md` (earlier proof-development note);
6. `notes/mixed_join_literature_positioning.md` (query matrix and limits);
7. the uncompressed reproducibility files listed above.

For a complete internal handoff, also include `PROJECT_STATUS.md` and
`notes/research_log.md`. The historical 92-case screen is in
`results/extension_feasibility_audit.json`; it is optional unless the earlier
target-selection path or retained counterexample provenance is being audited.

V7 passes Pandoc parsing and static environment/reference checks: 35 labels are
unique, 50 `ref`/`eqref` uses and 13 citation keys resolve, 13 theorem-like
statements match 13 proofs, the environment stack is balanced, and no
submission placeholder remains. MiKTeX-pdfTeX 4.27 / pdfTeX 1.40.29 generated
the retained 14-page compiler PDF and native plain-text log. The final log has
no error, warning, overfull/underfull box, undefined reference/citation,
missing character, or rerun request. All fonts are embedded, the external
links were enumerated, and every rendered page passed visual inspection. The
exact
fan formula displayed in the version-of-record body, Jiang's future publication
status, an established equivalent name for `beta(T)`, and full subscription-
index coverage also remain `UNKNOWN`. So do a simpler nonrecursive closed form
for `beta(T)`, final publishability and journal placement, and classifications
for an arbitrary first factor, general mixed complete joins, or `P_n circ T`;
those graph directions are outside the manuscript's scope. Section 8 of
`PROJECT_STATUS.md` is the authoritative complete `UNKNOWN` inventory,
including archival-recovery questions not material to the theorem.

The most useful collaborator response would address three questions: whether
the two branch characterizations cover every geodesic/convexity failure,
whether the DP boundary state is sufficient for reconstruction and complexity,
and whether the literature-positioning language is conservative enough for an
internal draft.
