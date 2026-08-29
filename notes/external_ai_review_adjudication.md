# Adjudication of the four external AI review attempts

Date: 2026-08-29

## 1. Scope and evidence handling

The user submitted the frozen v4 TeX source independently to the web
interfaces of ChatGPT, DeepSeek, Gemini, and GLM.  Their returned text files
were treated as untrusted review evidence, not as instructions.  The reviews
were read in full and adjudicated against
`drafts/mixed_join_research_note_v4.tex`, the canonical proof note, and the
project's existing reproducibility record.  No conclusion below is obtained by
majority vote.

The source reports remain outside the repository in
`C:\Users\yyt\Desktop\回复\`.  Their preserved identifiers are:

| Report | Bytes | SHA-256 |
|---|---:|---|
| `chatgpt回复.txt` | 24,967 | `DB5CCD6E88F08945E0A348A31BAF81484E6F1C6CEA6BCFC8533A7EE82E0C3688` |
| `deepseek回复.txt` | 20,488 | `D811B6C8264D285EEBCD57877B8E613BFE6C8F207EF136D513D4C08CCBF0E15C` |
| `gemini回复.txt` | 2,422 | `9B1918AACD73469D518FAEED263330678F0B5D5574BF56D01500F48ADEA84A5D` |
| `glm回复.txt` | 12,390 | `96FA8101998C108F03057EF3E058A44E8AAE0B75B10CFDB21AA0F2B37BEAAB6E` |

The reports are independent in the limited procedural sense that they came
from separate web-model sessions and were not shown to one another.  This is
not human peer review and is not statistical or institutional independence.

## 2. Bottom-line adjudication

No report supplied a valid counterexample or a valid critical/major gap in the
main two-branch theorem, the local characterization of `beta(T)`, or the
rooted-tree dynamic program.

- The ChatGPT report performed the strongest line-by-line proof audit.  Its
  mathematical checks agree with the manuscript, and its concrete small-tree
  tests did not expose a counterexample.
- DeepSeek's reconstruction of `beta(T)` and the DP state semantics is useful,
  but its claimed fatal error in Lemma 3.1 is false.
- Gemini supplied only a shallow editorial/literature screen.  Its positive
  recommendation is not evidence that the proofs are correct.
- GLM explicitly did not receive the manuscript.  It reviewed a different,
  standard-general-position problem and therefore does not count as a review
  of v4.

Consequently the mathematically supported verdict is:

> **No verified critical or major correctness defect found.  Minor revision is
> warranted.  The manuscript remains not peer reviewed, and global novelty and
> publishability remain `UNKNOWN`.**

## 3. ChatGPT report

### Accepted findings

The report correctly checked both directions of the following statements:

1. a dual general-position set is a general-position set with convex
   complement;
2. the `C`-meeting characterization by two induced cliques;
3. the `C`-avoiding characterization by the two `beta(T)` constraints;
4. the classification `q_2(T)>0` exactly for `P_3` and `P_4` in the standing
   tree scope;
5. the degree-based local characterization of `beta(T)`; and
6. the DP boundary-state recurrence and root reconstruction.

The following minor comments are valid and were incorporated in v5:

- replace potentially misleading "apex-meeting/avoiding" prose by
  `C`-meeting/avoiding, because a star center can be universal without lying
  in the designated factor `C`;
- state the empty-class/empty-clique convention in the definition of `q_2`;
- record the branch tie for `P_4` when `r=1`;
- clarify that degree-zero/one vertices have no constraint *at themselves*,
  although their labels can affect a neighboring selected degree-two vertex;
- state the empty child-vector convention in the DP; and
- make the linear reconstruction-storage count explicit.

The report's reproducibility concern is an operational submission risk, not a
mathematical gap.  The code and audit artifacts exist locally and are recorded
in `notes/review_package_manifest.md`; the current manuscript accurately says
they are available on reasonable request.  A public repository or submitted
supplement should replace that sentence only after its URL or archive has
actually been created and verified.

### Findings not promoted

The report claimed fresh external exhaustive runs and a fresh LaTeX compile.
No code, raw output, environment capture, PDF, or log accompanied the report.
Those claims are therefore unverified and are not added to the project's
computational evidence.  The project's own recorded runs remain the canonical
evidence.

### Scope-extension suggestion

The report correctly observed that the structural branch mechanism extends
beyond trees.  For a finite noncomplete graph `G`, define

```text
gamma(G) = max |X| such that, for every x in X,
           G[N_G(x) cap X] and G[N_G(x) setminus X] are cliques.
