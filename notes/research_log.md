# Research log

## 2026-08-28 — Jiang v1.0.1 proof-and-reproducibility audit

### Starting state and discrepancies

- Read `AGENTS.md` and the complete `PROJECT_STATUS.md` before acting.
- `PROJECT_STATUS.md` named this audit as the unique next task.
- The status file said that six source files and two detailed log files were
  present.  At audit start, `papers_local/` was empty,
  `notes/research_log.md` did not exist, and
  `notes/literature_search_log.md` did not exist.  No earlier detailed content
  was reconstructed or invented.

### Source restoration and integrity

- Queried the Zenodo API record `https://zenodo.org/api/records/22116770`.
- Restored the exact v1.0.1 PDF and supplement ZIP from the record's file
  endpoints into ignored `papers_local/` paths.
- PDF SHA-256:
  `ADB5DB88FD600C1AB031B51BBB9FC1771B905A7CD800D22E219184E05B7ACA34`.
- ZIP SHA-256:
  `604A86672EE6B6E7F8BE801EABC069C13806F08767CF5782CE71AC22F553BE84`.
- MD5 values matched the live Zenodo record:
  `ec460cc54eb00426b564476da3084c1b` for the PDF and
  `fa70a97d33f8a1a514c0b7f2a166d752` for the ZIP.
- `pdfinfo` reported 10 unencrypted letter-size pages, PDF version 1.7.
- Used `pdftotext -layout` for navigation and `pdftoppm -png -r 160` for
  visual verification of pages 2--5.  The PDF visibly contains the complement
  bars that text extraction omits.

### Proof audit

- Audited definitions, Theorems 3.1--3.2, and Proposition 3.3 step by step.
- Explicitly checked necessity, sufficiency, the empty selected set, the full
  selected set, complete and noncomplete bases, disconnected bases, `G=K_1`,
  empty-base exclusion, and the separate `m=1` identity.
- Every audited proof step was marked **正确**.  No step was marked
  **需要补充**, **错误**, or `UNKNOWN`.
- The reason disconnected bases cause no problem is that `K_m circ G` is
  connected for `m>=2`, while the proof only needs a nonadjacent base pair in
  the noncomplete branch.
- Full audit: `proofs/jiang_v1_0_1_audit.md`.

### Supplement reproduction

- Listed ZIP entries before extraction; no rooted path or `..` traversal entry
  was present.
- Extracted to the isolated directory
  `tmp/jiang_supplement_audit_20260828/`.
- Verified all seven entries in `MANIFEST.sha256`: all matched.
- Environment: Windows 11 build 26100, project CPython 3.13.5.  The supplement
  uses only the standard library and requires Python 3.10 or newer.
- Successful unit command:

  ```powershell
  C:\Users\yyt\Desktop\ai4math_dual_gp\.venv\Scripts\python.exe -m unittest -v supplement/test_dual_gp.py
  ```

  Result: 36/36 passed; unittest time 2.333 s; measured wall time 2.596 s.
- Successful driver command:

  ```powershell
  C:\Users\yyt\Desktop\ai4math_dual_gp\.venv\Scripts\python.exe supplement\run_exhaustive.py
  ```

  Result: exit code 0; 1,064 comparisons; every mismatch count zero; internal
  time 2.040786 s; measured wall time 2.113 s.
- Saved the actual driver report as
  `results/jiang_v1_0_1_supplement_report.json`.
- A first command attempt used paths relative to the wrong working directory
  and therefore did not run the manifest check or tests.  It produced only
  path-not-found errors.  The corrected commands above are the ones associated
  with the reported results.

### Independent implementation

- Installed and recorded the `requirements.txt` environment:
  Python 3.13.5, NetworkX 3.6.1, NumPy 2.5.2, pandas 3.0.5, SymPy 1.14.0,
  pytest 9.1.1, Matplotlib 3.11.1.
- Implemented `src/dual_gp_independent.py` without importing the supplement.
- Structural independence choices:
  explicit neighbor `frozenset`s instead of integer masks; explicit
  `(layer,vertex)` product vertices; fresh BFS distance tables; direct
  definition checks; formula evaluation by exhaustive two-clique partitions
  rather than complement two-coloring.
- Added `tests/test_dual_gp_independent.py`.
- Project-only test command:

  ```powershell
  .\.venv\Scripts\python.exe -m pytest -q tests
  ```

  Result: 18 passed in 0.02 s.
- Added `experiments/audit_jiang_v1_0_1.py` and ran:

  ```powershell
  .\.venv\Scripts\python.exe .\experiments\audit_jiang_v1_0_1.py --output .\results\jiang_v1_0_1_independent_report.json
  ```

- A first driver attempt failed before any comparison with
  `ModuleNotFoundError: src`; the driver was patched to add its repository root
  to `sys.path`, then rerun successfully.
- Successful independent report:
  217 maximum-value comparisons, 0 mismatches; 4,780 set-level Theorem 3.1
  classification comparisons, 0 mismatches; internal elapsed time about
  0.398 s.  Families include all labelled graphs through order 4 for `m=2`,
  through order 3 for `m=3`, all 125 labelled trees of order 5 for `m=2`, and
  six named boundary cases.
- These computations are evidence and are not used as the proof.

### Independent tree corollary

- After the general theorem passed the proof audit, independently proved that
  a tree can be partitioned into two cliques only for
  `K_1`, `K_2`, `P_3`, and `P_4`.
- The key argument is that a tree is triangle-free, so each clique has at most
  two vertices.  At order four, two two-vertex clique parts amount to a perfect
  matching, which occurs for `P_4` but not `K_{1,3}`.
- The resulting exact formula is:
  `m` for `K_1`, `2m` for `K_2`, `P_3`, or `P_4`, and `0` for all other trees,
  for `m>=2`.
- Full proof: `proofs/tree_corollary.md`.

### Stage conclusion

- Theorems 3.1--3.2 and Proposition 3.3 passed the internal proof audit.
- Supplement reproduction passed.
- A structurally independent second implementation found no mismatch.
- No counterexample was found.
- The formula is internally accepted as proved, but Jiang v1.0.1 remains a
  preprint and no peer-reviewed version has been identified.
- No novelty or priority claim is made for this project.

### Unique next step

Conduct a bounded literature-and-feasibility audit of extension directions not
covered by the complete-first-factor theorem, beginning with arbitrary first
factors `F` in `F circ G` and mixed complete joins.  Select exactly one
well-posed unresolved target before starting new proof or enumeration work.

## 2026-08-28 — Post-Jiang bounded extension audit and target selection

### Starting state and scope

- Read the complete `PROJECT_STATUS.md` and `AGENTS.md` before acting.
- The unique task was target selection only: literature-audit Jiang's two
  excluded directions, screen at least two concrete restricted problems, run
  only minimal feasibility checks, preserve counterexamples, and select one
  target.
- The missing historical file `notes/literature_search_log.md` was not
  reconstructed or treated as read.

### Jiang source boundary

- Used the restored Zenodo v1.0.1 PDF and its existing extracted text.
- Rendered PDF pages 8 and 9 at 160 dpi and visually checked them.
- Page 8 confirms that Theorem 5.1 assumes `s >= 2` and all join factors are
  nonempty and noncomplete.  The complement bars in the bipartiteness
  condition are visible; their absence in extracted text is an extraction
  artifact.
- Page 9 explicitly says that all-complete joins are handled separately, while
  mixed complete/noncomplete joins and arbitrary `F circ G` are not
  classified.  It asks for broader first factors with an explicit layer
  description.
- Rechecked `https://zenodo.org/api/records/22116770`: version `v1.0.1`,
  publication date 2026-08-27, DOI `10.5281/zenodo.22116770`, concept DOI
  `10.5281/zenodo.22081165`, type `publication/preprint`, with no related
  journal identifier in the record.

### Fresh bounded literature search

- Web search query families combined the exact phrase `dual general position`
  with `mixed joins`, `arbitrary first factor`, `lexicographic product`,
  `K_r`, `tree`, `path`, `cone`, and `universal vertex`.
- arXiv API exact phrase `"dual general position"` returned three records:
  Tian--Klavzar foundation, the strong/lexicographic product paper, and the
  vertex/edge-removal paper.  Adding `lexicographic` returned only the product
  paper.  Adding `join` returned zero.
- DataCite field query `titles.title:"dual general position"` returned three
  records, all Jiang concept/version records.  Adding `lexicographic` returned
  those same records; adding `join` returned zero.
- Screened the local survey v5 Section 3.5.  It covers the foundation, product,
  Sierpinski, glued-tree, and removal work but did not supply a mixed-join or
  path-first dual formula.
- OpenAlex fresh searches all returned HTTP 429.  The failed calls were not
  recorded as zero results.
- Semantic Scholar had one HTTP 429 and one noisy result set; the only relevant
  hits in the noisy set were already-known sources.
- Crossref's free-text/title ranking was too broad to provide a meaningful
  negative count; it did identify the known product paper but no screened
  exact mixed-join result.
- Search conclusion: no direct formula for `gp_d(K_r + T)` or
  `gp_d(P_n circ T)` was found **in this bounded audit**.  This is not an
  openness or novelty proof.

### Candidate coverage audit

1. Rejected preliminary candidate `P_3 circ T` for noncomplete trees.  Since
   `P_3 = K_1 + 2K_1`, the product decomposes as the join `T + 2T`; its two
   factors are nonempty and noncomplete, so Jiang Theorem 5.1 directly covers
   it.
2. Candidate A: determine `gp_d(K_r + T)` for `r >= 1`, tree order at least
   three.  It lies exactly in the mixed complete/noncomplete gap and was
   selected.
3. Candidate B: determine `gp_d(P_n circ T)` for `n >= 4`, tree order at least
   three.  It is not directly covered by the complete-first-factor, noncomplete
   join, no-simplicial-factor, or complete-second-factor theorems.  It remains
   viable but was left dormant.

### Minimal direct mathematics

- For `H = K_r + T`, split a dual set `X` according to whether it meets the
  complete factor.
- If it meets `K_r`, general position forces the selected tree side to be a
  clique and complement convexity forces the unselected tree side to be a
  clique.  The maximum branch value is `r + q_2(T)`, and the branch exists only
  when `q_2(T) > 0`.
- If it avoids `K_r`, the diameter-two and triangle-free structure gives two
  local conditions: every selected vertex has at most one selected tree
  neighbor and at most one unselected tree neighbor.  Their maximum cardinality
  defines `beta(T)`.
- This yields the provisional two-branch reduction recorded in
  `notes/extension_feasibility_audit.md`.  It is a checked logical proof
  skeleton, not yet a separately audited canonical proof.
- Preserved exact counterexample: for every `r >= 1`, the three leaves of
  `K_{1,3}` form a maximum dual set of `K_r + K_{1,3}`, so the value is 3 while
  `q_2(K_{1,3}) = 0`.  At `r = 4`, the naive expression `r + q_2(T)` would give
  4, so that extrapolation is false.

### Reproducible bounded computation

- Initial one-off feasibility checks gave:
  `K_r + P_3` values `r+2` for `r=1,2,3`;
  `K_r + P_4` values `r+2` for `r=1,2,3`;
  `K_r + K_{1,3}` values 3 for `r=1,2,3`; and zero for
  `P_4 circ P_3`, `P_4 circ P_4`, and `P_4 circ K_{1,3}`.
- To satisfy the project reproducibility and testing rules, consolidated the
  checks into `experiments/audit_extension_candidates.py` and added
  `tests/test_extension_feasibility.py`.
- The script deliberately remains bounded and imports the existing
  definition-first shortest-path checker; it is not a large general
  enumerator.
- Reproduction command:

  ```powershell
  .\.venv\Scripts\python.exe .\experiments\audit_extension_candidates.py --output .\results\extension_feasibility_audit.json
  ```

- Environment: CPython 3.13.5, NetworkX 3.6.1.
- Mixed-join matrix: all 23 nonisomorphic trees of orders 3--7 and
  `r=1,2,3,4`; 92 direct-versus-reduction comparisons, zero mismatches.
- Path-first screen: 17 products using `P_4`, `P_5`, or `P_6` and the smallest
  labelled noncomplete second factors; every direct value was zero.  These
  zeros were not promoted to a conjecture.
- Machine-readable report:
  `results/extension_feasibility_audit.json`.
- Test command:

  ```powershell
  .\.venv\Scripts\python.exe -m pytest -q tests
  ```

- Result after the new tests: 23 passed in 0.15 seconds.

### Stage conclusion

- The required bounded literature and feasibility audit is complete.
- Exactly one target was selected: determine `gp_d(K_r + T)` for `r >= 1` and
  finite trees of order at least three by characterizing/computing `beta(T)`.
- `P_n circ T` is not being pursued in parallel.
- No novelty claim, priority claim, or formal conjecture was made.

### Unique next step

Write and audit a formal proof of the two-branch mixed-join lemma, then design
and prove a rooted-tree dynamic program (or equivalent structural formula) for
`beta(T)`.  Implement the DP independently of the shortest-path checker and
compare it on a bounded nonisomorphic-tree matrix with full tests and preserved
mismatches.

## 2026-08-28 — Mixed-join theorem and beta-tree dynamic program

### Starting state and scope

- Read the complete `PROJECT_STATUS.md` and `AGENTS.md` before acting.
- Continued exactly the recorded unique task: formalize the mixed-join
  two-branch proof, solve `beta(T)` by a proved rooted-tree DP, implement it
  independently, and compare it with both subset search and the
  definition-first shortest-path checker.
