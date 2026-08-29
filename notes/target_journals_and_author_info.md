# Target journals and author-information checklist

Date checked: 29 August 2026

This note records a submission-positioning decision, not an acceptance
prediction. Journal fit is an informed recommendation; scopes and submission
requirements quoted below are facts checked against the linked journal pages.
The manuscript's global novelty and priority remain `UNKNOWN` for the reasons
recorded in `PROJECT_STATUS.md`.

## Recommended submission strategy

Only one journal may consider the manuscript at a time.

### Primary target: Discussiones Mathematicae Graph Theory (DMGT)

**Recommendation:** best topical fit for the present manuscript and the target
used for the local v4 first-submission candidate.

Why it fits:

- The paper is a structural graph-theory result about a distance-based vertex
  parameter, graph joins, and trees.
- DMGT's stated scope includes a variety of structural results about graphs.
- DMGT has published work on the standard general-position problem and graph
  operations, so the intended readership already knows the surrounding topic.
- The paper is well below DMGT's requested maximum of 30 journal-style pages.

Current official first-submission requirements relevant to v4:

- no submission fee or APC;
- English used consistently;
- abstract, keywords, and 2020 Mathematics Subject Classification;
- corresponding author's name, affiliation, and email;
- PDF no larger than 10 MB;
- first submission may use an ordinary LaTeX class, but it must be one-column
  and line-numbered;
- the `dmgt` class becomes mandatory after acceptance, not at first submission;
- ORCID completion is recommended for the corresponding author and coauthors.

Official pages:

- Scope: https://www.dmgt.uz.zgora.pl/
- Guide for authors: https://www.dmgt.uz.zgora.pl/system_pages/guide.php
- Closely related standard-general-position paper:
  https://www.dmgt.uz.zgora.pl/publish/article.php?doi=2269

### Stretch alternative: Graphs and Combinatorics

**Recommendation:** consider before DMGT only if an external graph theorist
judges the structural theorem and the new tree optimization parameter to be a
sufficiently broad advance.

The official scope explicitly includes structural graph theory and
combinatorial optimization and algorithms. That matches the theorem-plus-DP
combination. The main risk is not scope but contribution level: the current
result concerns one mixed-join family, and the full novelty audit is not yet
closed.

Official journal page and scope:
https://link.springer.com/journal/373

### Stretch alternative: Discrete Mathematics

**Recommendation:** a plausible pure-combinatorics target if human review
confirms that the classification is significant beyond the immediate dual
general-position literature.

The official scope includes graph theory and graph operations and accepts both
Contributions and shorter Notes. The paper is proof-led rather than primarily
experimental, which is consistent with the journal's stated scope. The risk is
again significance and breadth, not subject mismatch.

Official journal description:
https://shop.elsevier.com/journals/discrete-mathematics/0012-365X

### Algorithm-oriented alternative: Discrete Applied Mathematics

**Recommendation:** use if the linear-time computation and reconstruction of
the maximum set are foregrounded together with the structural theorem.

The journal's stated remit is algorithmic and applicable discrete mathematics.
It published the directly related 2026 paper on dual general position under
vertex and edge removal. The current manuscript has a genuine linear-time
algorithm, but it remains more structural than applied; the cover letter would
need to explain the algorithmic contribution clearly.

Official pages:

- Journal description:
  https://shop.elsevier.com/journals/discrete-applied-mathematics/0166-218X
- Directly related 2026 article:
  https://doi.org/10.1016/j.dam.2026.02.044

### Additional fallback: Computational and Applied Mathematics

The journal explicitly includes discrete mathematics and asks for mathematical
depth, methodological rigor, and computational relevance. It published the
2026 product paper that posed the surrounding complete-first-factor problem.
This is a defensible fallback, but DMGT has the cleaner audience match for the
present all-tree structural classification.

Official pages:

- Journal overview: https://link.springer.com/journal/40314
- Directly related product paper:
  https://doi.org/10.1007/s40314-025-03547-7

## Recommended order

Two reasonable, mutually exclusive strategies are:

1. **Fit-first:** DMGT, then Discrete Applied Mathematics, then Computational
   and Applied Mathematics.
