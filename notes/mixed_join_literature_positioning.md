# Systematic literature positioning for the mixed join `K_r + T`

Date: 2026-08-28

## 1. Scope and status labels

This audit concerns only the already proved project theorem for

```text
gp_d(K_r + T),  r >= 1,  |V(T)| >= 3,
```

where `T` is a tree.  It does not start the dormant `P_n circ T` or arbitrary
first-factor directions.

The labels used below are:

- **LITERATURE FACT**: verified in a specified source or metadata record;
- **DIRECT LOGICAL DEDUCTION**: follows from verified statements;
- **PROJECT PROOF**: proved in `proofs/mixed_join_tree.md`;
- **NOT FOUND IN THIS AUDIT**: no matching result was found in the recorded
  coverage; this is not a proof that the problem is open;
- `UNKNOWN`: the available evidence does not settle the point.

Search cutoff: 2026-08-28.  MathSciNet, Scopus, and Web of Science were not
directly accessible.  OpenAlex and Semantic Scholar were not usable as negative
evidence for the reasons recorded below.

## 2. Jiang record and version audit

### Current metadata

The Zenodo API record `22116770` still reports:

- title: *Dual General Position in Lexicographic Products with a Complete First
  Factor*;
- author: Weiqi Jiang;
- version: `v1.0.1`;
- publication date: 2026-08-27;
- DOI: `10.5281/zenodo.22116770`;
- concept DOI: `10.5281/zenodo.22081165`;
- resource type: `publication/preprint`;
- record update time: `2026-08-27T03:02:35.559335+08:00`.

The older record `22081166` remains available as `v1.0.0`, publication date
2026-08-24, DOI `10.5281/zenodo.22081166`, with the same concept DOI.  The
current Zenodo record has no `related_identifiers` entry pointing to a journal
article.  DataCite classifies `10.5281/zenodo.22116770` as a preprint and lists
only the `IsVersionOf` relation to the concept DOI.  Crossref has no work record
for this Zenodo DOI, as expected for a DataCite DOI.

**Verdict:** no version after `v1.0.1` and no peer-reviewed relation was found in
this audit.  Future revision, correction, or journal publication remains
`UNKNOWN`.

### Mathematical boundary

The previously checked PDF states that Jiang Theorem 5.1 treats complete joins
whose factors are all nonempty and noncomplete, while mixed joins containing
both complete and noncomplete factors are left unclassified.  Thus
`K_r + T`, for a noncomplete tree `T`, is outside that theorem.  Jiang's
complete-first-factor formula concerns `K_m circ G` and does not determine the
mixed join `K_r + T`.

## 3. Reproducible query matrix

### arXiv API

Endpoint: `https://export.arxiv.org/api/query`.  The following `search_query`
strings were run with `max_results=50`.

| Query | Count | Screened result |
|---|---:|---|
| `all:"dual general position"` | 3 | Tian--Klavzar foundation; strong/lexicographic-product paper; vertex/edge-removal paper |
| phrase plus `join` | 0 | no record |
| phrase plus `cone` | 0 | no record |
| phrase plus `"universal vertex"` | 0 | no record |
| phrase plus `tree` | 0 | no record |
| phrase plus `"dynamic programming"` | 0 | no record |
| phrase plus `lexicographic` | 1 | strong/lexicographic-product paper |

The very recent Jiang Zenodo preprint is not an arXiv record, so its absence
from these counts illustrates an indexing boundary rather than irrelevance.

### DataCite API

Endpoint: `https://api.datacite.org/dois`, page size 100.

| Query | Count | Screened result |
|---|---:|---|
| `titles.title:"dual general position"` | 3 | Jiang concept DOI, v1.0.0 DOI, and v1.0.1 DOI |
| preceding phrase plus `join` | 3 | the same three Jiang records; `join` is matched outside the title field |
| preceding phrase plus `lexicographic` | 3 | the same three Jiang records |
| preceding phrase plus `cone` | 0 | no record |
| preceding phrase plus `"universal vertex"` | 0 | no record |
| preceding phrase plus `tree` | 0 | no record |
| preceding phrase plus `"dynamic programming"` | 0 | no record |

The three DOI hits represent one intellectual work and its versions, not three
independent papers.

### zbMATH Open REST API

Endpoint: `https://api.zbmath.org/v1/document/_search`, page size 100.