- Did not start the dormant `P_n circ T` or arbitrary-first-factor directions.
- The bounded target-selection search still does not authorize a novelty or
  priority claim.

### Formal mixed-join proof

- Wrote `proofs/mixed_join_tree.md`.
- For a dual set meeting the complete factor, proved necessity and sufficiency
  of the two tree sides both being cliques.  Necessity uses a selected apex as
  the middle of a length-two tree-pair geodesic; sufficiency observes that both
  the selected set and its complement are cliques.  The branch exists exactly
  when `q_2(T)>0` and its maximum is `r+q_2(T)`.
- For a dual set avoiding the complete factor, proved that general position is
  equivalent to `Delta(T[X])<=1`, while complement convexity is equivalent to
  every selected vertex having at most one unselected tree neighbor.  The
  branch maximum is exactly `beta(T)`.
- Checked the two branches are exhaustive, treated `q_2(T)=0`, included `r=1`,
  and kept the order-at-least-three scope explicit.
- Specialized the already proved tree two-clique classification:
  `q_2(T)=2` only for `P_3` and `P_4`.  Since `beta(P_3)=2` and
  `beta(P_4)=3`, obtained the exact project theorem

  ```text
  gp_d(K_r + T) = r+2       for T in {P_3,P_4};
  gp_d(K_r + T) = beta(T)   for every other tree of order at least three.
  ```

- Recovered the preserved counterexample rather than discarding it:
  `beta(K_1,3)=3`, `q_2(K_1,3)=0`, and hence
  `gp_d(K_r+K_1,3)=3` for every `r>=1`.

### Structural characterization and DP proof

- Observed and proved that the two neighbor bounds for a selected vertex sum
  to its tree degree.  Consequently a beta-feasible set is characterized by:
  selected degree-two vertices have exactly one selected neighbor; vertices of
  degree at least three are never selected; selected leaves have no extra
  restriction.
- Rooted the tree arbitrarily and used the state `F_v(a,b)`, where `a` records
  whether `v` is selected and `b` records whether its parent is selected.
- The recurrence chooses child labels independently when `a=0`; when `a=1`,
  it admits exactly the child-label vectors giving at most one selected and at
  most one unselected neighbor at `v`.
- Proved correctness by induction on subtree height and proved that recorded
  maximizing child labels reconstruct a maximum set.
- Proved linear time and storage: a selected vertex of degree at least three is
  infeasible, so a feasible selected state examines at most four child-label
  patterns; unselected states optimize children independently.

### Independent implementation and tests

- Added `src/mixed_join_tree.py` without importing the direct shortest-path
  checker.  It validates the tree, computes `beta(T)`, returns one maximum set,
  tests local feasibility, and evaluates the scoped mixed-join formula.
- Used iterative rooting, postorder table construction, and iterative
  reconstruction.  The last choice avoids a Python recursion-depth failure on
  long paths while preserving the proved `O(n)` bounds.
- Added `tests/test_mixed_join_tree.py`, including named examples, invalid
  inputs, root independence, exhaustive beta comparison through order eight,
  direct mixed-join comparison through order six, and a 2,500-vertex path
  regression test for iterative reconstruction.
- The first test run had one failure: the manually entered expected value for
  the once-subdivided three-leaf star was 3.  The DP returned the feasible set
  of all six noncentral vertices.  Direct inspection shows each degree-two arm
  vertex has one selected leaf neighbor and one unselected center neighbor, so
  the correct value is 6.  The bad test expectation was corrected; the failure
  was not hidden or presented as a DP mismatch.
- Final test command:

  ```powershell
  .\.venv\Scripts\python.exe -m pytest -q tests
  ```

  Result after the final regression test: 29 passed.

### Bounded independent verification

- Added `experiments/audit_mixed_join_dp.py` and saved its report as
  `results/mixed_join_dp_audit.json`.
- Environment: CPython 3.13.5, NetworkX 3.6.1.
- Reproduction command:

  ```powershell
  .\.venv\Scripts\python.exe .\experiments\audit_mixed_join_dp.py --output .\results\mixed_join_dp_audit.json
  ```

- DP versus exhaustive subset search: all 985 nonisomorphic trees of orders
  3--12; mismatch count 0.
- Root invariance: 11,003 rerooted evaluations; mismatch count 0.
- Reconstructed maximum sets: 985 checks; failure count 0.
- Mixed-join formula versus the definition-first shortest-path checker: all 46
  nonisomorphic trees of orders 3--8 with `r=1,2,3,4`, for 184 comparisons;
  mismatch count 0.
- These finite computations independently audit the implementation.  They are
  not used as the proof and are not called proof.

### Stage conclusion

- The selected mixed-join problem is now internally proof-verified and has an
  exact linear-time computation/reconstruction method for its only new tree
  parameter.
- The formal theorem, implementation, unit tests, bounded matrices, initial
  failed expectation, and preserved star counterexample are all recorded.
- Whether an equivalent theorem already exists under different terminology,
  whether the result has novelty, and whether it warrants a research note
  remain `UNKNOWN` pending systematic literature positioning.

### Unique next step

Do only systematic literature positioning for the proved `K_r+T` theorem and
decide whether a research note is justified.  Recheck Jiang versions and
peer-review links, search broader mixed-join/cone/universal-vertex terminology,
record inclusion and exclusion decisions with coverage limits, and keep
novelty `UNKNOWN` unless the evidence supports a stronger statement.  Do not
start `P_n circ T` or arbitrary `F circ G` in parallel.

## 2026-08-28 — Systematic mixed-join positioning and research-note decision

### Starting state and scope

- Read the complete `PROJECT_STATUS.md`, `AGENTS.md`,
  `notes/extension_feasibility_audit.md`, `proofs/mixed_join_tree.md`,
  `notes/literature_notes.md`, and this research log before acting.
- Continued only the recorded task: literature-position the proved
  `gp_d(K_r+T)` theorem and decide whether a research note is justified.
- Did not start the dormant `P_n circ T` or arbitrary-first-factor directions.
- Used **NOT FOUND IN THIS AUDIT** and `UNKNOWN` rather than inferring global
  openness from negative searches.

### Jiang version and publication-link check

- Requeried Zenodo record `22116770`, old record `22081166`, the concept query,
  and DataCite DOI metadata.
- Current record remains v1.0.1, publication date 2026-08-27, DOI
  `10.5281/zenodo.22116770`, concept DOI `10.5281/zenodo.22081165`, resource
  subtype `preprint`, last updated 2026-08-27 03:02:35 +08:00.
- The old v1.0.0 DOI remains `10.5281/zenodo.22081166`.
- The current Zenodo record has no related journal identifier; DataCite lists
  only `IsVersionOf` the concept DOI.  No newer version or peer-reviewed link
  was found.  Future changes remain `UNKNOWN`.

### Structured database queries

- arXiv API exact phrase `"dual general position"`: 3 records (foundation,
  product, removal).  Adding `lexicographic` gave 1; adding `join`, `cone`,
  `universal vertex`, `tree`, or `dynamic programming` gave 0.
- DataCite title-phrase query: 3 DOI records, all the Jiang concept/version
  records for one work.  Adding `join` or `lexicographic` returned the same
  three; adding `cone`, `universal vertex`, `tree`, or `dynamic programming`
  returned 0.
- zbMATH Open exact phrase: 3 records with DOIs
  `10.1007/s40840-024-01788-z`, `10.1007/s40314-025-03547-7`, and
  `10.1016/j.dam.2026.02.044`.  Adding `lexicographic` gave only the product
  paper; the other narrower terms gave 0.
- Crossref free-text totals were extremely noisy and were not treated as
  meaningful negative counts.  Exact DOI metadata confirmed the removal paper
  as a 2026 journal article in *Discrete Applied Mathematics* 388, pp. 56--64.
- OpenAlex alternated between HTTP 429 and contradictory zero-result responses
  even for known titles; Semantic Scholar returned HTTP 429 for all five
  requests.  Neither source supplied negative evidence.
- OpenCitations v2 returned five DOI-linked citations to the foundation paper,
  one to the product paper, and zero to the removal and Jiang DOIs.  These
  incomplete counts were used only as discovery aids.
- The arXiv API still reports survey `2501.19385v5`, updated 2026-08-16.  It
  predates Jiang and provides no mixed-join tree theorem.

### Direct prior subcase found

- The removal paper treats the fan `F_n=K_1+P_n`, which is a direct subfamily
  of the project theorem.
- ArXiv v2 (`2510.01294v2`, 2026-02-03) states for `n>=4`
  `gp_d(F_n)=floor(2(n+1)/3)` and explains that maximum fan gp-sets are dual.
  This equals the known standard fan value `ceil(2n/3)` from Tian--Xu--Chao
  (2023), DOI `10.1007/s40840-023-01592-1`.
- Preserved a source-version discrepancy: the older author-hosted v1 PDF
  displays `ceil(2(n+1)/3)`, while arXiv v2 displays the consistent floor.
  The two differ when `n` is divisible by 3.  The paywalled version-of-record
  body was not directly compared, so its exact display remains `UNKNOWN`.
- Consequence for positioning: the fan case cannot be claimed as new.  The
  real increment is all trees, arbitrary `r`, the two-branch classification,
  and linear maximum-set reconstruction.

### Broader terminology and neighboring parameters

- Web queries covered mixed/complete join, cone, apex, universal vertex, fan,
  wheel, split/complete-split graph, tree, `K_r`, convex complement, and tree
  dynamic programming.
- Tian--Klavzar Proposition 3.5 for `P_m+2K_1` was included but excluded as
  direct coverage because `2K_1` is noncomplete.  The standard-general-position
  join formula and the mobile-general-position join paper were excluded because
  they concern different invariants.
- Dissociation-set literature is the closest named optimization family:
  `Delta(T[X])<=1`.  It does not impose the beta outside-neighbor bound.  The
  center plus one leaf of `K_1,3` is a dissociation set but is not beta-feasible,
  proving that the feasible-set systems differ.
- No established name or exact recurrence for `beta(T)` was found.  The label
  remains **NOT FOUND IN THIS AUDIT**, not a novelty theorem.

### Positioning result

- No source determining the full family `gp_d(K_r+T)` was found in the recorded
  coverage.
- Relative to checked work, the project contributes the mixed complete-factor
  branch split, all-tree formula, `r`-dependence classification, beta local
  structure, and linear value/reconstruction DP.
- Global openness/novelty remains `UNKNOWN` because MathSciNet, Scopus, and Web
  of Science were not checked directly and two open indexes were unavailable.
- Full audit and source table:
  `notes/mixed_join_literature_positioning.md`.

### Research-note verdict

- Verdict: **CONDITIONAL GO FOR AN INTERNAL DRAFT**.
- Positive evidence: explicit Jiang gap, nontrivial star counterexample,
  complete dual-set classification, linear reconstruction, and two independent
  bounded computational audits.
- Conditions: cite the published fan subcase, explain beta versus dissociation,
  add explicit worked families, keep the manuscript self-contained, recheck
  Jiang immediately before submission, and seek direct MathSciNet/Scopus/Web of
  Science and VOR access if available.
- This verdict authorizes drafting, not a novelty or priority claim.

### Unique next step

Begin a self-contained research-note draft.  First write the
introduction/literature-position section, preliminaries, and the two-branch
theorem; include the fan formula as prior work and do not expand the mathematical
scope.

## 2026-08-29 — Research-note introduction drafted (small-budget step)

### Scope

- Read the complete `PROJECT_STATUS.md` and `AGENTS.md` before acting, then
  checked `notes/mixed_join_literature_positioning.md` and the theorem statement
  in `proofs/mixed_join_tree.md`.
- Because the user requested a simple step under a tight usage budget, split the
  recorded three-section drafting task at a clean boundary: this stage writes
  only the Introduction / literature-positioning section and the manuscript
  skeleton.
- No mathematical result, implementation, test, experiment, or literature
  search was changed or started.

### Draft added

- Added `drafts/mixed_join_research_note.md` as an English internal working
  draft.
- The Introduction states the Tian--Klavžar dual-set criterion and the
  lexicographic-product context, distinguishes Jiang's complete-first-factor
  result from the mixed join `K_r+T`, and records that Jiang Theorem 5.1 excludes
  mixed complete/noncomplete joins.
- It explicitly cites the previously known fan family `K_1+P_n`, gives the
  arXiv-v2 floor formula, and preserves the author-v1 versus arXiv-v2 discrepancy
  and the version-of-record display as `UNKNOWN`.
- It states the proved mixed-join formula and defines `beta(T)` only to orient
  the reader. It labels the bounded negative literature result correctly and
  makes no novelty or priority claim.
- Added only four references whose metadata had already been verified in the
  canonical notes. No new citation was inferred or fabricated.

### Status and unique next step

- Introduction / literature positioning is now drafted; later sections remain
  explicit placeholders.
- Unique next step: write only the self-contained Preliminaries, defining
  graph/geodesic/interval/convexity, general and dual general position, complete
  join, `q_2(T)`, `beta(T)`, and the fixed notation `C=V(K_r)`, `H=K_r+T`.

## 2026-08-29 — Research-note preliminaries drafted (small-budget step)

### Scope and sources

- Re-read the complete `PROJECT_STATUS.md` and `AGENTS.md`, then used the
  verified definitions in `notes/definitions.md` and the existing research-note
  draft.
- Continued only the recorded next task. No theorem proof, implementation,
  experiment, test, or literature search was started.

### Text added

- Replaced the Section 2 placeholder in
  `drafts/mixed_join_research_note.md` with self-contained preliminaries.