2. **Stretch-first:** Graphs and Combinatorics or Discrete Mathematics, then
   DMGT.

The fit-first sequence is the current recommendation because the manuscript is
a specialized 13-page graph-theory paper and global novelty is still
`UNKNOWN`. This is a risk assessment, not a statement that DMGT will accept the
paper.

## Local journal-specific TeX candidates

Five local-only files were prepared on 29 August 2026 under
`drafts/journal_versions/`, using the full journal name as the filename. The
DMGT file is an exact byte copy of v4. For the other four files, the preamble,
front matter, declarations placement, and required reference presentation were
adapted, while the entire text from `Introduction` through `Conclusion and
limitations` remains byte-for-byte identical to v4.

| Target | Local file | Official submission-format route used |
|---|---|---|
| Discussiones Mathematicae Graph Theory | `Discussiones_Mathematicae_Graph_Theory.tex` | Ordinary one-column, line-numbered `article` for first submission; `dmgt` is reserved for the acceptance stage. |
| Graphs and Combinatorics | `Graphs_and_Combinatorics.tex` | Springer `svjour3` with `smallextended`; 150--250-word abstract, five keywords, 2020 MSC, and numeric references. |
| Discrete Mathematics | `Discrete_Mathematics.tex` | Elsevier `elsarticle` in readable preprint mode with journal front matter, numeric references, and Elsevier-style declarations. |
| Discrete Applied Mathematics | `Discrete_Applied_Mathematics.tex` | Elsevier `elsarticle` in readable preprint mode with journal front matter, numeric references, and Elsevier-style declarations. |
| Computational and Applied Mathematics | `Computational_and_Applied_Mathematics.tex` | Springer Nature `sn-jnl` with line numbers and the journal-requested `sn-mathphys-ay` author--year route; 150--250-word abstract, five keywords, and 2020 MSC. |

The Springer requirements were checked against the two official journal
submission-guideline pages and the official Springer Nature LaTeX support
package. Elsevier's journal pages were used for scope, while the two Elsevier
files follow the publisher's first-submission flexibility and official
`elsarticle` authoring route. Exact hashes, class dependencies, and source
links are recorded in `drafts/journal_versions/README.md` and
`drafts/TEX_VERSION_HISTORY.md`.

All five files passed Pandoc parsing and a common static scan: 35 unique
labels, 47 resolved cross-references, six bibliography entries, 13 resolved
cite commands, balanced environments, 13 theorem-like statements, 13 proofs,
zero submission placeholders, and confirmed author/email fields. They have not
been compiled because no TeX engine is installed locally. No Google Drive file
or folder was created, read, or changed for this work.

## Information needed from the author(s)

Do not infer or invent any item below. A collaborator who only reviews the
paper is normally acknowledged, not automatically made a coauthor.

### Information required for the title page

For every author:

1. Full publishing name in Roman letters, with the exact spelling,
   capitalization, initials, and order to use in bibliographic databases.
2. Final author order.
3. Affiliation where the work was carried out:
   department or school, university or institution, city, postal code, and
   country. If no institutional affiliation is appropriate, explicitly choose
   an honest independent-researcher affiliation and location instead of
   borrowing an institution's name.
4. Email address. Identify the corresponding author and remember that the
   corresponding email will normally become public.
5. ORCID iD in the form `0000-0000-0000-0000`, if one exists. DMGT recommends
   completing ORCID information; it is not fabricated when absent.

### Needed for declarations and the submission system

6. Funding source and grant number, or an explicit confirmation that there was
   no funding.
7. Any competing interest, or an explicit confirmation that none exists.
8. Each author's actual contribution and confirmation that every listed author
   approves the final manuscript and accepts responsibility for it.
9. Acknowledgements, including the name and consent of any person to be thanked.
10. Code/data availability choice:
    - public repository plus persistent URL/DOI;
    - files supplied as journal supplementary material; or
    - availability from the corresponding author on reasonable request.
    The current project is local-only, so no public-repository statement may be
    inserted until the author deliberately chooses and performs that release.