| Query | Count | Screened result |
|---|---:|---|
| `"dual general position"` | 3 | foundation DOI `10.1007/s40840-024-01788-z`; product DOI `10.1007/s40314-025-03547-7`; removal DOI `10.1016/j.dam.2026.02.044` |
| phrase plus `lexicographic` | 1 | product paper |
| phrase plus `join` | 0 | no record |
| phrase plus `cone` | 0 | no record |
| phrase plus `"universal vertex"` | 0 | no record |
| phrase plus `tree` | 0 | no record |
| phrase plus `"dynamic programming"` | 0 | no record |

Jiang was not in this index at the cutoff date.  The zero rows are therefore
bounded index results, not claims about all literature.

### Crossref and exact DOI checks

Crossref free-text queries such as `dual general position join graph`, `cone`,
`universal vertex`, `tree`, `fan`, `wheel`, and `convex complement` returned
very large noisy totals dominated by unrelated uses of the words.  These totals
were not used as negative counts.  The top 20 records for each query were
screened; relevant results were already-known general-position papers.

The exact DOI request for `10.1016/j.dam.2026.02.044` confirms a journal article
in *Discrete Applied Mathematics* 388 (2026), pp. 56--64, published in July
2026.  Its Crossref record has no relation to Jiang.

### OpenAlex, Semantic Scholar, and OpenCitations

- OpenAlex alternated between HTTP 429 responses and contradictory zero-result
  responses even for known exact titles.  No zero from OpenAlex is used as
  evidence.
- All five Semantic Scholar API requests returned HTTP 429.  No result count is
  inferred.
- OpenCitations Index v2 returned five DOI-linked citations to the foundation
  paper, one to the product paper, and zero to the removal DOI and Jiang DOI.
  These counts were used only as discovery aids.  In particular, the index
  misses known version-level citation links and cannot support a novelty claim.

### General web and phrase search

Representative exact combinations included:

```text
"dual general position" +
  join / mixed join / complete join / cone / apex / universal vertex /
  tree / fan graph / wheel graph / split graph / complete split graph /
  K_r / dynamic programming
```

Searches without the exact invariant also combined `general position`, `convex
complement`, `join`, `cone`, and tree-set conditions.  This broader search found
nearby standard-general-position and dissociation-set literature, but only one
direct additional overlap for the dual invariant: fan graphs, discussed next.

### Current survey

The arXiv API still reports *The General Position Problem: A Survey* as
`2501.19385v5`, updated 2026-08-16.  Its dual-general-position section predates
Jiang and does not supply a mixed-join tree theorem.  It does cover the
foundation, product, Sierpinski, glued-tree, and removal directions already
recorded in `notes/literature_notes.md`.

## 4. Included and excluded sources

| Source | Inclusion reason | What it does not cover |
|---|---|---|
| Tian--Klavzar (2025), DOI `10.1007/s40840-024-01788-z` | Defines dual general position; Theorem 3.1 gives the general-position plus convex-complement criterion; Proposition 3.5 treats `P_m + 2K_1` | No formula for `K_r+T`; `2K_1` is noncomplete, not the complete factor `K_r` |
| Dokyeesun--Klavzar--Kuziak--Tian (2026), DOI `10.1007/s40314-025-03547-7` | Main product context and source of the complete-first-factor open problem | No mixed-join tree formula |
| Tian--Dokyeesun--Klavzar (2026), DOI `10.1016/j.dam.2026.02.044`, arXiv `2510.01294v2` | Gives the exact dual general position number of fan graphs `F_n=K_1+P_n`; this is a direct subfamily of the project theorem | Does not treat arbitrary trees or `r>1` |
| Jiang (2026), DOI `10.5281/zenodo.22116770` | Exact complete-first-factor theorem and noncomplete-factor join theorem; explicitly identifies the mixed-join boundary | Preprint; mixed complete/noncomplete joins are excluded |
| Tian--Xu--Chao (2023), DOI `10.1007/s40840-023-01592-1` | Supplies the standard general-position formula for fans used by the removal paper | Standard `gp`, not dual `gp_d`; no arbitrary-tree mixed join |
| Ghorbani et al. (2021), DOI `10.7151/dmgt.2269`, and later survey/polynomial papers | Standard general-position formula for an arbitrary join | The convex-complement condition needed for `gp_d` is absent, so the formula cannot be substituted for the project theorem |
| Dissociation-set literature, e.g. Tu--Zhang--Shi (2021), DOI `10.1002/jgt.22627` | Closest named set system to `Delta(T[X])<=1`; tree algorithms and structure results exist for dissociation sets | `beta` also requires every selected vertex to have at most one neighbor outside `X`; no exact identification with a named parameter was found |
| Klavzar et al. (2026), DOI `10.1016/j.dam.2025.10.041` | Contains joins in the title and search results | Studies **mobile** general position, a different invariant |