- Defined finite simple graph notation, induced subgraphs, neighborhoods,
  distance, geodesics, intervals, convex sets, positionable pairs, general
  position, dual general position, and `gp_d`.
- Included both the original positionable-pair formulation and the verified
  Tian--Klavžar criterion: general position plus convex complement.
- Defined the complete join and fixed `C=V(K_r)` and `H=K_r+T`; recorded why
  `H` has diameter two in the manuscript scope.
- Defined `q_2(T)` and `beta(T)` and added a plain interpretation of the two
  local beta constraints. No mathematical conclusion was changed.

### Verification and status

- The definitions were checked against `notes/definitions.md`; no unverified
  citation or new claim was added.
- This was a documentation-only change, so the existing code tests were not
  rerun.
- All recorded `UNKNOWN` items remain unchanged.
- Unique next step: draft only the apex-meeting branch and its
  `r+q_2(T)` corollary as self-contained manuscript text.

## 2026-08-29 — Research-note apex-meeting branch drafted

### Scope and source

- Re-read the complete `PROJECT_STATUS.md` and `AGENTS.md`, then used the
  already audited proof in `proofs/mixed_join_tree.md` as the canonical
  mathematical source.
- Continued only the recorded next task. Did not draft the apex-avoiding
  branch, combine the final formula, start an experiment, or perform a new
  literature search.

### Manuscript text added

- Replaced the Section 3 placeholder in
  `drafts/mixed_join_research_note.md` with an introductory branch split and
  the complete apex-meeting subsection.
- Stated and proved that, for `X cap C` nonempty and
  `S=X cap V(T)`, the set `X` is dual general position in `H=K_r+T` if and
  only if both `T[S]` and `T[V(T) setminus S]` are complete.
- Necessity for the selected tree side uses a selected universal-clique
  vertex as the middle of a length-two geodesic, contradicting general
  position. Necessity for the unselected tree side uses the same kind of
  geodesic to contradict convexity of the complement.
- Sufficiency is self-contained: both `X` and `H-X` are cliques, so `X` is in
  general position and its complement is convex.
- Explicitly covered empty/full complete-factor parts and explained why an
  empty tree part cannot occur in this noncomplete-tree scope.
- Derived the corollary that the branch exists exactly when `q_2(T)>0` and
  has maximum size `r+q_2(T)`, including both the upper bound and an attaining
  construction using all of `C`.

### Verification and status

- Compared the drafted statement and every proof implication against
  `proofs/mixed_join_tree.md`; no mathematical claim was changed.
- This was a manuscript-only change. No implementation changed and no test
  suite was run.
- No new literature fact, computation, conjecture, novelty claim, or priority
  claim was introduced. All `UNKNOWN` items remain unchanged.
- Unique next step: draft only the apex-avoiding branch and its `beta(T)`
  corollary as self-contained manuscript text; do not yet combine the final
  formula.

## 2026-08-29 — Research-note apex-avoiding branch drafted

### Scope and source

- Re-read the complete `PROJECT_STATUS.md` and `AGENTS.md`, then checked the
  current manuscript and the already audited apex-avoiding proof in
  `proofs/mixed_join_tree.md`.
- Continued only the recorded next task. Did not combine the two branch
  maxima, specialize `q_2(T)`, draft the beta structural characterization or
  dynamic program, start an experiment, or perform a literature search.

### Manuscript text added

- Replaced the Section 3.2 placeholder in
  `drafts/mixed_join_research_note.md` with Lemma 3.3 and Corollary 3.4.
- Proved that, for `X subseteq V(T)`, general position in `H=K_r+T` is
  equivalent to `Delta(T[X])<=1`. One direction uses two selected tree
  neighbors of a selected vertex; the other uses the fact that every geodesic
  containing three distinct selected vertices must have length two because
  `H` has diameter two.
- Proved separately that `H-X` is convex if and only if every selected
  `x` has at most one neighbor in `V(T) setminus X`. The proof treats pairs
  involving `C`, adjacent tree pairs, and nonadjacent unselected tree pairs,
  and uses triangle-freeness of `T` in both directions.
- Combined the two equivalences using the Tian--Klavzar criterion already
  stated in the preliminaries.
- Derived directly from the definition that the maximum size in this branch
  is `beta(T)`.

### Verification and status

- Compared the statement and both directions of each equivalence with
  `proofs/mixed_join_tree.md`; no mathematical result was changed.
- This was a manuscript-only change. No implementation changed and no tests
  were run.
- No new literature fact, computation, conjecture, novelty claim, or priority
  claim was introduced. All `UNKNOWN` items remain unchanged.
- Unique next step: combine the two branch maxima, prove the tree
  specialization of `q_2(T)`, verify `beta(P_3)=2` and `beta(P_4)=3`, and
  derive the simplified exact formula. Do not yet draft the local beta
  characterization or dynamic program.

## 2026-08-29 — Research-note exact formula combined

### Scope and source

- Re-read the complete `PROJECT_STATUS.md` before acting, then checked the
  current manuscript and the already audited formula in
  `proofs/mixed_join_tree.md`.
- Continued only the recorded next task. Did not draft the local beta
  characterization or rooted-tree dynamic program, modify an implementation,
  start an experiment, or perform a literature search.

### Manuscript text added

- Added Section 3.3 to `drafts/mixed_join_research_note.md`.
- Combined the exhaustive, disjoint apex-meeting and apex-avoiding branches to
  prove
  `gp_d(K_r+T)=beta(T)` when `q_2(T)=0` and
  `gp_d(K_r+T)=max{beta(T),r+q_2(T)}` when `q_2(T)>0`.
- Proved the tree specialization rather than merely citing it: triangle-free
  trees have clique number at most two, so a two-clique partition forces order
  at most four; `P_3` has a `2+1` partition, and among the two order-four trees
  only `P_4` has the required perfect matching. Thus `q_2(T)=2` precisely for
  `T` in `{P_3,P_4}` and is zero otherwise in the manuscript scope.
- Verified both beta boundary values with explicit lower and upper bounds:
  `{v_1,v_3}` witnesses `beta(P_3)>=2`, `{v_1,v_2,v_4}` witnesses
  `beta(P_4)>=3`, and the full vertex set is infeasible in each path because
  its induced maximum degree is two. Hence `beta(P_3)=2` and
  `beta(P_4)=3`.
- Derived the simplified formula
  `gp_d(K_r+T)=r+2` for `T` in `{P_3,P_4}` and `beta(T)` otherwise, using
  `r+2>=3` for every `r>=1`.

### Verification and status

- Compared the combined formula, the tree classification, both beta values,
  and the simplified corollary line by line with
  `proofs/mixed_join_tree.md`; no mathematical result was changed.
- This was a manuscript-only change. No implementation changed and no tests
  were run; the previously recorded computational audits remain supporting
  evidence rather than proof.
- No new literature fact, computation, conjecture, novelty claim, or priority
  claim was introduced. All recorded `UNKNOWN` items remain unchanged.
- Unique next step: write only the set-level local characterization of
  `beta(T)` in Section 4, including the degree-zero and degree-one boundary
  cases. Do not yet draft the rooted-tree dynamic program.

## 2026-08-29 — Research-note beta characterization drafted

### Scope and source

- Continued from the newly recorded unique next step, using the definition in
  the manuscript and the independently proved characterization in
  `proofs/mixed_join_tree.md`.
- Did not draft the rooted-tree dynamic program, add examples, change code,
  start an experiment, or perform a literature search.

### Manuscript text added

- Replaced the Section 4 placeholder in
  `drafts/mixed_join_research_note.md` with a set-level proposition and proof.
- For each selected vertex `x`, introduced its selected-neighbor count
  `s_X(x)` and unselected-neighbor count `u_X(x)`, with
  `s_X(x)+u_X(x)=deg_T(x)`.
- Proved necessity: the original beta constraints give
  `s_X(x)<=1` and `u_X(x)<=1`; hence no selected vertex has degree at least
  three, and a selected degree-two vertex must have exactly one selected and
  one unselected neighbor.
- Proved sufficiency by checking all possible selected-vertex degrees. A
  selected degree-two vertex has neighbor counts `(1,1)`, while both counts
  are automatically at most one for selected vertices of degree zero or one.
  The high-degree case is excluded.
- Explicitly noted that the equivalence classifies every beta-feasible set,
  not only maximum sets, and retained the degree-zero boundary even though it
  is absent for trees in the manuscript's order-at-least-three scope.
- Added the direct corollary that the set of all leaves is beta-feasible and
  therefore `beta(T)>=|L(T)|`.

### Verification and status

- Compared both implications with the characterization in
  `proofs/mixed_join_tree.md`. The new leaf corollary follows directly because
  every leaf has degree one.
- This was a manuscript-only change. No mathematical implementation changed
  and no tests were run.
- No new literature fact, computation, conjecture, novelty claim, or priority
  claim was introduced. All `UNKNOWN` items remain unchanged.
- Unique next step: write the complete rooted-tree DP, correctness proof,
  maximum-set reconstruction, and linear complexity analysis in Section 5.
  Do not yet add examples or a reproducibility appendix.

## 2026-08-29 — Research-note linear DP drafted

### Scope and source

- Continued only the recorded Section 5 task, using the audited recurrence and
  proof in `proofs/mixed_join_tree.md`.
- Did not add worked examples or a reproducibility appendix, change code,
  start a new experiment, or perform a literature search.

### Manuscript text added

- Replaced the Section 5 placeholder in
  `drafts/mixed_join_research_note.md` with a complete rooted-tree dynamic
  program.
- Rooted the tree at an arbitrary vertex, defined descendant subtrees and
  child sets, and introduced `F_v(a,b)` with the current-vertex and parent
  labels as the complete boundary state. Root states use the no-parent symbol
  `bot`, and impossible states have value minus infinity.
- Defined `s` as the number of selected children, `p` as the parent label (or
  zero at the root), and `d=deg_T(v)`. For a selected state the recurrence
  admits exactly the child-label vectors satisfying
  `p+s<=1` and `d-(p+s)<=1`; an unselected state has no constraint at `v`.
- Gave the bottom-up recurrence, the maximum of the two root states, and a
  height-induction proof. The proof fixes the boundary labels, uses the lack of
  edges between different child subtrees, invokes exact child optima, and then
  checks precisely the constraint at the current vertex.
- Specified top-down reconstruction: choose a maximizing root label, add each
  vertex with label one, and follow the stored maximizing child-label vector.
  Compatibility and optimality follow from the same induction.
- Proved linear time and space. Unselected states choose independently for
  each child; selected states of degree at least three are immediately
  infeasible, and every remaining selected state examines at most four label
  vectors. There are constantly many states per vertex, while the total child
  count is `|V(T)|-1`.

### Verification and status

- Compared the state meaning, both neighbor inequalities, recurrence, root
  answer, induction, reconstruction, and complexity argument with
  `proofs/mixed_join_tree.md`; no mathematical or algorithmic claim was
  changed.
- This was a manuscript-only change. No implementation changed and no tests
  were run; existing exhaustive and reroot audits remain separate supporting
  evidence.
- No new literature fact, computation, conjecture, novelty claim, or priority
  claim was introduced. All `UNKNOWN` items remain unchanged.
- Unique next step: add worked examples covering stars and the path/fan family,
  with all values derived only from proved formulas or already verified
  literature. Do not yet write the reproducibility appendix.

## 2026-08-29 — Research-note worked examples drafted

### Scope and sources

- Continued the recorded examples task using Proposition 4.1, Corollary 3.8,
  the preserved star counterexample, and the already verified fan statement in
  `notes/mixed_join_literature_positioning.md`.
- Added proofs and deductions only. No implementation or result file changed,
  no experiment was run, and no new literature claim was introduced.

### Stars and subdivided stars

- Proved for `k>=3` that the center of `K_{1,k}` is forced unselected while
  all leaves form a feasible set. Hence `beta(K_{1,k})=k` and
  `gp_d(K_r+K_{1,k})=k` for every `r>=1`.
- Recovered the preserved counterexample
  `gp_d(K_r+K_{1,3})=3`, and explicitly retained the failure of the naive
  `r+q_2(T)` expression at `r=4`.
- Defined the once-subdivided star `S_k` for `k>=3`. Its center is forced
  unselected, while selecting every degree-two arm vertex and every leaf is
  feasible and has size `2k`. Since all other vertices are selected, this is
  maximum. Thus `beta(S_k)=gp_d(K_r+S_k)=2k` for every `r>=1`.

### Paths and the fan consistency check

- Proved independently that `beta(P_n)=ceil(2n/3)` for every `n>=3`.
  A feasible set contains at most two vertices in each consecutive block of
  three, and the words `(110)^q`, `(110)^q1`, and `(110)^q11` attain the three
  residue-class bounds. Proposition 4.1 verifies every construction.
- Combined this with Corollary 3.8 to obtain
  `gp_d(K_r+P_n)=r+2` for `n=3,4` and `ceil(2n/3)` for `n>=5`.
- For `r=1,n>=4`, showed explicitly that this becomes
  `ceil(2n/3)=floor(2(n+1)/3)`, exactly the verified arXiv-v2 fan value. The
  manuscript labels this as a consistency check and not a novelty claim.

### Verification and status

- Checked the star argument against the preserved proof/counterexample notes,
  checked every selected degree-two vertex in the subdivided-star construction,
  and checked all three path residue classes against the local characterization.
- The fan agreement provides a literature-level independent check for the
  `r=1,n>=4` subfamily; the source-version discrepancy and VOR `UNKNOWN` remain
  stated in the Introduction.
