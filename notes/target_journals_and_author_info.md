# Target journals and author-information checklist

Date checked: 2 September 2026

> **Current route update (2 September 2026).** DMGT rejected v7 at initial
> evaluation without a manuscript-specific reason. The active target is now
> Discrete Applied Mathematics using the new v8 `Contribution` candidate
> derived from frozen v7. The detailed current Guide and upload requirements
> are recorded in `notes/dam_v8_submission_requirements.md`. The older DMGT
> recommendation below is retained as decision history, not as the active
> submission instruction; the obsolete v4 DAM derivative must not be used.

V8 local validation is now complete: bounded literature refresh, static checks,
30 passing tests (one nonfunctional pytest-cache permission warning), three
MiKTeX passes, a clean final native log, and all 22 PDF pages visually checked.
The current validated source/PDF hashes are maintained in
`drafts/TEX_VERSION_HISTORY.md`. This does not replace author approval or the
live submission-system build review, and no DAM submission has been made.

This note records a submission-positioning decision, not an acceptance
prediction. Journal fit is an informed recommendation; scopes and submission
requirements quoted below are facts checked against the linked journal pages.
The manuscript's global novelty and priority remain `UNKNOWN` for the reasons
recorded in `PROJECT_STATUS.md`.

## Recommended submission strategy

Only one journal may consider the manuscript at a time.

### Former primary target: Discussiones Mathematicae Graph Theory (DMGT)

**Recommendation:** best topical fit for the present manuscript and the target
used for the frozen v4--v6 and current v7 first-submission candidates.

Why it fits:

- The paper is a structural graph-theory result about a distance-based vertex
  parameter, graph joins, and trees.
- DMGT's stated scope includes a variety of structural results about graphs.
- DMGT has published work on the standard general-position problem and graph
  operations, so the intended readership already knows the surrounding topic.
- The paper is well below DMGT's requested maximum of 30 journal-style pages.

Current official first-submission requirements relevant to v7:

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
- Author registration: https://www.dmgt.uz.zgora.pl/secure/user/register.php
- Author login: https://www.dmgt.uz.zgora.pl/secure/login.php
- Editorial-office contact: https://www.dmgt.uz.zgora.pl/system_pages/display_page.php?E48D6848C298E50780C6
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

### Current target: Discrete Applied Mathematics

**Recommendation:** current controlled follow-on target. V8 foregrounds the
linear-time computation and reconstruction of a maximum set together with the
structural theorem.

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
This remains a defensible fallback if the controlled DAM attempt is not
successful, but it is not the active target.

Official pages:

- Journal overview: https://link.springer.com/journal/40314
- Directly related product paper:
  https://doi.org/10.1007/s40314-025-03547-7

## Current order

DMGT has completed its initial evaluation and rejected v7 without a
manuscript-specific reason. The active sequence is therefore:

1. obtain author approval of validated v8, then prepare one controlled
   `Contribution` submission to Discrete Applied Mathematics; verify the live
   fields and generated submission PDF before any final submission;
2. if DAM also rejects at initial evaluation, pause direct transfers and audit
   the broader `K_r+G` direction before choosing another journal.

The fit-first sequence is the current recommendation because the manuscript is
a specialized graph-theory paper (22 pages in the current Elsevier preprint
layout), with a proved linear-time algorithm, and global novelty is still
`UNKNOWN`. This is a risk assessment, not a prediction of DAM acceptance.

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
zero submission placeholders, and confirmed author/email fields. These obsolete
v4-derived files remain uncompiled even though a local TeX engine is now
available; no Google Drive file or folder was created, read, or changed for
this work.

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
    The public-repository option is now used in v7. The repository and fixed
    archive were anonymously read back before the statement was added.
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
frozen v4--v6, current v7, and all five v4-derived journal-name files:

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
- V6 preserved the fixed archive `mixed_join_v6_reproducibility.zip` and
  described it as submission supplementary material. V7 instead names the
  public repository and the archive path there, so a separate ZIP upload or
  email to the editorial office is not needed for the stated availability.
- **Verified GitHub release state:** the repository
  `https://github.com/Star5Dust/dual-general-position-mixed-joins` is publicly
  readable on 29 August 2026 and contains the v6 source, PDF, fixed archive,
  code, tests, and audit output. No license or Zenodo DOI has yet been selected.
  The public URL is now included in v7; v6 remains frozen.
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

This metadata completion does not certify the mathematics. The four initial
web-AI attempts and the later GLM 5.3 adversarial report have been adjudicated
in `notes/external_ai_review_adjudication.md` and
`notes/glm_5_3_review_adjudication.md`, but they do not constitute human peer
review. Before submission, the author must personally review and approve the
manuscript.

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

The five v4-derived journal-specific files are superseded format references
and must not be submitted. The compiled v7 ordinary-`article` route is the
current DMGT initial-submission package. Before any submission:

1. personally read and approve v7; if a qualified human review later becomes
   available, preserve and adjudicate it rather than treating the multi-model
   AI screen as equivalent;
2. check on the submission date whether Jiang's v1.0.1 preprint has changed or
   acquired a journal version;
3. reconfirm the filled author metadata, declarations, and AI-use disclosure;
4. DMGT's public guide currently asks for only the line-numbered PDF at first
   submission and requests TeX source after acceptance. Upload v7 PDF only;
   the public GitHub URL in v7 supplies the code and fixed archive, so no ZIP
   attachment or email is needed. Do not upload v7 TeX at first submission
   unless the authenticated form explicitly asks for it;
5. retain DMGT as the working first target unless the author deliberately
   changes it; v7 has already completed real MiKTeX compilation, native-log
   review, and 14-page inspection, but the live journal instructions should
   still be rechecked on the submission date;
6. confirm that the manuscript is not simultaneously under consideration by
   another journal.