All other screened candidates were excluded because they concerned standard,
outer, edge, lower, monophonic, or mobile general position; mutual visibility;
non-join products; or graph-theoretic uses of “dual” unrelated to `gp_d`.

## 5. The fan overlap and a preserved version discrepancy

The direct overlap is important and must be cited in any manuscript.

In arXiv v2 of the removal paper, the authors define `F_n` as the graph obtained
from `P_n` by adding one universal vertex and state, for `n>=4`,

```text
gp_d(F_n) = floor(2(n+1)/3).
```

They also state that a maximum general-position set is dual.  The displayed
value is equivalent to `ceil(2n/3)`, the fan formula from the cited 2023 paper.

There is a genuine version discrepancy that must not be hidden: the older
author-hosted v1 PDF displays `ceil(2(n+1)/3)`, whereas arXiv v2 displays
`floor(2(n+1)/3)` and adds the independent-edge description.  The v2 expression
is consistent with the cited fan result and with the project theorem; the two
expressions differ when `n` is divisible by 3.  The body of the paywalled
version of record was not independently compared during this audit, so the
exact displayed expression in the VOR is `UNKNOWN`.

For `r=1` and `T=P_n`, the project theorem recovers this entire fan subfamily.
Consequently, the fan case cannot be advertised as new.  The actual extension
is from paths to all trees, from one universal vertex to an arbitrary universal
clique `K_r`, and from a closed fan value to a structural two-branch theorem and
linear reconstruction algorithm.

## 6. Position of the `beta(T)` parameter

Every beta-feasible set is a dissociation set because it induces maximum degree
at most one.  The converse is false: in `K_{1,3}`, the center together with one
leaf is a dissociation set, but it violates the beta outside-neighbor constraint.
Thus existing dissociation-number algorithms do not directly compute `beta`.

The project proof gives a sharper tree-specific characterization:

- vertices of degree at least three cannot be selected;
- a selected degree-two vertex has exactly one selected neighbor;
- selected leaves have no additional restriction.

Searches for this combined condition and for tree dynamic programming did not
find an established named parameter or the same four-boundary-state recurrence.
The strict conclusion is **NOT FOUND IN THIS AUDIT**.  Whether `beta` is already
known under substantially different terminology remains `UNKNOWN`.

## 7. Real mathematical increment

| Component | Prior position | Project increment |
|---|---|---|
| Dual-set criterion | Tian--Klavzar Theorem 3.1 | Used, not new |
| All-noncomplete joins | Jiang Theorem 5.1 | Not reproved as the contribution |
| Mixed join `K_r+T` | Explicitly outside Jiang; no exact general result found | Exact apex-meeting/apex-avoiding classification |
| Fan `K_1+P_n` | Already exact in the removal paper | Recovered as a consistency check, not new |
| All trees with `r=1` | No exact theorem found | Exact formula through `beta(T)` plus `P_3,P_4` boundary |
| Arbitrary `r>=1` | No exact theorem found | Shows the value is independent of `r` except for `P_3,P_4` |
| Tree optimization | Dissociation literature is related but not equivalent | Local characterization, linear-time value computation, and maximum-set reconstruction |
| Verification | No external computation found for this family | Independent DP/subset and shortest-path audits; evidence, not proof |

This is a meaningful and self-contained increment relative to the sources
checked.  It is not a proof of global novelty.

## 8. Research-note feasibility verdict

### Verdict: **CONDITIONAL GO FOR AN INTERNAL DRAFT**

Reasons supporting a note:

1. the theorem fills a boundary explicitly excluded by the closest exact
   preprint;
2. the star counterexample shows that the result is not obtained by simply
   adding a complete-factor term to Jiang's formula;
3. the result classifies all dual sets by two branches, not only the maximum
   value;
4. `beta(T)` has a clean local structure and an `O(n)` value/reconstruction
   algorithm with two independent bounded audits;
5. the published fan formula is recovered as a transparent prior subcase.

Reasons the verdict is conditional:

1. the full-field openness/novelty status remains `UNKNOWN` because
   MathSciNet, Scopus, and Web of Science were not checked directly and two open
   indexes were unavailable;
2. Jiang is one day old at the cutoff and may change rapidly;
3. the fan subfamily is already published, so the manuscript must state the
   broader-tree and arbitrary-`r` increment precisely;