- No computational result was called a proof. Global novelty, priority, and
  the other recorded `UNKNOWN` items remain unchanged.
- Unique next step: write the reproducibility section from the existing code,
  tests, and JSON reports; rerunning existing audits is allowed only to verify
  the current workspace, with no expansion of experimental scope.

## 2026-08-29 — Research-note reproducibility section drafted

### Source and implementation inspection

- Read the complete mixed-join audit driver, DP implementation, definition-first
  shortest-path checker, brute-force beta routine, focused tests, and both
  relevant JSON reports before writing any count.
- Confirmed that `src/mixed_join_tree.py` uses the rooted-tree recurrence and
  does not import the shortest-path checker. The beta reference side enumerates
  all vertex subsets and checks the two local constraints directly.
- Confirmed that `src/dual_gp_independent.py` explicitly constructs graphs,
  computes all-pairs distances by BFS, enumerates subsets, and checks general
  position plus complement convexity without using the mixed-join formula,
  beta characterization, or DP.

### Fresh reproduction

- Ran `.\.venv\Scripts\python.exe -m pytest -q tests` on 2026-08-29:
  `29 passed in 0.79s`.
- Ran `.\.venv\Scripts\python.exe .\experiments\audit_mixed_join_dp.py`
  without changing the archived report. The live output reproduced the JSON:
  985 DP-versus-subset comparisons, 11,003 reroot comparisons, 985 successful
  reconstructions, and 184 formula-versus-definition comparisons, with zero
  mismatch or reconstruction failure.
- Verified the active environment as Windows 11 build 26100, CPython 3.13.5,
  NetworkX 3.6.1, and pytest 9.1.1.

### Manuscript text added

- Added Section 7 explaining the two independent verification routes and
  explicitly stating that they are finite computational evidence, not proof.
- Recorded the exact sample scopes: all 985 nonisomorphic trees of orders
  3--12 for DP/subset/reconstruction checks; all 46 nonisomorphic trees of
  orders 3--8 with `r=1,2,3,4` for 184 shortest-path-definition comparisons.
- Kept the earlier 92 mixed-join target-selection comparisons separate because
  they overlap the larger matrix and must not be double-counted.
- Added reproduction commands, the unpinned-requirements limitation, the
  `29 passed` result, and the order-2,500 nonrecursive reconstruction test.
- Recorded SHA-256 hashes for the DP implementation, definition-first checker,
  audit driver, and archived JSON; independently recomputed all four hashes
  after drafting and obtained exact matches.

### Status

- No mathematical implementation or archived result changed. The existing
  experiment was rerun without increasing its orders, `r` values, or test
  families.
- No computation was promoted to proof, and no literature, novelty, or
  priority claim changed. All `UNKNOWN` items remain unchanged.
- Unique next step: perform a complete manuscript consistency audit against
  the proof and literature notes, fixing only manuscript issues. Do not yet
  write the conclusion or run a new search/experiment.

## 2026-08-29 — First complete manuscript consistency audit

### Audit coverage

- Re-read the full manuscript and compared it with `notes/definitions.md`,
  `proofs/mixed_join_tree.md`, `notes/mixed_join_literature_positioning.md`,
  the reference metadata in the canonical notes, and the machine-readable
  mixed-join audit report.
- Checked the all-geodesics quantifiers in the definitions, both directions of
  each structural lemma, exhaustion of the two branches, the `q_2=0` boundary,
  `r=1`, the `P_3/P_4` classification, both beta boundary values, every DP
  boundary label and neighbor count, reconstruction compatibility, all three
  worked families, and the non-double-counted audit totals.
- Scanned headings, theorem declarations, formula labels, cross-references,
  Markdown code fences, display-math delimiters, and LaTeX cases environments.

### Findings and manuscript fixes

- Found no mathematical error or counterexample in the manuscript.
- Replaced the stale future-tense Introduction preview with exact references to
  the now-present Sections 3--7.
- Added the required beta-versus-dissociation comparison. Every beta-feasible
  set is a dissociation set, but the center plus one leaf of `K_{1,3}` is a
  dissociation set and fails beta because the center has two unselected
  neighbors. The text makes no claim that beta is a new named parameter.
- Renamed the final heading from “References currently cited” to “References,”
  added the canonical Article 5 information to reference [1], and added the
  verified 27 August 2026 date to the Jiang preprint entry.
- Structural scan result: 76 display-math delimiters, 2 code fences, 7 opening
  and 7 closing cases environments, and 6 distinct equation labels. The 13
  numbered lemmas/corollaries/theorems/propositions are unique and every
  manuscript cross-reference resolves.

### Preserved limits and follow-up observation

- Fan VOR wording, subscription-index coverage, Jiang future status, global
  novelty/priority, and the other recorded `UNKNOWN` items remain unchanged.
- No new literature search or computation was run during this stage.
- A cross-file observation was parked because this stage was manuscript-only:
  the docstring of the historical brute-force `beta_tree` helper still says it
  is used only through order seven, while the later main audit correctly uses
  it through order twelve. The executable behavior and manuscript counts are
  correct; the stale source comment should be corrected during the final
  cross-file documentation pass.
- Unique next step: write only the Conclusion and limitations section, keeping
  every scope and literature limitation explicit.

## 2026-08-29 — Conclusion and limitations drafted

### Manuscript text added

- Added Section 8 to `drafts/mixed_join_research_note.md`.
- Summarized the exhaustive apex-meeting/apex-avoiding split, their maxima
  `r+q_2(T)` and `beta(T)`, the `P_3/P_4` specialization, and the final exact
  formula without introducing a new claim.
- Summarized the beta local characterization and the linear-time,
  linear-space value/reconstruction algorithm, and pointed back to the star,
  subdivided-star, and path examples.
- Described the fan overlap precisely as the prior value displayed in the
  checked arXiv v2 of [4], avoiding any implication that the path subfamily is
  new or that the unchecked VOR display is known.

### Limitations retained

- Jiang [3] remains a preprint; future revision, correction, or peer review is
  `UNKNOWN`.
- The bounded computations remain implementation evidence and are not proof.
- MathSciNet, Scopus, and Web of Science were not directly checked, and some
  open indexes were unavailable; global novelty and priority remain `UNKNOWN`.
- The exact fan formula display in the version-of-record body remains
  `UNKNOWN`, although arXiv v2 was checked.
- The manuscript scope remains only `K_r+T`, `r>=1`, `|V(T)|>=3`; arbitrary
  first factors, general mixed complete joins, and `P_n circ T` are explicitly
  outside scope.

### Status

- No literature search, computation, implementation, conjecture, or theorem
  change occurred in this stage.
- Unique next step: perform final readability, formatting, and cross-file
  documentation checks; add a concise abstract, correct the known stale
  brute-force-helper docstring, and rerun the existing tests after documentation
  changes.

## 2026-08-29 — Internal research-note drafting pass completed

### Final manuscript work

- Added a concise Abstract stating the exact mixed-join formula, the two-branch
  interpretation, the beta characterization, linear reconstruction, examples,
  and the evidence-not-proof status of the computations.
- Rechecked heading hierarchy, tables, code blocks, display mathematics,
  equation tags, references, and trailing whitespace. Final structural counts
  are 80 display-math delimiters, 2 code fences, 9 matched cases environments,
  and 6 unique equation labels; no unmatched item or trailing whitespace was
  found.
- The manuscript now contains Abstract, Sections 1--8, and References. No
  theorem, formula, scope, citation claim, or `UNKNOWN` conclusion changed in
  the final readability pass.

### Cross-file documentation fixes

- Updated `README.md` from the original lexicographic-only description to the
  actual complete-first-factor history and current mixed-join focus; corrected
  the nonexistent `manuscript/` path to the real `drafts/` path and updated the
  test command.
- Corrected the stale `beta_tree` helper docstring: the historical target
  selection audit uses it through order seven, while the later dedicated audit
  uses it through order twelve. This was a comment-only source change.
- Added the imported helper's SHA-256
  `A463CE202995000F324BDB7F90D2821B1B97AB38911E3E8941DFFC381F8393F6`
  to the manuscript artifact table, so the exact audit dependency is no longer
  omitted.
- Updated the canonical draft description in `PROJECT_STATUS.md`, marked the
  completed next step in `notes/mixed_join_literature_positioning.md` as
  historical, checked off the four completed manuscript requirements there,
  and marked the old next step in `notes/theorem_applicability.md` as completed
  and superseded.

### Verification and next stage

- After the source-docstring correction, ran
  `.\.venv\Scripts\python.exe -m pytest -q tests`: `29 passed in 0.38s`.
- No experiment range was expanded and no literature search occurred during
  this documentation stage.
- The first full internal drafting pass is complete. Global novelty/priority,
  subscription-index coverage, fan VOR body wording, and Jiang future status
  remain `UNKNOWN`.
- Unique next step: perform a bounded post-draft version and literature refresh
  centered on Jiang metadata/versions, exact-title and direct-citation changes,
  and another evidence-based attempt to inspect the fan VOR body. Do not start
  a new mathematical direction.

## 2026-08-29 — Post-draft version and literature refresh

### Jiang record refresh

- Queried the live Zenodo record, concept-family search, and versions endpoint.
  The versions endpoint returns exactly v1.0.0 (`22081166`, 2026-08-24) and
  v1.0.1 (`22116770`, 2026-08-27); v1.0.1 remains latest with update timestamp
  `2026-08-27T03:02:35.559335+08:00`.
- The current record remains a `publication/preprint`, has no related journal
  identifier, and retains the previously checked PDF and supplement MD5 values.
- DataCite still classifies the current DOI as a Preprint, version v1.0.1, and
  lists only `IsVersionOf` the concept DOI. Its exact-title query returns the
  concept DOI and two version DOIs for one intellectual work.
- No newer version, correction, or peer-reviewed identifier was found. This is
  a bounded metadata result; future changes remain `UNKNOWN`.

### Index and citation refresh

- arXiv exact phrase `"dual general position"`: the same 3 records
  (foundation, product, removal); no Jiang or mixed-join hit.
- zbMATH Open exact phrase: the same 3 records; an exact Jiang-title request
  returned its no-results response.
- Crossref's Jiang-title free-text query remained noisy and returned no exact
  Jiang record in the top 20. It was not used as a global negative count.
- OpenCitations v2 returned 5 citations to the foundation paper, 1 to the
  product paper (arXiv `2601.19769`), and 0 to the removal and Jiang DOIs.
  Crossref cited-by metadata gave 6, 1, and 0 for foundation, product, and
  removal. The disagreement is preserved as a coverage difference.
- OpenAlex returned zero for the exact Jiang title but also zero for a DOI query
  of the known product paper. It remains a coverage failure and supplies no
  negative evidence.
- No returned record covered the full all-tree, arbitrary-`r` mixed join. The
  correct label remains **NOT FOUND IN THIS BOUNDED REFRESH**.

### Fan VOR body attempt

- Crossref exposes Elsevier VOR text-mining links for the journal DOI. An
  unauthenticated text request returned HTTP 400 with an unauthorized/minimized
  metadata warning; a direct ScienceDirect page request returned HTTP 403.
- Used the in-app Browser only after the API and direct webpage routes failed.
  The visible ScienceDirect page stopped at a Cloudflare “Are you a robot?”
  CAPTCHA. In accordance with browser safety rules, the CAPTCHA was neither
  solved nor bypassed. The temporary browser tab was closed.
- The current author publication-list PDF link resolves to the 17-page arXiv v2
  PDF. It is not evidence for the distinct VOR body display.
- The fan VOR formula therefore remains `UNKNOWN`; arXiv v2 remains the checked
  source of the floor expression.

### Status and unique next step

- Added the complete refresh results and coverage failures to
  `notes/mixed_join_literature_positioning.md`.
- No mathematical statement, computation, conjecture, or novelty/priority
  status changed. Subscription databases were still not directly checked.
- With all currently accessible open-source checks stable, the next bounded
  step is to prepare a LaTeX/submission-style version of the existing internal
  note without changing scope or claims, then compile it if a TeX engine is
  available.

## 2026-08-29 — LaTeX/submission-style internal draft completed

### Conversion and normalization

- Checked the local toolchain before claiming compilation support. None of
  `pdflatex`, `xelatex`, `lualatex`, `latexmk`, `tectonic`, `latex`, or
  `texify` is installed. Pandoc 2.12 is available at
  `E:\\Anaconda\\Scripts\\pandoc.exe`.
- Used Pandoc for the initial mechanical Markdown-to-LaTeX conversion, then
  normalized `drafts/mixed_join_research_note.tex` by hand with patch-based
  edits. The source now uses the portable `article` class with `amsmath`,
  `amssymb`, and `amsthm`.
- Removed the duplicated title heading, converted the abstract and Sections
  1--8 to native LaTeX structure, and placed all 13 numbered statements and 13
  proofs in shared-counter `theorem`/`lemma`/`corollary`/`proposition` and
  `proof` environments. The intended sequence is 3.1--3.8, 4.1--4.2,
  5.1--5.2, and 6.1.
- Converted the six hand-tagged equations to section-numbered `equation`
  environments with labels and replaced internal hard-coded references with
  `ref`/`eqref`. Converted the four bibliography entries and ten in-text
  citation occurrences to `thebibliography`/`bibitem`/`cite`, retaining the
  arXiv-v2 qualifiers and adding clickable DOI/arXiv targets.
