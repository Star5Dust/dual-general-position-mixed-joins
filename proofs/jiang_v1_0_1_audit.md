# Jiang v1.0.1 proof-and-reproducibility audit

Date: 2026-08-28

Source: Weiqi Jiang, *Dual General Position in Lexicographic Products with a
Complete First Factor*, Zenodo preprint v1.0.1, DOI
`10.5281/zenodo.22116770`.

This is an internal proof audit, not peer review.  The labels below mean:

- **正确**: the step follows from the stated definitions and earlier steps;
- **需要补充**: the conclusion is supportable, but an omitted argument should
  be supplied;
- **错误**: the step is false or does not establish its conclusion;
- **UNKNOWN**: the available evidence does not settle the step.

## 1. Source integrity and visual verification

- The PDF was restored directly from Zenodo record `22116770` because the local
  `papers_local/` directory was unexpectedly empty at the start of this audit.
- PDF SHA-256:
  `ADB5DB88FD600C1AB031B51BBB9FC1771B905A7CD800D22E219184E05B7ACA34`.
- Supplement ZIP SHA-256:
  `604A86672EE6B6E7F8BE801EABC069C13806F08767CF5782CE71AC22F553BE84`.
- The PDF has 10 pages.  Pages 2--5, containing the definitions and the complete
  proofs of Theorems 3.1--3.2 and Proposition 3.3, were rendered with Poppler at
  160 dpi and visually inspected.
- Plain-text extraction drops some complement bars.  Visual inspection confirms
  that Proposition 3.3 consistently uses the complement graph `\bar G`.  This is
  a text-extraction artifact, not an error in the PDF.

## 2. Definitions and scope

| ID | Audited statement | Status | Reason |
|---|---|---|---|
| D1 | Graphs are finite and simple; the main result assumes nonempty `G` and `m >= 2`. | **正确** | These hypotheses make `K_m circ G` finite, nonempty, and connected even when `G` is disconnected. |
| D2 | Dual general position is checked as general position of `X` plus convexity of its complement. | **正确** | This is the verified Tian--Klavzar characterization on the connected product graph. |
| D3 | Empty and singleton convex sets, and sets of at most two vertices in general position, are treated vacuously. | **正确** | The pair/triple quantifiers have no counterexample in these sizes. |
| D4 | An admissible side `A` is one for which both `G[A]` and `G[V(G)\A]` are complete. | **正确** | The convention that graphs of order zero or one are complete is explicitly stated and is used consistently. |
| D5 | `q_2(G)` is the largest cardinality of an admissible side, and is zero when no side exists. | **正确** | Since `G` is finite, the maximum exists whenever the admissible family is nonempty. |

## 3. Theorem 3.1: layerwise classification

Let `H = K_m circ G`, let `X_i` be the selected vertices in layer `i`, and let
`T_i = V(G) \ X_i`.

| ID | Proof step | Status | Audit |
|---|---|---|---|
| 3.1-1 | Distinct layers are completely joined; any two vertices in one layer have a common neighbor in another layer. | **正确** | This follows directly from the lexicographic-product adjacency rule and `m >= 2`; nonemptiness of `G` supplies the common neighbor. |
| 3.1-2 | Therefore `H` is connected, and `X = empty` is feasible. | **正确** | Cross-layer adjacency connects the product; the whole vertex set is convex and the empty set is in general position. |
| 3.1-3 | If `G` is complete, the required clique conditions hold in every layer. | **正确** | Every induced subgraph of a complete graph is complete, including empty and singleton induced subgraphs.  In this branch `H` itself is complete, so in fact every `X` is feasible. |
| 3.1-4 | If `G` is noncomplete and nonempty dual set `X` misses a layer, convexity fails. | **正确** | Choose nonadjacent `u,v` in the missed layer and any `x in X`.  The path `(i,u)-x-(i,v)` has length two and is geodesic; its endpoints are outside `X` and its middle is in `X`. |
| 3.1-5 | Hence every layer is met by `X` in the noncomplete branch. | **正确** | This is exactly the contradiction in 3.1-4.  It does not assume that `G` is connected. |
| 3.1-6 | Every `G[X_i]` is complete. | **正确** | If nonadjacent selected `u,v` occurred in layer `i`, a selected vertex in any other, now known nonempty, layer would lie between them on a length-two geodesic, contradicting general position. |
| 3.1-7 | Every `G[T_i]` is complete. | **正确** | The identical length-two construction has endpoints in the complement and a selected middle vertex, contradicting convexity of the complement. |
| 3.1-8 | Conversely, layerwise clique conditions make `X` a clique in `H`. | **正确** | Same-layer pairs are adjacent by `G[X_i]` being complete and cross-layer pairs are adjacent by the product definition. |
| 3.1-9 | They also make `V(H)\X` a clique. | **正确** | Apply the same argument to the `T_i`. |
| 3.1-10 | A clique is in general position and is convex in the ambient graph. | **正确** | Two distinct vertices in the clique are adjacent, so their distance is one and their only geodesic is their edge. |
| 3.1-11 | Therefore the layer conditions are sufficient. | **正确** | 3.1-8 gives general position; 3.1-9--10 give convexity of the complement. |