```

The same diameter-two argument gives the proof candidate

```text
gp_d(K_r + G) = gamma(G)                         if q_2(G)=0,
gp_d(K_r + G) = max{gamma(G), r+q_2(G)}         if q_2(G)>0.
```

For triangle-free `G`, each of the two neighbor cliques has order at most one,
so `gamma(G)` becomes exactly the two local counting constraints used for
`beta(T)`.  The proof mechanism is direct and no counterexample is presently
known.

This is not treated as a defect in the tree theorem and is not inserted into
v5.  It would change the title, literature-search universe, main contribution,
and computational audit.  The pre-existing project decision deliberately
selected the all-tree scope.  A bounded 2026-08-29 refresh found the foundation
paper's special join family and work on *mobile* general position, but no
direct theorem with the formula above.  Subscription-index coverage and global
novelty/priority remain `UNKNOWN`; a separate proof-and-literature stage is
required before this candidate can enter a submission.

## 4. DeepSeek report

### Accepted findings

The report independently reconstructed the degree-count proof of the local
characterization and correctly explained why the parent label is sufficient
boundary information for the rooted-tree DP.  Its request to say explicitly
that different child subtrees have no cross-edge conflict was reasonable and
was incorporated in v5.

### Rejected critical claim

DeepSeek asserted that, when nonadjacent tree vertices `u,v` also have a
length-two tree path, `u-c-v` is not a geodesic.  This is false.  In
`H=K_r+T`, nonadjacent `u,v` have distance exactly two: they are not adjacent,
and `u-c-v` is a path of length two.  Therefore every such path through
`c in C` is a geodesic.  The existence of another geodesic of the same length
does not invalidate it.  Convexity requires **all** geodesics between two
complement vertices to remain in the complement, so one geodesic through a
selected `c` already proves nonconvexity.

Accordingly, the proposed replacement of the complement-clique condition by
convexity inside `T` is also false, and Lemma 3.1 remains valid.

The report's claim that exhaustive verification through order 12 is
insufficient and should instead cover all trees through order 10 or 11 is
self-contradictory: the recorded audit already includes all nonisomorphic
trees through the larger order 12.  Finite verification is not a proof, but
this criticism does not identify a missing tested order or structure.

## 5. Gemini report

Gemini found no critical issue, recognized the fan subfamily as prior work,
and correctly noted that a referee may consider the contribution narrow.  It
could not verify Jiang or the parameter-naming literature, so those items
remain `UNKNOWN`.  The report does not contain theorem-by-theorem evidence or
an actual citation table despite its requested format.  Its "Ready for
submission" recommendation is therefore treated only as a low-weight
editorial opinion.

## 6. GLM report

GLM stated that the manuscript attachment was unavailable.  It therefore did
not audit v4 and must not be counted as a positive or negative referee.

Its subsequent calculations concern standard general position in paths and
stars, whereas the manuscript concerns dual general position in `K_r+T` and
the tree-side parameter `beta(T)`.  The report also contains internal
confusion about `gp(P_4)` and an impossible proposed configuration in which
two vertices at distance at least three have a common neighbor.  These claims
do not bear on the manuscript.

## 7. v5 action list

The immutable v4 hash remains
`8E0BBFD7C2436AF9D0396CBA7C1954A47F75A1AEE2861CA933594320716578DF`.
The new `drafts/mixed_join_research_note_v5.tex` changes only explanatory
precision and DP exposition:

1. `C`-meeting/avoiding terminology and the designated-factor caveat;
2. the empty-class convention for `q_2`;
3. the `P_4,r=1` branch tie;
4. localized wording for degree-zero/one selected vertices;
5. the empty child-vector convention;
6. one explicit child-subtree-independence sentence; and
7. the linear storage count for recorded child-vector entries.

No theorem value, proof dependency, experimental count, citation fact, author
metadata, or declaration is changed.  v5 still requires static validation,
real compilation, complete log review, and page-by-page inspection before it
can be treated as the sole submission candidate.