- Replaced the Pandoc syntax-highlighting block with a plain `verbatim`
  PowerShell block, preserving a valid PowerShell backtick continuation.
  Changed the two wide tables to wrapping `p{}` columns, changed file paths to
  breakable `path` forms, and inserted zero-width `allowbreak` points in each
  64-character SHA-256 value. Removing those layout commands reconstructs all
  five original hashes exactly.
- Replaced the only non-ASCII name spelling by the portable TeX form
  `Klav\\v{z}ar`; no mathematical or bibliographic identity changed.

### Static verification

- Pandoc successfully parsed the normalized LaTeX source back to its native
  representation (`pandoc ... --from=latex --to=native`). This is a syntax
  check, not a TeX compilation.
- Static cross-reference scan: 35 labels, all unique; 46 `ref`/`eqref`
  occurrences with zero undefined targets; 10 citations with zero undefined
  bibliography keys; four bibliography items.
- Structural scan: 50 begin/end pairs pass a nested stack check; unescaped
  left/right brace counts are 395/395; 34 `\\[...\\]` pairs plus six
  equation pairs preserve 40 display formulas; all five Markdown SHA-256
  values are recoverable from the TeX source; `UNKNOWN` occurs five times in
  both source forms.
- Removed the five Pandoc artifacts `-\\/-` and found no residual manual
  `tag`, `hypertarget`, hand-written citation marker, proof heading, square
  terminator, or non-ASCII character.
- Reran `./.venv/Scripts/python.exe -m pytest -q ./tests`: `29 passed in
  0.99s`. No mathematical implementation or experiment range changed.

### Limitation and next step

- Because no TeX engine is installed, no PDF was generated and no actual
  LaTeX compilation log, overfull-box report, font check, or rendered-page
  inspection exists. The source passed static checks only; this must not be
  restated as successful compilation.
- No literature search, theorem change, experiment, conjecture, or
  novelty/priority claim occurred in this stage. All recorded `UNKNOWN` items
  remain unchanged.
- Unique next step: perform the separately bounded, section-by-section
  Markdown-versus-LaTeX content parity audit and record any remaining
  conversion-only discrepancy or unverified layout risk.

## 2026-08-29 — Markdown--LaTeX source parity audit completed

### Independent and local comparison

- Performed a separate read-only, section-by-section comparison of
  `drafts/mixed_join_research_note.md` and
  `drafts/mixed_join_research_note.tex`, alongside local extraction checks.
- The complete structural manifest agrees: Abstract, Sections 1--8, the eight
  subsections, and References are present in the same order. Native LaTeX
  numbering replaces only the Markdown's hand-written heading prefixes.
- The 13 statement types and their order agree exactly. The shared counter
  generates Lemma/Corollary/Theorem/Proposition numbers 3.1--3.8, 4.1--4.2,
  5.1--5.2, and 6.1, and both forms contain exactly 13 proofs.
- Extracted all 40 Markdown display formulas and all 40 LaTeX display/equation
  formulas in source order. After removing only Markdown `tag` commands and
  LaTeX `label` commands and normalizing whitespace, every item is identical.
- Removed display formulas and the Markdown-only 13 QED-square markers, then
  compared inline mathematics in source order. The 447 Markdown and 447 LaTeX
  items are identical. Equation numbering generated by section is 5.1--5.3
  and 6.1--6.3.
- The DP states, recurrence, admissibility inequalities, induction proof,
  reconstruction, and complexity statement are unchanged. The star,
  subdivided-star, path, and retained `K_{1,3}` counterexample calculations
  are unchanged.

### References and reproducibility parity

- All four bibliography records and ten citation sites resolve. A final minor
  typography defect was fixed: reference [4] no longer prints both a literal
  `DOI:` prefix and a linked `doi:` prefix. All four DOI sets agree with the
  Markdown source, and the arXiv-v2 qualification remains explicit.
- The two audit tables preserve 985 DP/subset comparisons, 11,003 root checks,
  985 reconstruction checks, 184 definition-first mixed-join comparisons, and
  zero failures in every row. The historical 92 comparisons remain explicitly
  excluded from the totals to avoid double counting.
- Rejoining the single legal PowerShell backtick continuation makes the three
  LaTeX commands byte-for-byte equivalent to the three Markdown commands after
  whitespace normalization.
- Removing the five sets of layout-only `allowbreak` commands reconstructs all
  five 64-character SHA-256 values exactly. The final TeX source has 1,069
  lines and SHA-256
  `B0EE092172447B08480C9CBA14D80BBC7CAD4E475067B8FE762797EE9F7642C9`.
- All five occurrences of `UNKNOWN`, the evidence-not-proof warning, Jiang's
  preprint status, the fan-prior-work boundary, subscription-database coverage
  limits, and the no-novelty/no-priority language remain present.

### Result and next step

- No substantive content loss, mathematical change, or semantic drift was
  found. The only edit arising from this audit was the duplicate DOI-prefix
  typography fix.
- Pandoc's LaTeX reader still returns exit code 0 after the fix. Actual TeX
  compilation and rendered-page inspection remain unavailable because the
  machine has no TeX engine; this is the only outstanding artifact-verification
  limitation.
- No new search, experiment, conjecture, proof, or novelty assessment occurred.
- Unique next step: prepare a concise, evidence-bounded collaborator reading
  guide that points to the theorem dependency chain, prior-work boundary,
  computational checks, review hotspots, preserved `UNKNOWN` items, and the
  no-engine limitation.

## 2026-08-29 — Collaborator reading guide completed and audited

### Guide produced

- Added `notes/collaborator_reading_guide.md`, an approximately two-page
  (1,119-word) entry point for a mathematical collaborator.
- The guide states the simplified formula and the two-branch structural form,
  gives the beta definition and degree characterization, and presents a compact
  dependency map from the Tian--Klavzar criterion through Lemmas 3.1/3.3,
  Theorem 3.5, the tree specialization, and the rooted-tree DP.
- It identifies six high-value review blocks: the apex-meeting equivalence,
  the universal quantifier over geodesics in complement convexity, the small
  tree classification, the beta/dissociation distinction, DP boundary-state
  sufficiency and complexity, and conservative literature wording.
- It keeps the Jiang lexicographic-product and all-noncomplete-join results
  separate from the present mixed join and marks the fan path subfamily as
  prior work. It points to `PROJECT_STATUS.md` Section 8 as the authoritative
  complete inventory of `UNKNOWN` items.

### Dependency and independence corrections

- A read-only source audit found that
  `experiments/audit_mixed_join_dp.py` imports three helpers from
  `experiments/audit_extension_candidates.py`. The guide now includes this
  runtime dependency, as well as `tests/` and `requirements.txt`, in the
  reproducibility delivery set.
- The guide explicitly says that the two verification routes use different
  checking logic but share audit-driver infrastructure and NetworkX tree
  generation. This avoids implying two completely disjoint software stacks.
- The earlier `proofs/mixed_join_tree.md` is described as a
  proof-development note rather than an "independent proof note"; it contains
  the same proof chain in an earlier form, not a second independent theorem
  proof.
- The optional historical 92-case report and the full internal handoff files
  are separated from the minimum core review package.

### Validation

- Three bounded read-only reviews (outline/coverage, mathematical hotspots and
  dependency closure, and final guide-to-source consistency) found no
  mathematical, numerical, bibliographic, scope, or novelty/priority error.
- Pandoc parsed the final guide successfully. It contains no non-ASCII
  characters or trailing whitespace. Final length is 174 lines / 1,119 words;
  SHA-256 is
  `4008075091B15508FECEE6FFA07219CA859545DD4EDD2B695CE90B4C49CBA89E`.
- No new theorem, proof, conjecture, experiment, literature search, or
  novelty/priority assessment was introduced. No PDF or compilation log was
  created; the no-TeX-engine limitation remains explicit.
- Unique next step: create a non-self-referential review-package manifest with
  stable-file hashes, sizes, dependency closure, verified commands/results,
  optional historical material, and the explicit absence of compiled output.

## 2026-08-29 — TeX source delivered to Google Drive

### Status before delivery

- Confirmed from the current project handoff that the submission-style source
  `drafts/mixed_join_research_note.tex` exists and has completed static parsing,
  structure checks, and Markdown--LaTeX content parity review.
- Actual TeX compilation has not occurred because this machine has no TeX
  engine. No PDF or compilation log existed before or after this delivery.

### Drive operation and verification

- The connected Google Drive account was searched for an accessible folder
  named `ai4math`, including exact, case-variant, related-name, root-folder,
  and shared-drive checks. No existing matching folder was found.
- Under the user's explicit request to place the prepared TeX source in that
  location, created `ai4math` in My Drive root. Folder ID:
  `1GmHnRNCA_RRscwFqsQnD2KiILnAD3OrH`.
- Uploaded only `mixed_join_research_note.tex` with MIME type
  `application/x-tex`. File ID:
  `1SVkC2udd2568CXOuzXFYp-23tUrR_M81`.
- Verified the write by both file-metadata readback and direct folder listing.
  Both report the intended filename, a size of 43,228 bytes, and the new
  `ai4math` folder as parent. The local source SHA-256 remains
  `B0EE092172447B08480C9CBA14D80BBC7CAD4E475067B8FE762797EE9F7642C9`.

### Scope and next step

- No theorem, proof, conjecture, experiment, literature search, or manuscript
  content changed. The upload is an artifact-delivery action, not evidence of
  successful compilation.
- Unique next step remains actual compilation and page-by-page PDF inspection
  once the user supplies or authorizes an environment with a TeX engine.

## 2026-08-29 — Internal review package manifest completed

### Stable artifact inventory

- Added `notes/review_package_manifest.md` without copying or archiving any
  file. It separates the core reading set, reproducibility dependency closure,
  optional historical provenance, and dynamic handoff files.
- Recorded byte lengths and SHA-256 values for 19 stable files. A parser read
  the tables back from the completed manifest and recomputed every size and
  digest: 19/19 matched with zero missing paths or mismatches.
- `PROJECT_STATUS.md`, `notes/research_log.md`, and the manifest itself are
  deliberately listed without hashes because the first two change when a
  stage closes and self-hashing the manifest would be circular.
- Added `notes/literature_notes.md` as optional citation-chain provenance
  because the current positioning note refers to it. The missing historical
  `notes/literature_search_log.md` remains explicitly absent/`UNKNOWN`, not
  silently represented as part of the package.

### Dependency closure

- Read all direct imports of the main audit and tests. The local execution
  closure is `experiments/audit_mixed_join_dp.py`,
  `experiments/audit_extension_candidates.py`, `src/mixed_join_tree.py`,
  `src/dual_gp_independent.py`, and `src/__init__.py`; the three test files are
  separately included.
- The main audit's only third-party runtime dependency is NetworkX, and the
  tests additionally require pytest. No script reads an external data file or
  an existing JSON report; `results/mixed_join_dp_audit.json` is generated
  output.
- The manifest keeps `requirements.txt` as the broader environment record but
  notes that it does not pin versions. Because the JSON embeds Python and
  NetworkX versions, another environment can reproduce all logical counts yet
  produce a different byte-level JSON hash; such a hash difference alone is
  not evidence of a mathematical failure.
- The ignored `papers_local/` third-party material is excluded from the
  distributable review package pending a separate rights/provenance decision.

### Validation and terminal local status

- Pandoc parsed the manifest successfully; it has no non-ASCII control issue
  or trailing whitespace. Final size is 137 lines / 902 words / 7,781 bytes,
  with SHA-256
  `22BB0301F048D62503BCD49C060476001881B902362F519BA4B2E01A21005667`.
- This stage did not rerun or expand a research experiment. It records the
  already verified 29-test result and four zero-failure audit categories and
  clearly distinguishes them from proofs.
- No theorem, conjecture, literature result, or novelty/priority status
  changed. All existing `UNKNOWN` items remain in force.
- The local package is now internally review-ready. The unique next step needs
  an externally provided or explicitly authorized TeX engine: compile the
  LaTeX source, retain its full log, fix actual typesetting issues, and inspect
  the resulting PDF page by page. No system-level TeX installation was
  attempted or inferred as authorized.

## 2026-08-29 — First external PDF review and post-review source revision

### Input and provenance boundary

- Before project work, reread `AGENTS.md` and all 365 lines of
  `PROJECT_STATUS.md`; the recorded unique task was real compilation and
  page-by-page PDF inspection.
- The user supplied
  `C:/Users/yyt/.codex/codex-remote-attachments/01a04b43-90d7-74f3-9387-27ad52584ddf/2E291CC7-51B4-44EA-9D4C-FC82BCA302F0/1-math.pdf`.
  It is 346,836 bytes with SHA-256
  `2516C872A6ACCAFE8F0690AB3D2DD33B813EF514CA3FAA486F24264509185540`.
- PDF metadata reports 13 A4 pages, pdfTeX 1.40.27, and TeX Live 2025. The
  title, date, theorem/equation structure, text, and previous source state are
  consistent with the uploaded TeX revision, but a PDF cannot by itself prove
  byte-for-byte source identity. The user did not supply the `.log` file.

### Machine and visual PDF checks

- Rendered all 13 pages to PNG at 140 dpi and inspected every page. No text
  clipping, overlap, missing glyph, black box, unresolved `??`, or broken
  equation/reference number was visible.
- `pdffonts` reported only embedded, subsetted Latin Modern/MSBM Type 1 fonts,
  all with Unicode mappings. Bounding-box extraction placed visible words
  within approximately `x=71.1--525.9` points on a 595.276-point-wide page;
  no glyph approached the physical page edge.
- The PDF contains 62 link annotations: 56 internal links and 6 external URI
  links (5 unique targets). All named internal destinations resolved. The DOI,
  Zenodo, and arXiv targets present in the bibliography were preserved.