Conclusion for Theorem 3.1: **correct as stated**.  No omitted hypothesis or
logical gap was found.

## 4. Theorem 3.2: maximum-value formula

| ID | Proof step | Status | Audit |
|---|---|---|---|
| 3.2-1 | A nonempty feasible `X` has every `X_i` admissible. | **正确** | This is Theorem 3.1. |
| 3.2-2 | Summing `|X_i| <= q_2(G)` gives `|X| <= m q_2(G)`. | **正确** | Layers are disjoint and there are exactly `m` of them. |
| 3.2-3 | The same upper bound holds for `X = empty`. | **正确** | `q_2(G) >= 0`, so `0 <= m q_2(G)`. |
| 3.2-4 | If `q_2(G) > 0`, repeating a maximum admissible side in every layer attains the upper bound. | **正确** | The layer conditions of Theorem 3.1 hold, and the constructed set has size `m q_2(G)`. |
| 3.2-5 | If `q_2(G) = 0`, the admissible family is empty. | **正确** | A nonempty admissible side would have positive size.  If the only possible side were empty, its admissibility would force `G` complete, making the full nonempty vertex set admissible and giving positive `q_2`. |
| 3.2-6 | Thus only the empty dual set exists when `q_2(G) = 0`. | **正确** | Theorem 3.1 rules out every nonempty set when no layer side is admissible. |
| 3.2-7 | For `m = 1` and connected `G`, `K_1 circ G` is isomorphic to `G`. | **正确** | This is a separate identity, not an extension of the `m >= 2` proof. |

Conclusion for Theorem 3.2: **correct as stated**.  The proof handles the zero
case rather than silently assuming that an admissible side exists.

## 5. Proposition 3.3: complement-bipartition translation

| ID | Proof step | Status | Audit |
|---|---|---|---|
| 3.3-1 | `G[A]` is complete iff `A` is independent in `\bar G`, and similarly for its complement. | **正确** | Complementation exchanges edges and nonedges between distinct vertices. |
| 3.3-2 | Hence admissible sides are precisely the two sides of bipartitions of `\bar G`, with an empty side allowed. | **正确** | The two sides partition the full vertex set and are both independent in `\bar G`. |
| 3.3-3 | On each connected bipartite component, the two color classes are unique up to swapping. | **正确** | This is the standard uniqueness of a bipartition on a connected bipartite graph. |
| 3.3-4 | An isolated complement vertex contributes side sizes `(1,0)`. | **正确** | The vertex may be assigned to either global side; the stated rooted convention records the two orientations. |
| 3.3-5 | All admissible sides arise by choosing one color class independently in every component. | **正确** | Restrictions of a global bipartition give these choices, and the componentwise choices combine to a global bipartition. |
| 3.3-6 | Maximizing independently gives `q_2(G) = sum_j max(a_j,b_j)`. | **正确** | The total size is the sum of component contributions with no cross-component constraint. |
| 3.3-7 | `q_2(G) > 0` iff `\bar G` is bipartite for nonempty `G`. | **正确** | An admissible side gives a bipartition; conversely a bipartition exists and at least one component contributes one vertex. |