4. a referee may view the DP as routine unless the structural classification,
   reconstruction, boundary cases, and relation to dissociation sets are made
   explicit.

The result is therefore strong enough to justify drafting, but not strong
enough to authorize the sentence “this problem is new/open” or a submission
without another final metadata/index check.

## 9. Proposed research-note structure

1. **Introduction and precise literature position** — foundation criterion,
   product problem, Jiang boundary, and the published fan subcase.
2. **Preliminaries** — dual general position, convexity, complete joins, and
   the two-clique parameter `q_2`.
3. **Two-branch structure theorem** — dual sets meeting and avoiding `K_r`.
4. **Tree specialization** — `P_3,P_4`, definition and local characterization
   of `beta(T)`, and the preserved `K_{1,3}` counterexample.
5. **Linear rooted-tree DP and reconstruction** — recurrence, induction proof,
   and complexity.
6. **Known subfamilies and examples** — fan formula, stars/complete split
   examples, long paths, and why the value is usually independent of `r`.
7. **Reproducibility** — independent checker design and bounded audit tables,
   explicitly labelled computational evidence.
8. **Conclusion and limitations** — no claim beyond mixed joins over trees;
   Jiang/peer-review and novelty status stated accurately.

## 10. Required additions before submission

- [x] add an explicit fan corollary and show
  `floor(2(n+1)/3)=ceil(2n/3)` so the prior overlap is unmistakable;
- [x] add a short comparison between `beta` and the dissociation number, without
  claiming that `beta` is a new named parameter;
- [x] include at least stars and subdivided stars as worked structural examples;
- [ ] check the version-of-record body of DOI `10.1016/j.dam.2026.02.044` for the
  floor/ceiling display;
- [x] rerun the Jiang version/related-identifier and exact-title searches
  at the 2026-09-02 v8 validation cutoff (refresh again if submission is delayed);
- [ ] if human access becomes available, check MathSciNet, Scopus, and Web of
  Science and record the result; absence there would still be search evidence,
  not a proof of novelty;
- [x] keep the manuscript self-contained so correctness does not depend on the
  peer-review status of Jiang.

## 11. Historical next step (completed)

Begin a self-contained research-note draft using the structure above.  The
first drafting pass should write the introduction/literature-position section,
preliminaries, and the two-branch theorem, and should include the fan subcase as
prior work.  Do not expand to `P_n circ T` or arbitrary `F circ G`.

This drafting step was completed on 2026-08-29 and expanded, within the same
mixed-join scope, to the full internal draft in
`drafts/mixed_join_research_note.md`. The active unique next step is maintained
only in `PROJECT_STATUS.md`.

## 12. Post-draft metadata and literature refresh (2026-08-29)

This refresh was performed after the first complete internal draft. It updates
only the bounded sources below and does not establish global novelty.

### Jiang versions and publication links

- The Zenodo versions endpoint reports exactly two versions: v1.0.0, record
  `22081166`, DOI `10.5281/zenodo.22081166`, dated 2026-08-24; and v1.0.1,
  record `22116770`, DOI `10.5281/zenodo.22116770`, dated 2026-08-27.
- v1.0.1 remains the latest version. Its record update time is still
  `2026-08-27T03:02:35.559335+08:00`, its resource subtype is `preprint`, and
  the record has no related journal identifier.
- The two archived file names, sizes, and MD5 values are unchanged. In
  particular, the PDF MD5 is `ec460cc54eb00426b564476da3084c1b` and the
  supplement MD5 is `fa70a97d33f8a1a514c0b7f2a166d752`.
- DataCite still returns three DOI records for the exact title: the concept DOI,
  v1.0.0 DOI, and v1.0.1 DOI. The current DOI remains classified as a Preprint
  with version `v1.0.1`; its only related identifier is `IsVersionOf` the
  concept DOI `10.5281/zenodo.22081165`.

No newer Jiang version, correction, or peer-reviewed link was found in these
records. Future changes remain `UNKNOWN`.

### Index and citation refresh