- Four genuine layout issues were recorded: three introducing sentences were
  separated from their displays at pages 1--2, 2--3, and 7--8; Lemma 3.7 was
  isolated at the bottom of page 5 while its proof began on page 6. The two
  reproducibility tables also had forced word/path breaks, the hash-table
  introduction was separated from its table, and reference [1] ended with a
  one-character DOI line. The final reference page otherwise had no defect.
- Because the full TeX log is absent, this stage does not claim zero
  overfull/underfull boxes, font warnings, duplicate destinations, or rerun
  warnings. Visual success is not a substitute for the missing warning log.

### Independent content review

- Ran three separate read-only reviews focused on mathematics, literature and
  claim language, and typesetting. No critical or major mathematical error was
  found in the two-branch theorem, the tree specialization, the local
  characterization of `beta`, the rooted-tree DP, reconstruction/complexity,
  or the worked star/path families.
- The only formal mathematical gap was that `X` may be empty while the text
  had not declared the maximum degree of the empty induced graph. The revision
  now explicitly sets the empty graph's maximum degree to zero. This closes an
  edge-case convention and changes no theorem, optimization value, or test.
- Corrected the loose complete-factor boundary sentence: under the
  apex-meeting hypothesis, the allowed boundary is `X intersect C = C`,
  equivalently `C minus X` empty; `X intersect C` itself cannot be empty.
- Replaced claims of "independent" computations with the evidenced statement
  that the two bounded routes use distinct checking logic while sharing the
  audit driver and NetworkX-generated trees. Restricted the fan formula claim
  to the checked arXiv v2 rather than treating the unchecked version-of-record
  display as evidence. Added Jiang theorem pinpoints and the `q_2(G)=0`
  convention. Removed the unreferenced dissociation-set label from the
  manuscript while preserving the mathematical `K_{1,3}` separation example.

### Source and layout revision

- Updated both `drafts/mixed_join_research_note.tex` and the content-equivalent
  Markdown source. The abstract now contains the compact definition of
  `beta(T)`; the empty-graph convention and evidence-bounded version language
  appear in both forms.
- In the TeX source, inserted targeted `nopagebreak` guards before the three
  orphaned displays, conditional `needspace` guards before Lemma 3.7 and the
  hash table, ragged-right table columns, directory-boundary path breaks, a
  clean reference-page break, and protection for the final DOI suffix.
- The revised TeX is 43,773 bytes with SHA-256
  `D648DD44CA321475BCA94CBB29C86F22A218738FAE1546C372AAD774F6FAFF1F`.
  The revised Markdown is 36,960 bytes with SHA-256
  `9A76A7E8E6AE9BD0505224234C5BEF6379F713B4753D11FB11F5AEEA03E531A7`.

### Static validation and tests

- Pandoc 2.12 parsed the revised TeX with exit code zero. Static checks found
  35 unique labels, 46 resolved `ref/eqref` uses, 11 resolved citation uses,
  four bibliography entries, and a correctly nested environment stack.
- The two sources retain 13 numbered statements, 13 proofs, 40 display
  formulas, 448 non-QED inline formulas, all five artifact hashes, and five
  `UNKNOWN` occurrences. Removing layout-only `allowbreak` commands still
  reconstructs all five 64-character hashes, each matching its local file.
- Reran `.venv/Scripts/python.exe -m pytest -q tests`: `29 passed in 0.44s`.
  Pytest also emitted one cache-provider warning because `.pytest_cache` could
  not be written. This warning was recorded rather than hidden; it does not
  affect test execution or any mathematical conclusion.
- Updated `README.md`, `notes/collaborator_reading_guide.md`, and
  `notes/review_package_manifest.md`. The manifest's 19 stable rows were read
  back and recomputed: 19/19 sizes and SHA-256 values match.

### Google Drive delivery and unique next step

- Followed the user's standing instruction to use Google Drive for TeX files.
  Read metadata for the existing file ID
  `1SVkC2udd2568CXOuzXFYp-23tUrR_M81`, then replaced its bytes in place rather
  than creating a duplicate. The parent folder remains
  `1GmHnRNCA_RRscwFqsQnD2KiILnAD3OrH` (`ai4math`).
- Metadata and a direct folder listing both read back the same file ID, name
  `mixed_join_research_note.tex`, MIME type `application/x-tex`, and size
  43,773 bytes.
- No literature search, theorem, experiment range, conjecture, or
  novelty/priority conclusion changed. All previously recorded `UNKNOWN`
  items remain in force.
- Unique next step: the user should compile the current Drive revision, retain
  and return the complete `.log` together with the new PDF, after which only
  actual warnings/errors and page-layout regressions will be reviewed.

## 2026-08-29 — v2 external compile/log audit, immutable versioning, and v3 layout revision

### Preflight and scope

- Before project work, reread `AGENTS.md` and every line of
  `PROJECT_STATUS.md`. The recorded unique task was to inspect the current
  revised PDF and complete log, then update artifact status without expanding
  into a new theorem, experiment, or literature search.
- Read the complete PDF skill before PDF inspection and used its render-first
  workflow. Read the Google Drive skill before any cloud write; this caused the
  folder structure to be read back before assigning a version number.
- The user's new standing rule is now explicit: every TeX change creates a new
  numbered version, and a numbered TeX file is never overwritten after a later
  version exists.

### Supplied PDF and source correspondence

- Input PDF:
  `C:/Users/yyt/.codex/codex-remote-attachments/01a04b67-d6a9-7cf0-bc3f-320a09e624c0/8EA23F27-1E15-4CAA-A5AD-D7DA138649BA/1-math.pdf`.
  It is 347,353 bytes, 13 A4 pages, PDF 1.7, with SHA-256
  `CBAD3BEE3568FEC000847095610D021F7C40F1CDADF6D0CB21818B8E372A649C`.
  Metadata reports Producer `pdfTeX-1.40.27` and creation time 29 August 2026
  10:40:37 China Standard Time.
- The PDF contains the revised source's distinctive content: the abstract
  definition of `beta`, the empty-graph maximum-degree convention, Jiang
  theorem pinpoints and `q_2=0` convention, the fan formula restricted to
  arXiv v2, and the wording that the two checks share the audit driver and
  NetworkX tree instances. Lemma 3.7 and its proof are together on page 5, and
  references start cleanly on page 13.
- The supplied log's only overfull locations are lines 927--931 and 931--941;
  those exact lines in the 43,773-byte D648 source are the first `longtable`.
  These content and line-number fingerprints make the PDF/log highly
  consistent with the current source, while not proving byte identity.
- The log records its original `output.pdf` as 343,488 bytes. The attachment is
  347,353 bytes and its header explicitly contains `/Linearized 1 /L 347353`.
  The size/hash/object-layout change is therefore consistent with a
  post-compile linearization rewrite, but the attachment is not claimed to be
  the original logged file byte for byte.

### Complete log audit

- The pasted log is structurally complete from the pdfTeX banner through
  package loading, pages 1--13, `Output written`, memory use, and PDF
  statistics. It records a successful 13-page build.
- Found no TeX/LaTeX error, fatal error, undefined reference, undefined
  citation, missing character, underfull box, or rerun request.
  `rerunfilecheck` says `output.out has not changed`, which is a stable-state
  message rather than an instruction to rerun.
- The only true warning is
  `Overfull \hbox (2.68097pt too wide) in alignment`, reported once for the
  header alignment chunk at lines 927--931 and once for the body chunk at
  lines 931--941. Both reports have one cause: the four-column longtable is
  2.68097 points wider than `\textwidth`. Informational PD1/PU mapping and
  microtype generic-setting messages were not mislabeled as warnings.

### Rendered-page and PDF-structure audit

- Rendered all 13 pages at 160 dpi with `pdftoppm` and inspected every PNG.
  Also used `pdfinfo -isodates`, `pdffonts`, `pdfimages -list`,
  `pdftotext -layout -enc UTF-8`, PowerShell SHA-256, and bundled Python with
  pypdf 6.10.0/pdfplumber for page boxes, character bounds, annotations, URI
  targets, and named destinations.
- Found zero critical or major visual defects. There is no clipping, overlap,
  black box, missing glyph, wrong glyph, unresolved `??`, replacement
  character, or tool token. Page numbers 1--13 are continuous and aligned.
- All 22 font resources are embedded, subsetted, and Unicode-mapped. The PDF
  has 63 link annotations: 57 internal GoTo links, all resolved, and 6 URI
  links; 58 named destinations resolve. One DOI wraps into two clickable
  regions, but both remain valid.
- Minor p.2--3 issue: the sentence “The dual general position number is” is at
  the bottom of p.2 and its display begins p.3.
- Minor p.10--11 issue: the audit-report lead-in ends with “records:” at the
  bottom of p.10 and the longtable starts p.11.
- Minor p.11 issue: the first longtable exceeds the nominal text boundary by
  2.68097 points, matching the log. It remains about 69 points from the
  physical page edge and is not clipped. The second hash table is inside the
  text area and all five split hashes remain recoverable.
- Pages 1, 3--9, 12, and 13 have no additional defect. The lower-page whitespace
  on p.12 is acceptable because the references intentionally start on p.13.
- Removed only the two task-created render directories
  `tmp/pdfs/pdf_visual_audit_1_math_20260829` and
  `tmp/pdfs/source_provenance_audit` after verifying their resolved paths were
  inside the workspace PDF temp root. Historical PDF intermediates were left
  untouched.

### Immutable v2/v3 mapping and v3 changes

- Drive discovery found that `ai4math/` already contained a populated `v2`
  folder and an empty `v3` folder. `ai4math/v2/` contains file ID
  `1SVkC2udd2568CXOuzXFYp-23tUrR_M81`, name
  `mixed_join_research_note.tex`, MIME type `application/x-tex`, and size
  43,773 bytes. Therefore the compiled D648 source was frozen locally as
  `drafts/mixed_join_research_note_v2.tex`; no v1 file was invented.
- Created `drafts/mixed_join_research_note_v3.tex` from v2 and changed only
  layout:
  1. added `\Needspace{6\baselineskip}` before the dual-number lead-in;
  2. added `\Needspace{8\baselineskip}` before the audit-report lead-in; and
  3. changed the first longtable text columns from `0.26/0.41\textwidth` to
     `0.25/0.40\textwidth`, reducing the nominal table width by about 9.06
     points and leaving about 6.38 points of margin relative to the logged
     overfull.
- Added `drafts/TEX_VERSION_HISTORY.md`. It records the immutable-copy rule,
  local hashes, Drive folder/file IDs, compile states, and the PDF/log
  provenance boundary. The unnumbered local TeX remains a legacy byte-duplicate
  of v2 and is no longer an editing target.

### Static validation and Drive delivery

- V3 is 44,087 bytes with SHA-256
  `35C9D1D4816D3C7B39381FF42F5CCAB7064131870AB2458D256B09DA22FF53A6`.
  Pandoc 2.12 parsed it successfully. Static checks found 35 unique labels,
  46 resolved `ref/eqref` uses, 11 resolved citation uses, four bibliography
  keys, and a correctly nested environment stack. It still contains 13
  theorem-like statements, 13 proofs, 40 display formulas, and five `UNKNOWN`
  occurrences.
- No mathematical source or implementation changed, so the prior `29 passed`
  result was not presented as a fresh run. This stage neither reran nor
  expanded a numerical experiment.
- Uploaded v3 as a new file, not an update, into the empty Drive folder
  `ai4math/v3/` (folder ID `1JKUCmJoC7E18skB_FmfbwxtTqG_GvXx_`). Readback by
  both file metadata and folder listing agrees on file ID
  `1A2MepYtCLU80SR9pb011T-lM7iyU2X8M`, name
  `mixed_join_research_note.tex`, MIME type `application/x-tex`, size 44,087
  bytes, and the v3 parent. V2 and the legacy unnumbered cloud history were not
  overwritten.
- Updated README, collaborator guide, review-package manifest, this research
  log, and project status. The manifest now contains 21 stable-file rows; all
  21 sizes and SHA-256 values were recomputed from the workspace and match.

### Claim boundary and unique next step

- This stage changed only artifact validation, pagination, table width, and
  version management. It produced no new theorem, conjecture, calculation,
  literature fact, novelty claim, or priority claim. All existing mathematical
  and literature `UNKNOWN` items remain in force.
- Unique next step: externally compile
  `ai4math/v3/mixed_join_research_note.tex`, retain the complete log from banner
  through PDF statistics, and return both it and the PDF. Check that the two
  lead-ins remain with their display/table, the first longtable has no overfull,
  and all 13 pages have no new regression. Any further TeX edit must be a new
  v4 file; v3 must not be overwritten.

## 2026-08-29 — v3 external compile and final typesetting audit

### Preflight and scope

- Before project work, reread `AGENTS.md` and every line of
  `PROJECT_STATUS.md`. The recorded unique task was to audit the externally
  recompiled v3 PDF and its complete log content, with special attention to
  the three v2 layout findings.
- Read the complete PDF skill and followed its render-first workflow. No PDF or
  TeX authoring operation was performed: the externally supplied files were
  inspected read-only, so no artifact-operation marker was required.
- The review did not reopen mathematics, run a new literature search, alter an
  experiment, or edit the immutable v3 TeX source.

### Supplied artifacts and provenance boundary