Conclusion for Proposition 3.3: **correct as stated**.

## 6. Boundary-case audit

| Case | Status | Result |
|---|---|---|
| `X = empty` | **正确处理** | Always feasible; explicitly separated because the layer-clique conditions need not hold for it. |
| `X = V(H)` | **正确处理** | Feasible exactly in the complete-product branch; otherwise the selected part of a layer is noncomplete and the classification rejects it. |
| `G = K_1` | **正确处理** | `q_2(G)=1`, so the formula gives `gp_d(K_m)=m`. |
| Complete `G` | **正确处理** | `K_m circ G` is complete and `q_2(G)=|V(G)|`; the value is the full product order. |
| Noncomplete `G` | **正确处理** | The missed-layer argument is valid because a nonadjacent pair exists. |
| Disconnected `G` | **正确处理** | No step requires base connectivity; the product remains connected for `m >= 2`. |
| `m = 1` | **正确排除** | The layer argument needs another layer.  The paper states only the separate isomorphism identity for connected `G`. |
| Empty `G` | **正确排除** | The theorem explicitly assumes a nonempty base graph. |

## 7. Supplement reproducibility audit

The ZIP was extracted only after its entry list was checked for rooted or parent
traversal paths.  Its `MANIFEST.sha256` verified successfully for all seven
payload files.

Environment:

- Windows 11, build 26100;
- project virtual environment, CPython 3.13.5;
- supplement requirement: Python 3.10 or newer, standard library only.

Commands run from the extracted supplement root:

```powershell
C:\Users\yyt\Desktop\ai4math_dual_gp\.venv\Scripts\python.exe -m unittest -v supplement/test_dual_gp.py
C:\Users\yyt\Desktop\ai4math_dual_gp\.venv\Scripts\python.exe supplement\run_exhaustive.py
```

Results:

- 36 of 36 supplement tests passed; unittest-reported time 2.333 seconds,
  measured wall time 2.596 seconds.
- Driver exit code 0; internal elapsed time 2.040786 seconds, measured wall time
  2.113 seconds.
- Fixed family counts matched `expected-report.json`.
- Total comparisons: `771 + 43 + 75 + 11 + 64 + 100 = 1,064`.
- Every mismatch field was zero and no mismatch details were emitted.

The supplement's direct checker enumerates selected subsets and evaluates
shortest-path general position and complement convexity.  Its closed-form path
instead two-colors complement components.  Thus the direct search does not call
the formula decoder and is independent in that algorithmic sense.  Both paths
still share the same bit-mask graph representation and product constructor, so
the supplement alone is not a fully separate implementation.  The project
implementation below removes that shared-representation limitation.

## 8. Project-independent implementation

The independent implementation in `src/dual_gp_independent.py` differs
structurally from the supplement:

- adjacency is stored with `frozenset` neighbor collections, not integer masks;
- product vertices are explicit `(layer, vertex)` pairs;
- the direct verifier uses breadth-first distances and Python set combinations;
- the formula verifier enumerates all vertex partitions and checks that both
  sides induce cliques; it does not two-color the complement;
- no supplement module is imported.

Verification results on CPython 3.13.5:

- project tests: 18 passed;
- maximum-value comparisons: 217, with zero mismatches;
- set-by-set Theorem 3.1 classification comparisons: 4,780, with zero
  mismatches;
- experiment internal elapsed time: about 0.398 seconds.

The exact machine-readable report is in
`results/jiang_v1_0_1_independent_report.json`.

## 9. Overall judgment

- Theorems 3.1--3.2 and Proposition 3.3: **correct** under their stated
  hypotheses.
- Missing proof steps in the audited results: **none found**.
- Counterexamples or computational mismatches: **none found**.
- Supplement reproduction: **successful** in the project environment.
- Independent small-instance reproduction: **successful**.
- Peer-reviewed status: **UNKNOWN / no peer-reviewed version identified in the
  completed literature search**.

The formula

```text
gp_d(K_m circ G) = m q_2(G),  for nonempty finite simple G and m >= 2,
```

is therefore accepted as an internally proof-verified result of this project.
The zero-mismatch experiments support this judgment but are not themselves the
proof.