11. The accurate disclosure of AI-assisted tools required by the selected
    journal. AI tools cannot be authors; the human author(s) must personally
    verify and take responsibility for the mathematics, text, citations, and
    code.
12. Whether any version has been posted as a preprint, submitted elsewhere, or
    included in a thesis or conference proceeding. Give links or identifiers if
    applicable.
13. Optional cover-letter information: suggested handling area/editor,
    genuinely qualified reviewer suggestions if requested by the submission
    system, and people who should be excluded for a concrete conflict of
    interest. Do not suggest reviewers merely to improve acceptance odds.

## Author response recorded on 29 August 2026

The following information and working decisions have now been applied to the
local v4 candidate and all five journal-name derivatives:

- Sole author and corresponding author: **Yi Yuteng**. The Chinese name
  `易宇腾` is retained in this internal note but is not added to the English
  title page.
- Public corresponding email: `yiyuteng29@163.com`.
- Current affiliation: **Independent Researcher, Shanghai, China**.
- No ORCID was reported.
- No funding or competing interests were reported.
- No human acknowledgement was requested. Acknowledgements are not arbitrary:
  they must describe genuine assistance, and a named person should normally
  consent to being identified.
- Because the project remains local-only, the working availability statement
  is that the code and machine-readable audit outputs are available from the
  corresponding author on reasonable request. No public repository is claimed.
- **Deferred GitHub release item:** the linked GitHub identity was verified as
  `Star5Dust`, but the current GitHub App installation exposes no installed
  account or accessible repository, and the local computer has no `gh` CLI.
  No repository was created and no file was uploaded. When the author is back
  at the computer, create an empty private repository under `Star5Dust`, grant
  the Codex GitHub integration access to that repository, and then decide the
  curated file set, public/private visibility, license, and whether to archive
  a release on Zenodo for a DOI. The manuscript must retain the
  availability-on-request statement until a public URL has actually been
  created and verified.
- OpenAI Codex is acknowledged as an AI-assisted tool, not as an author. The
  disclosure lists its actual roles in literature organization, proof drafting,
  code development, computational checking, manuscript drafting, and editorial
  revision, while assigning responsibility for the final manuscript to the
  human author. This follows the transparency and human-responsibility principle
  in OpenAI's sharing and publication policy:
  https://openai.com/policies/sharing-publication-policy/

The author reported recent graduation from 上海交通大学浦江国际学院. The
college's official site currently gives the English name **SJTU Global
College**:
https://gc.sjtu.edu.cn/cn/admission/undergraduate-admission/overview/.
This educational history is not used as a present affiliation because the
author has graduated and reported no current institutional position. It may be
added later only if the author confirms that the work was carried out there and
that listing the institution is accurate and appropriate.

This metadata completion does not certify the mathematics. Before submission,
the author must personally review and approve the manuscript, and the external
human mathematical and literature review remains an open gate.

## Metadata already selected in v4 and its journal derivatives

The following fields do not require personal information and were added to the
local v4 candidate:

- Keywords: dual general position; graph join; tree; graph convexity; dynamic
  programming.
- 2020 MSC primary: `05C12` (distance in graphs).
- 2020 MSC secondary: `05C05` (trees), `05C69` (special vertex subsets),
  `05C76` (graph operations), and `05C85` (graph algorithms).

The official MSC descriptions are in:
https://msc2020.org/MSC_2020.pdf

## Submission gates still open

The five journal-specific files are candidates, not ready-to-upload final
manuscripts. Before any submission:

1. obtain the external human mathematical and literature review already listed
   as the next scientific gate in `PROJECT_STATUS.md`;
2. check on the submission date whether Jiang's v1.0.1 preprint has changed or
   acquired a journal version;
3. reconfirm the filled author metadata, declarations, and AI-use disclosure;
4. reconfirm the availability-on-request policy or deliberately replace it
   with a public repository or journal-supplement statement;
5. select exactly one target, obtain its current official class package, then
   run a real LaTeX compilation, complete log review, and page-by-page PDF
   inspection on that journal-specific file;
6. confirm that the manuscript is not simultaneously under consideration by
   another journal.