- Manuscript PDF:
  `C:/Users/yyt/.codex/codex-remote-attachments/01a04b8e-7d25-7313-b691-ac4131149302/AE565DF1-317D-4B93-B8EA-AA90DB4B734B/1-math.pdf`.
  It is 347,402 bytes with SHA-256
  `566A99646FFEA83983445A1F2BEBEE44B122911061304AC4DBCC839A948D2712`.
  `pdfinfo` reports 13 unencrypted A4 pages, PDF 1.7, Creator `LaTeX`, Producer
  `pdfTeX-1.40.27`, and creation/modification time 29 August 2026 11:24:10
  China Standard Time.
- Displayed-log attachment:
  `C:/Users/yyt/.codex/codex-remote-attachments/01a04b8e-7d25-7313-b691-ac4131149302/AE565DF1-317D-4B93-B8EA-AA90DB4B734B/2-pdf`.
  Its bytes begin with `%PDF-1.3`; it is a 10-page Safari/iOS Quartz PDF
  printout, not the native plain-text `.log`. It is 45,700 bytes with SHA-256
  `9E1A279A710538140F70403CD50EC921A9A17B91A0B27E26BC8F54589C60CC5D`.
  Text extraction and rendered-page inspection show readable log content from
  the pdfTeX banner through the final PDF statistics.
- The log records the compiler's `output.pdf` as 343,570 bytes. The manuscript
  attachment declares `/Linearized 1 /L 347402`; its declared length equals
  its actual length. The 3,832-byte difference is consistent with a
  post-compile linearization rewrite. Page count, producer/time, 58 named
  destinations, manuscript content, and all three v3-specific layout changes
  are mutually consistent, but byte-for-byte identity with the logged
  pre-delivery PDF is not established.
- The local immutable v3 source remains 44,087 bytes with SHA-256
  `35C9D1D4816D3C7B39381FF42F5CCAB7064131870AB2458D256B09DA22FF53A6`.
  The displayed log names `mixed_join_research_note.tex` but records no source
  hash, so exact byte identity between the external compiler input and this
  local source cannot be proved cryptographically.

### Complete displayed-log audit

- The log content begins with pdfTeX
  `3.141592653-2.6-1.40.27`, TeX Live 2025, format date 22 April 2025, and the
  29 August 2026 03:24 build. It proceeds through class/package loading, pages
  1--13, auxiliary-file closure, memory use, `Output written`, and `PDF
  statistics`; no beginning or ending section is missing from the printout.
- Exact and case-insensitive scans found zero TeX/LaTeX error, fatal error,
  emergency stop, warning, overfull or underfull h/vbox, undefined reference,
  undefined citation, undefined control sequence, missing character, multiply
  defined label, or rerun request. Package names containing words such as
  `infwarerr` and `rerunfilecheck` were not misclassified as diagnostics.
- `rerunfilecheck` reports that `output.out` has not changed and gives a
  checksum; this is a stable-state information message, not a rerun request.
  The final line reports `Output written on output.pdf (13 pages, 343570
  bytes)`, followed by PDF statistics including 342 objects and 58 named
  destinations.
- Because the supplied wrapper is a PDF printout, these conclusions apply to
  all displayed log content. They do not assert preservation of the native
  `.log` byte stream or invisible data outside the printed representation.

### PDF structure and 13-page visual review

- Rendered every manuscript page to PNG independently at 160 and 200 dpi and
  inspected all 13 pages. `pdfinfo`, `pdffonts`, `pdftotext`, pypdf, and
  pdfplumber also parsed the file without content-stream or page-box error.
- All 13 MediaBox, CropBox, BleedBox, TrimBox, and ArtBox values are the same
  full A4 box. Every content stream is nonempty. Text-coordinate checks place
  all characters within the page boxes and leave approximately 69--71 points
  at the left/right physical edges; no text touches a page edge.
- All 22 font resources are embedded and subsetted and have `/ToUnicode`
  mappings. Twelve private-use code points are the expected pieces of large
  cases braces on pages 9--10; the rendered braces are correct. No replacement
  glyph, `cid:` token, NUL, `??`, missing glyph, black block, clipping, overlap,
  or exact duplicate glyph box was found.
- The PDF contains 63 link annotations: 57 internal links, all resolved, and
  six structurally valid URI links. All 58 named destinations resolve, all 16
  bookmarks target valid pages, and every link rectangle lies inside its page.
  URI network responses were not tested because link structure, not live Web
  availability, was the task.
- The first v2 regression is fixed: page 3 begins with “The dual general
  position number is” and the defining display follows on the same page. The
  second is fixed: page 11 begins with “The archived report ... records:” and
  the first longtable immediately follows on that page. The table rules span
  approximately x=75.18--520.10 points, remain within the text area, and the
  log contains no overfull report.
- No critical, major, or minor visual defect was found on any page. Page 7--8
  and page 9--10 contain ordinary proof/argument continuations, not orphaned
  headings. The large lower whitespace on page 13 is expected for the short
  references section. Page numbers 1--13 are continuous.

### Documentation, integrity, and claim boundary

- Left `drafts/mixed_join_research_note_v3.tex` byte-for-byte unchanged and
  updated only artifact metadata in `README.md`,
  `drafts/TEX_VERSION_HISTORY.md`, `notes/collaborator_reading_guide.md`,
  `notes/review_package_manifest.md`, `PROJECT_STATUS.md`, and this log.
- The updated stable metadata files have the following fingerprints:
  `README.md` is 2,627 bytes with SHA-256
  `5989E162BB001922DE10CC7184D122AC458305ADBBBA323CCE045D764794AC5A`;
  the collaborator guide is 9,977 bytes with SHA-256
  `D22DE369783119B7D59CBD7ED71C0F2F6A3FE1A35208876ED747B0FD06A60169`;
  and the version history is 3,259 bytes with SHA-256
  `0CDBDECB55CA1522431BF49CB4EBA105469E94CEC70E760C25CE3970577EBC8B`.
  The manifest was updated with these values and remains intentionally
  self-unhashed. A fresh readback recomputed every stable row: 21/21 byte
  counts and SHA-256 values match, with zero missing or mismatched files.
- No mathematical implementation changed, so the earlier `29 passed` result
  was not presented as a fresh test run. No theorem, proof, conjecture,
  computational total, experiment range, literature fact, or novelty/priority
  assessment changed. Every Section 8 `UNKNOWN` remains in force.
- The v3 typesetting stage is complete on the available evidence. The native
  `.log` would improve archival/raw-byte provenance if later supplied, but its
  absence does not block the warning and page-layout conclusions above.
- Unique next step: give the compiled/reviewed v3 package to an external human
  collaborator and request the mathematical and submission review prioritized
  in `notes/collaborator_reading_guide.md`. If that review requires any TeX
  change, create a new v4 from v3; never overwrite v3.

## 2026-08-29 — target-journal screening and local DMGT v4 candidate

### Scope and preflight

- Before project work, read `AGENTS.md` and all 387 lines of
  `PROJECT_STATUS.md`. The first raw read was truncated by the terminal, so the
  status file was reread in three numbered chunks before any file was changed.
- The user requested a shortlist of target journals, a precise list of needed
  personal information, and a corresponding local TeX rewrite, explicitly
  excluding Google Drive. This new direct request replaced the immediate
  formatting priority while preserving external human review as a mandatory
  pre-submission scientific gate.
- Verified before editing that the frozen v3 source remained 44,087 bytes with
  SHA-256
  `35C9D1D4816D3C7B39381FF42F5CCAB7064131870AB2458D256B09DA22FF53A6`.
  It was not edited.

### Official journal and classification checks

- Checked current official journal pages on 29 August 2026. The decision and
  links are recorded in `notes/target_journals_and_author_info.md`.
- DMGT's home page states that it publishes refereed original graph-theory
  papers and includes structural graph results in scope. Its author guide says
  that there is no APC, requests articles not exceeding 30 pages in DMGT
  style, and requires corresponding-author metadata, abstract, keywords, 2020
  MSC, and a PDF no larger than 10 MB. At first submission an ordinary LaTeX
  class is allowed, but the PDF must be one-column and line-numbered; the
  `dmgt` class is required after acceptance. ORCID completion is recommended.
  Sources:
  `https://www.dmgt.uz.zgora.pl/` and
  `https://www.dmgt.uz.zgora.pl/system_pages/guide.php`.
- Verified direct audience precedent in DMGT: Ghorbani et al., “The general
  position problem on Kneser graphs and on some graph operations,” DMGT 41
  (2021), 1199--1213, DOI `10.7151/dmgt.2269`. It treats standard rather than
  dual general position and therefore does not subsume the present theorem.
- Checked the current official scopes of Graphs and Combinatorics, Discrete
  Mathematics, Discrete Applied Mathematics, and Computational and Applied
  Mathematics. The shortlist distinguishes official scope facts from the
  recommendation: DMGT is the fit-first primary target; Graphs and
  Combinatorics and Discrete Mathematics are stretch alternatives; Discrete
  Applied Mathematics is the algorithm-oriented alternative; Computational
  and Applied Mathematics is an additional fallback with a direct product-paper
  precedent.
- Verified the 2020 MSC text from `https://msc2020.org/MSC_2020.pdf` and chose
  `05C12` (distance in graphs) as primary, with `05C05` (trees), `05C69`
  (special vertex subsets), `05C76` (graph operations), and `05C85` (graph
  algorithms) as secondary codes. The closely related DMGT general-position
  paper used `05C12`, `05C69`, and `05C76`, providing an additional topical
  consistency check.
- Verified the survey citation directly from arXiv v5: Ullas Chandran S.V.,
  Sandi Klavžar, and James Tuite, “The General Position Problem: A Survey,”
  arXiv:2501.19385v5, last revised 16 August 2026, DOI
  `10.48550/arXiv.2501.19385`.

### Local v4 changes

- Copied the immutable v3 bytes to a new
  `drafts/mixed_join_research_note_v4.tex` before applying any edit. No cloud
  file or folder was created, read, or updated.
- Prepared v4 as a DMGT first-submission candidate without prematurely
  converting it to the acceptance-only `dmgt` class:
  - loaded `lineno` with mathematical-line support and enabled line numbers;
  - retained the one-column A4 article layout;
  - added explicit placeholders for publishing name, affiliation, public
    corresponding email, and ORCID;
  - added keywords and 2020 MSC metadata;
  - added placeholders for funding, competing interests, author
    contributions, code/data availability, acknowledgements, and accurate
    disclosure of AI-assisted tools;
  - removed the internal-working-draft banner and blank author/date front
    matter;
  - changed remaining self-descriptions from “note” to “paper”;
  - converted literal internal `UNKNOWN` markers into publication-facing
    limitations without claiming that any underlying unknown had been
    resolved;
  - added the verified survey and DMGT graph-operations references and an
    explanatory paragraph distinguishing standard from dual general position.
- Mathematical content was preserved: v3 and v4 both contain 13 theorem-like
  environments, 13 proofs, 34 opening/closing display delimiters, six equation
  environments, nine cases environments, and two longtables. No Python source,
  test, experiment, result matrix, theorem, proof, counterexample, or numerical
  range changed.

### Validation and one repaired defect

- Pandoc 2.12 parsed v4 successfully.
- The first structural scan correctly caught one new authoring defect: a
  conclusion sentence referred to nonexistent label `cor:path-family`. The
  intended target was the existing formula `eq:path-family`; this was repaired
  to `\eqref{eq:path-family}` and the entire scan was rerun.
- Final checks report 35 unique labels, 47 resolved `ref/eqref` uses, six
  unique bibliography keys, 13 resolved cite commands, a correctly nested
  environment stack, 13 theorem-like statements, 13 proofs, and 40 displayed
  formulas. V4 contains 11 `\submissiontodo` calls and zero literal `UNKNOWN`
  tokens. The latter is a presentation fact only; the project `UNKNOWN` list
  remains authoritative.
- V4 is 46,198 bytes and 1,143 lines with SHA-256
  `03035E57EACBE14924EA0C5FF526C75FF98BCB181E23C9B63B2E401807EF7E1B`.
  The target-journal/author-information note is 8,731 bytes with SHA-256
  `47F6DB0292F0CB6E0D526402ABC78A3BBED8EE554B6F1B464ED819907C85BA6E`.
  The updated version history is 4,106 bytes with SHA-256
  `0C6817AEC3B25DC9906FA18EE1691A4769292C380EF0629F014CA1A69A655622`.
- A final handoff-integrity check noticed that the stable review manifest still
  contained the pre-edit README and version-history fingerprints. Updated
  those two rows, explicitly classified v4 and the target-journal note as
  mutable submission-preparation files outside the compiled-v3 digest table,
  and recomputed all stable entries. The manifest now verifies 21/21 rows with
  zero missing, size-mismatched, or hash-mismatched files. The manifest remains
  intentionally self-unhashed.
- No TeX engine is installed locally. Therefore v4 has not been compiled, its
  page count is unknown, and it does not inherit v3's warning-free log or
  13-page visual result. No Python implementation changed, so the earlier
  `29 passed` result was not misrepresented as a fresh test run.

### Claim boundary and unique next step

- The target list is a scope-and-risk recommendation, not an acceptance
  prediction. DMGT's topical fit does not establish originality,
  publishability, novelty, or priority. Jiang's future status, subscription
  database coverage, the fan version-of-record display, an established name
  for the stricter tree parameter, and all out-of-scope classifications remain
  `UNKNOWN`.
- The local-only instruction was followed: there was no Google Drive tool call
  or other cloud mutation.
- Unique next step: the user must supply and approve every author metadata and
  declaration item listed in `notes/target_journals_and_author_info.md`. Until
  then, retain all 11 placeholders and do not circulate or submit v4. After
  metadata completion, external human mathematical/literature review and a
  real compile/log/page audit remain mandatory before any journal submission.