| Source | Refreshed observation | Bounded interpretation |
|---|---|---|
| arXiv API, exact phrase `"dual general position"` | 3 records: foundation, product, and removal, unchanged | no Jiang or mixed-join record in this query |
| DataCite, exact-title query | 3 DOI records for the one Jiang concept/version family, unchanged | not three independent works |
| zbMATH Open, exact phrase | 3 records: foundation, product, and removal, unchanged | exact Jiang-title query returned no record |
| Crossref, Jiang-title query | no exact Jiang work record; noisy top results begin with the product paper | Crossref remains unsuitable for a negative free-text count here |
| OpenCitations v2 | 5 citations to foundation, 1 to product, 0 to removal, 0 to Jiang | the sole product citation returned is arXiv `2601.19769`; counts are incomplete discovery aids |
| Crossref cited-by metadata | foundation 6, product 1, removal 0 | disagreement with OpenCitations is retained rather than reconciled by assumption |
| OpenAlex | exact Jiang title returned 0, but a DOI query for the known product paper also returned 0 | coverage failure; no negative inference |

No newly returned record covers `gp_d(K_r+T)` for all trees and arbitrary
`r`. This is **NOT FOUND IN THIS BOUNDED REFRESH**, not a novelty or openness
proof.

### Fan version-of-record attempt

- Crossref still identifies DOI `10.1016/j.dam.2026.02.044` as the journal
  article in *Discrete Applied Mathematics* 388 (2026), pp. 56--64, and exposes
  Elsevier text-mining links labelled as VOR.
- An unauthenticated request to the Elsevier text endpoint returned HTTP 400
  with an unauthorized/minimized-metadata warning; the ScienceDirect article
  page returned HTTP 403 to a direct request.
- A visual in-app browser attempt reached a Cloudflare human-verification
  CAPTCHA. It was not solved or bypassed. The author's current publication-list
  PDF link still resolves to arXiv v2, not a separately identifiable VOR PDF.

Therefore the exact fan formula display in the version-of-record body remains
`UNKNOWN`. The checked arXiv v2 floor formula remains the manuscript's explicit
source for that display.

## 13. DAM v8 pre-submission refresh (2026-09-02)

This is a bounded metadata and source refresh, not a new full-database search
or a proof of novelty. No subscription database was newly accessed.

- The [Zenodo record API](https://zenodo.org/api/records/22116770) still
  identifies Jiang's latest preprint as v1.0.1, dated 2026-08-27, DOI
  `10.5281/zenodo.22116770`, updated
  `2026-08-27T03:02:35.559335+08:00`, with no related journal identifier.
  Its [versions endpoint](https://zenodo.org/api/records/22116770/versions)
  returns only v1.0.1 (`22116770`) and v1.0.0 (`22081166`).
- The [DataCite DOI record](https://api.datacite.org/dois/10.5281/zenodo.22116770)
  remains findable, version v1.0.1, updated `2026-08-26T19:02:36Z`.
  Its only related identifier is `IsVersionOf` the concept DOI
  `10.5281/zenodo.22081165`; it supplies no journal relation.
- A Crossref title-weighted query for Jiang's exact title, inspecting the top
  ten returned candidates, did not return an exact title match. Its first
  result was the known product paper, DOI `10.1007/s40314-025-03547-7`.
  Crossref's broad `total-results` value is not a count of exact title matches.
  Web searches for the exact title, version DOI, and author/title with journal
  terms likewise yielded no new identifiable Jiang publication. This is only
  a negative result within those queries, not evidence of exhaustive coverage.
- The [arXiv API](https://export.arxiv.org/api/query?id_list=2510.01294) still
  gives `2510.01294v2`, updated `2026-02-03T06:35:52Z`, for the removal paper.
  The [Crossref DOI record](https://api.crossref.org/works/10.1016/j.dam.2026.02.044)
  identifies its journal publication as *Discrete Applied Mathematics* 388
  (2026), 56--64, with publication date parts `[2026, 7]`.
- The [author publication list](https://users.fmf.uni-lj.si/klavzar/papers-all.htm)
  confirms the same journal citation. Its linked
  [PDF](https://users.fmf.uni-lj.si/klavzar/preprints/2510.01294v2.pdf)
  is still the 17-page arXiv v2, not a separately identifiable version of
  record. Section 3.3, PDF page 9, was read visually: it treats fans for
  `n >= 4` and displays `gp(F_n) = gp_d(F_n) = floor(2(n+1)/3)`.
  Accessible ScienceDirect metadata/abstract material does not display the
  fan formula. The exact version-of-record body remains `UNKNOWN`.

The manuscript therefore keeps the same six bibliography entries and the
explicit arXiv-v2 attribution for the fan display. Only its Jiang literature
cutoff date advances to 2 September 2026. Jiang's future publication status,
global novelty/priority, subscription-index coverage, and the fan VOR wording
remain unresolved. The active unique next step is in `PROJECT_STATUS.md`.
