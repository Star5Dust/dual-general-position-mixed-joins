# Adjudication of the GLM 5.3 adversarial review and v6 actions

Date: 2026-08-29

## 1. Evidence boundary

The user's GLM 5.3 report was read in full and treated as untrusted review
evidence rather than as instructions. Its source file was outside the
repository at
`C:\Users\yyt\.codex\attachments\1fad3539-a77c-405f-9b63-30ebc68d86bf\pasted-text.txt`.
It contained 14,927 bytes and had SHA-256
`148C257B0F1F73E9D7FD6C942AA76B146F2570CD8499C8913918194FEDA8B284`.

The report says that it received the manuscript PDF but no code, data, project
notes, or other reviews. Its claimed hand enumeration and proof tracing were
not accompanied by machine-readable output. They are therefore useful review
testimony, but they are not added to the project's computational record.

## 2. Bottom-line mathematical adjudication

No critical or major mathematical correctness defect was identified. The
report's checks of Lemmas 3.1, 3.3, 3.6, and 3.7, Corollaries 3.2, 3.4, and
3.8, Theorem 3.5, the local characterization, the rooted-tree recurrence,
reconstruction, complexity, and the worked families agree with the canonical
proof note and the prior independent audit.

The main formula, the two-branch split, every theorem value, and the proof
dependency graph are unchanged in v6. In particular, the piecewise condition
in Theorem 3.5 remains necessary: when `q_2(T)=0`, there is no `C`-meeting
branch, so an unconditional expression `max{beta(T), r+q_2(T)}` would be
wrong.

This remains AI review, not qualified human peer review. Global novelty,
priority, and ultimate publishability remain `UNKNOWN` because the bounded
literature audit does not replace full subscription-index coverage or an
editorial decision.

## 3. Major comments

### C1: reproducibility

Accepted as an operational submission weakness, although the report's claim
of a logical contradiction between hashes and availability on request is too
strong. Exact hashes can identify privately supplied artifacts, but a reader
cannot reproduce them without receiving the files.

V6 closes the practical problem without changing the private GitHub state:

- `requirements-lock.txt` pins the complete installed Python environment;
- the audit now includes 184 definition-first feasibility checks of the sets
  reconstructed by the tree DP;
- `REPRODUCIBILITY.md` records clean commands and evidence boundaries;
- `artifacts/mixed_join_v6_reproducibility.zip` packages the source, tests,
  reports, proof note, locked environment, and instructions;
- the archive was extracted into a clean directory, where `30 passed` and a
  byte-identical main JSON report were reproduced; and
- the manuscript now says that this fixed archive accompanies the submission
  as supplementary material instead of promising availability on request.

The archive is 21,868 bytes and has SHA-256
`0E91BAAC07EFA121784CA94355C93F304A7AF8FF89AB480E952E9C62DC316A33`.

### C2: citation scope

Rejected as a manuscript defect; retained as a useful request for explicit
wording. The report marked the claims `UNKNOWN` because it did not have the
sources. The project does have and has audited Jiang v1.0.1. Its Theorem 3.2
explicitly assumes a nonempty finite simple graph and says that connectedness
of the second factor is not required. Its Section 5 assumes every join factor
is nonempty and noncomplete, and its closing scope statement explicitly
leaves mixed complete/noncomplete joins unclassified. The fan formula and its
`n >= 4` hypothesis were also rechecked against arXiv v2.

V6 adds the phrase "without a connectedness assumption on G" to prevent the
specific ambiguity raised by the reviewer. No bibliographic or theorem-scope
claim was changed.

### C3: contribution size

Accepted as an editorial risk, not a correctness issue. Whether the structural
classification plus the new tree parameter and linear reconstruction are
substantial enough is for an editor and referees to decide. V6 does not inflate
the novelty claim. It strengthens the mathematical comparison with the weaker
induced-maximum-degree-one problem by giving a tree on which the two optimum
values differ.

## 4. Minor comments

- D1 accepted: internal phrases such as "feasibility stage" and "preserved
  counterexample" were removed from the manuscript.
- D2 accepted: the abstract now uses vertex degrees and numbers of selected
  neighbors instead of undefined DP "labels".
- D3 accepted: Section 7 now states explicitly that the DP-versus-subset route
  shares the formalization of `beta(T)` and tests implementation rather than
  the structural reduction. The new 184-set definition-first check has zero
  failures.
- D4 accepted: the new lock file fixes all installed package versions.
- D5 accepted: the manuscript records `gp_d(F_3)=3`, explaining why the known
  floor formula is restricted to `n >= 4`.
- D6 accepted after independent verification: for the depth-two complete
  binary tree, subset search and the DP both give `beta=4`; the five-vertex
  root-plus-leaves set satisfies the weaker induced-degree condition; and the
  definition-first checker gives `gp_d(K_1+T)=4`.
- D7 accepted: the preliminaries now explain that `|V(T)| >= 3` excludes the
  complete, diameter-one cases `T=K_1,K_2`.

## 5. V6 verification outcome

The immutable v5 source remains 47,256 bytes with SHA-256
`0516949DBC02887615A01E8D3A61E441A19188F0E8342AADA3F23E659DABF2E2`.
The new `drafts/mixed_join_research_note_v6.tex` is 49,825 bytes with SHA-256
`6C8C1812C64FB3B55909A7CFC82383944A93D4C34DBD1423DBC839FA51E0B9FE`.

Static checks found 35 unique labels, 50 resolved `ref/eqref` uses, six
bibliography entries, 13 resolved citation keys, 13 theorem-like statements,
13 proofs, balanced environments, and zero submission placeholders. Pandoc
parsed the source with exit code zero. The test suite returned `30 passed`.

MiKTeX-pdfTeX 4.27 / pdfTeX 1.40.29 compiled v6 successfully through three
passes. The final native log contains no LaTeX/package warnings, overfull or
underfull boxes, undefined references or citations, missing characters,
rerun requests, or errors. The unmodified compiler output is a 14-page A4 PDF;
all fonts are embedded, hyperlinks were enumerated, and all 14 rendered pages
were visually inspected without finding clipping, overlap, broken tables, or
abnormal pagination.

The compiler PDF is 470,046 bytes with SHA-256
`C41FDA75669A253273CF05BC90F0B04DE9020884F982B1E6E56784583919DE44`.
The native log is 27,395 bytes with SHA-256
`7696F4DCF9A5AF6B1F2EC40E0F899CFDA4DEF4ED883A8973FFC05B2007BC13D1`.

## 6. Submission assessment

V6 is a technically complete DMGT-style initial-submission package when the
TeX, PDF, and reproducibility ZIP are submitted together. This means the
source compiles, the proofs and citations have survived the documented audits,
the layout has passed page review, and the computations are locally
reproducible. It does not mean acceptance is assured, novelty is globally
proved, or human peer review has occurred. Before submission, the author must
personally read and approve the theorem, authorship/affiliation, AI disclosure,
declarations, and supplementary-material statement, and must submit the work
to only one journal at a time.