## 2026-08-29 — sole-author metadata completion and Codex disclosure

### Author response and affiliation decision

- Before editing, reread `AGENTS.md` and completed the remaining full read of
  the 396-line `PROJECT_STATUS.md`; continued from its unique metadata task.
- The user confirmed one author, publishing name `Yi Yuteng` (Chinese name
  `易宇腾`), current location Shanghai, China, and public corresponding email
  `yiyuteng29@163.com`. The user reported no other author, ORCID, funding,
  competing interest, or current institutional position.
- Verified the institution named by the user on the official Shanghai Jiao Tong
  University site. The current English name is `SJTU Global College`:
  `https://gc.sjtu.edu.cn/cn/admission/undergraduate-admission/overview/`.
  Because the author has graduated and did not report a current appointment,
  the manuscript uses the honest present affiliation `Independent Researcher,
  Shanghai, China`; the former college is retained only as internal biographical
  context and is not presented as endorsing or hosting this work.
- The user asked whether an acknowledgement could be arbitrary and suggested
  Codex. No person was invented. Checked OpenAI's official sharing and
  publication policy, which calls for a clear description of AI's role and
  ultimate human responsibility:
  `https://openai.com/policies/sharing-publication-policy/`. The manuscript
  therefore acknowledges OpenAI Codex as a tool, separately lists the actual
  assistance categories, states that Codex is not an author, and assigns final
  responsibility to the human author.

### Local v4 changes

- Edited only `drafts/mixed_join_research_note_v4.tex`; the frozen v3 source
  remains byte-for-byte unchanged at SHA-256
  `35C9D1D4816D3C7B39381FF42F5CCAB7064131870AB2458D256B09DA22FF53A6`.
- Replaced the title-page and PDF-author placeholders with `Yi Yuteng`, the
  corresponding email, and `Independent Researcher, Shanghai, China`. Removed
  the absent ORCID field and the now-unused `\submissiontodo` macro.
- Filled declarations with no funding, no competing interests, a concise sole-
  author responsibility statement, and a local-only-compatible policy making
  code and machine-readable audit outputs available from the corresponding
  author on reasonable request. No public repository or persistent identifier
  was claimed.
- Split acknowledgements from the AI-assisted-tools disclosure. The disclosure
  accurately records assistance with literature organization, proof drafting,
  code development, computational checking, manuscript drafting, and editorial
  revision. This disclosure does not itself establish human verification; the
  external review and author-approval gates remain open.
- Recorded the supplied metadata, affiliation rationale, working availability
  policy, and acknowledgement boundary in
  `notes/target_journals_and_author_info.md`. Updated README, version history,
  review manifest, project status, and this log. No Google Drive or other cloud
  tool was called.

### Static validation and artifact integrity

- Pandoc 2.12 parsed the filled v4 successfully. A fresh scan found zero
  `SUBMISSION TODO`, `\submissiontodo`, pending-author, or ORCID markers.
- Structural checks found 35 unique labels, 47 resolved `ref/eqref` uses, six
  bibliography keys, 13 resolved cite commands, a balanced environment stack,
  13 theorem-like statements, 13 proofs, 34 matched display-delimiter pairs,
  and six matched equation environments, for 40 displayed formulas. Author
  metadata and the five declaration headings are present.
- Filled v4 is 46,222 bytes and 1,147 lines with SHA-256
  `8E0BBFD7C2436AF9D0396CBA7C1954A47F75A1AEE2861CA933594320716578DF`.
  The author/target note is 10,992 bytes with SHA-256
  `21A19581FAC4B0D51918707EB6536A9B487821754CFDBF39AB990501D6FE11A7`.
  README is 2,644 bytes with SHA-256
  `9DFC3C6CCFC272750F11B9D57ECFAF96EC3FF1CBD7F192313AB44C87F9D6CA3A`,
  and the updated version history is 4,224 bytes with SHA-256
  `5495DB1579775B8CBB195E36D5331537054A31B2C24D05C9D0C4BF12FECD1D20`.
  After updating those two stable rows, the non-self-referential manifest
  recomputed as 21/21 matching files with zero size or hash mismatch.
- No TeX engine is installed locally, so the filled v4 was not compiled and no
  PDF, native log, page count, warning conclusion, or visual-review conclusion
  was produced. No mathematical implementation changed; the previous
  `29 passed` result was deliberately not described as a fresh test run.

### Claim boundary and unique next step

- This stage changed administrative metadata and disclosure only. It created no
  theorem, proof, experiment, literature result, novelty claim, or institutional
  endorsement. All existing mathematical, literature, publishability,
  novelty/priority, subscription-database, and fan-VOR `UNKNOWN` items remain.
- Unique next step: give the filled local v4 and the frozen compiled v3 baseline
  to an external human collaborator for the mathematical, literature, and
  submission review specified in `notes/collaborator_reading_guide.md`. Any
  review-driven TeX revision must start v5 rather than overwrite v3 or v4; a
  real compile/log/page audit remains mandatory before submission.

## 2026-08-29 — GitHub connection audit and deferred code release

### Read-only connection check

- The user asked whether Codex could directly create a GitHub repository and
  recalled having linked GitHub. Used the plugin-management procedure to verify
  the connection rather than assuming that identity linkage implied repository
  permissions.
- The GitHub integration returned authenticated login `Star5Dust`. Its installed
  account list and accessible repository list were both empty. The available
  GitHub integration operations included writes to existing repositories but no
  create-repository operation. A local PowerShell check also found no installed
  `gh` CLI.
- These results distinguish an authenticated identity from an authorized
  repository installation. No repository was created, no permission was
  changed, no file was uploaded, and no GitHub or Google Drive state was
  mutated.

### Deferred action recorded

- The user asked to defer the task until returning home and having access to a
  computer. Recorded the following user-dependent sequence: create an empty
  private repository under `Star5Dust`; grant the Codex GitHub integration
  access to that repository; select the curated files and an appropriate
  license; then decide when to make it public and whether to archive a release
  on Zenodo for a DOI.
- Until a public repository URL has actually been created and read back, the
  v4 statement remains: code and machine-readable audit outputs are available
  from the corresponding author on reasonable request. No public URL, license,
  or DOI may be invented or inserted early.
- Added this pending item to `notes/target_journals_and_author_info.md` and
  `PROJECT_STATUS.md`. The updated target/author note is 11,698 bytes with
  SHA-256
  `290706978B1C7470F798642F1C52954F8369D195A288BA16B9EE5BF518CF06D7`.
  It remains one of the manifest's intentionally dynamic, unhashed handoff
  files, so the stable review-package digest table does not require a row
  change.

### Claim boundary and unique next step

- This was an administrative connection audit only. No TeX, mathematical
  implementation, test, experiment, theorem, proof, literature fact, or
  `UNKNOWN` status changed, and the previous `29 passed` result was not
  described as a fresh run.
- The unique scientific next step remains external human mathematical,
  literature, and submission review of filled v4 against the frozen compiled v3
  baseline. GitHub publication is a separate deferred, user-dependent item and
  does not replace that next step.

## 2026-08-29 — five local journal-name LaTeX candidates

### Request and source-format audit

- The user asked whether only the DMGT TeX version existed and requested all
  intended submission versions, named by journal and kept locally. Before
  editing, reread `AGENTS.md` and the complete `PROJECT_STATUS.md`, then
  continued from the recorded v4/v3 state. No Google Drive tool or other cloud
  mutation was used.
- Confirmed that, before this stage, only the DMGT-oriented v4 existed as a TeX
  submission candidate; the other four journals were recommendations, not
  separate files.
- Rechecked the relevant official routes:
  - DMGT first submission permits ordinary one-column, line-numbered LaTeX;
    `dmgt` is required after acceptance:
    `https://www.dmgt.uz.zgora.pl/system_pages/guide.php`.
  - Graphs and Combinatorics requires Springer's LaTeX macros and the
    `smallextended` option, with a 150--250-word abstract, 4--6 keywords, MSC,
    and numeric references:
    `https://link.springer.com/journal/373/submission-guidelines`.
  - Discrete Mathematics and Discrete Applied Mathematics were kept on the
    publisher's readable first-submission route using the official
    `elsarticle` class. Their official scope pages are
    `https://shop.elsevier.com/journals/discrete-mathematics/0012-365X` and
    `https://shop.elsevier.com/journals/discrete-applied-mathematics/0166-218X`.
    The detailed ScienceDirect guide endpoint returned HTTP 403 in this
    environment; that access failure was not bypassed or silently treated as a
    successful read.
  - Computational and Applied Mathematics recommends the Springer Nature
    template and specifies a 150--250-word abstract, 4--6 keywords, and an
    author--year reference style:
    `https://link.springer.com/journal/40314/submission-guidelines`.
  - Inspected the official Springer `svjour3` package and the December 2024
    Springer Nature `sn-jnl` package from the publisher's LaTeX support page:
    `https://www.springernature.com/gp/authors/campaigns/latex-author-support`.
    The downloaded template material remained in a temporary directory and was
    not added to the project.

### Files and transformations

- Created `drafts/journal_versions/` and five files named from the journals:
  - `Discussiones_Mathematicae_Graph_Theory.tex`: exact byte copy of v4;
  - `Graphs_and_Combinatorics.tex`: `svjour3` with `smallextended`, Springer
    author/affiliation front matter, numeric references, acknowledgements before
    references, and statements/declarations after references;
  - `Discrete_Mathematics.tex`: `elsarticle` in `preprint,12pt` mode with
    Elsevier front matter and declaration headings;
  - `Discrete_Applied_Mathematics.tex`: the corresponding `elsarticle` route
    with the target journal name;
  - `Computational_and_Applied_Mathematics.tex`: line-numbered `sn-jnl` with
    `sn-mathphys-ay`, Springer Nature front matter, back matter, and six
    bibliography entries alphabetized and labeled for author--year citations.
- Preserved `Yi Yuteng`, `Independent Researcher, Shanghai, China`,
  `yiyuteng29@163.com`, the no-funding/no-competing-interest statements, the
  availability-on-request statement, and the transparent Codex disclosure in
  every file. No ORCID, institution, public repository, grant, person, DOI, or
  other metadata was invented.
- Added `drafts/journal_versions/README.md` with class dependencies, official
  links, hashes, and the validation boundary. Updated the root README, TeX
  version history, target-journal note, review manifest, project status, and
  this log. The five files are format derivatives of v4, not numbered content
  revisions; any review-driven content edit must begin in v5.

### Static validation and exact fingerprints

- Pandoc 2.12 parsed all five TeX files with exit code 0.
- A content-identity scan extracted each file from `\section{Introduction}` to
  the start of its back matter and compared it with the same v4 span. All five
  comparisons were exact. Thus no theorem, proof, computation, citation, or
  limitation in the mathematical body changed during the format split.
- Every file has 35 unique labels, 47 resolved `ref`/`eqref` uses, six
  bibliography entries, 13 resolved cite commands, 13 theorem-like
  environments, 13 proofs, 34 matched `\[...\]` display pairs, balanced named
  environments, zero `TODO`/`TBD`/`PLACEHOLDER`/`FIXME` markers, and the
  confirmed author name and email.
- Exact TeX fingerprints are:
  - Computational and Applied Mathematics: 46,241 bytes,
    `A102B5F3BD3BA1EA8CB012339D15E7993AB4E4A7F2D96FBC9DF79C54562B4E4D`;
  - Discrete Applied Mathematics: 46,172 bytes,
    `D215AC66D586E4D0AACA330AD65466EBE5250CA2E3F6F182F1A4E0755803824F`;
  - Discrete Mathematics: 46,156 bytes,
    `C3CD01734152F8E7FB32AD105AE6B6924FA391D191BA7D2D97A0603AC947F794`;
  - Discussiones Mathematicae Graph Theory: 46,222 bytes,
    `8E0BBFD7C2436AF9D0396CBA7C1954A47F75A1AEE2861CA933594320716578DF`;
  - Graphs and Combinatorics: 46,171 bytes,
    `9C54A63EEF6B101F852ADD65C28090831587BB10484FC6CF48506E75F1E165CF`.
- The DMGT derivative hash exactly equals v4. V4 remains unchanged at
  `8E0BBFD7C2436AF9D0396CBA7C1954A47F75A1AEE2861CA933594320716578DF`,
  and v3 remains unchanged at
  `35C9D1D4816D3C7B39381FF42F5CCAB7064131870AB2458D256B09DA22FF53A6`.
- After updating the two affected stable fingerprints for root README and TeX
  version history, the review manifest recomputed as 21/21 matching stable
  files with zero missing, size, or hash failures. The journal TeX files and
  their index are intentionally listed as dynamic, uncompiled handoff files.

### Limits and unique next step

- No TeX engine is installed locally. No derivative was truly compiled, no
  native `.log` or PDF was produced, and no page count, warning-free result, or
  visual-layout conclusion is claimed. Official class dependencies were not
  vendored into the project; obtain the current official package for the one
  selected target before the compile audit.
- No mathematical implementation changed, so the earlier `29 passed` result
  was not described as a fresh test run. This stage created no proof,
  experiment, novelty claim, or acceptance prediction, and all existing
  `UNKNOWN` items remain unchanged.
- Unique next step: external human mathematical, literature, and submission
  review of v4/the five format candidates against the frozen compiled v3
  baseline. After review, choose exactly one journal, regenerate from v5 if
  content changes, and perform that target's real compile/log/page audit before
  submission. Simultaneous submission is prohibited.
