# Discrete Applied Mathematics v8 submission requirements

Date checked: 2 September 2026

This note records requirements and factual submission inputs for the v8
manuscript. It does not certify acceptance, novelty, or external applicability.
The journal guide is evidence, not an instruction that overrides the project
rules in `AGENTS.md` or `PROJECT_STATUS.md`.

## Official sources checked

- Journal-specific Guide for Authors saved from the official ScienceDirect
  page on 2 September 2026:
  `Guide for authors - Discrete Applied Mathematics - ISSN 0166-218X _ ScienceDirect.com by Elsevier.pdf`.
  The 17-page PDF is 539,209 bytes with SHA-256
  `FD626863EFD3F53EED8850395555A2307E00E88F183ED6673B2F226499AC9E64`.
- Official journal description:
  https://shop.elsevier.com/journals/discrete-applied-mathematics/0166-218X
- Official DAM Editorial Manager entry:
  https://www.editorialmanager.com/dam/default.aspx
- Elsevier generative-AI policy for journals:
  https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals
- Elsevier Editorial Manager submission overview:
  https://www.elsevier.support/publishing/answer/how-do-i-submit-a-manuscript-in-editorial-manager
- Elsevier LaTeX submission support:
  https://www.elsevier.support/publishing/answer/how-to-submit-a-latex-file-in-editorial-manager
- Elsevier cover-letter guidance:
  https://www.elsevier.support/publishing/answer/what-should-be-included-in-a-cover-letter

The live ScienceDirect guide page returned a CAPTCHA to the automated browser.
The user-supplied PDF is a same-day print of that exact official page and makes
the journal-specific text available without inferring missing requirements.

## Journal-specific requirements relevant to v8

- Scope: algorithmic and applicable discrete mathematics, including research
  papers and short notes. The manuscript's fit is its exact linear-time
  dynamic program and maximum-set reconstruction. It remains primarily a
  structural graph-theory paper and must not claim an unproved external
  application.
- Article type: **Contribution**, defined by the guide as a full-length
  original research article of more than 10 pages. A Note is limited to 10
  pages or fewer. The frozen v7 compiled to 14 pages, so Contribution is the
  correct working type for v8.
- Review model: single anonymized. Author names, affiliation, corresponding
  author, and email therefore remain in the manuscript title page.
- File format: retain the editable `.tex` and build dependencies; a PDF is
  not an editable source. The guide says relevant editable source files will
  be requested upon submission or revision. The authenticated DAM Attach Files
  screenshot supplied on 2 September 2026 resolves the initial-upload route:
  LaTeX authors first upload a compiled PDF as item type `Manuscript`; source
  files are requested at revision. Thus the first file is the validated v8
  PDF, not the TeX or a source ZIP. This corrects the earlier source-first
  interpretation; it does not remove the need to retain editable sources.
- Title page: concise title; accurately spelled author names; affiliation with
  country; one clearly identified corresponding author; corresponding email.
- Abstract: concise, factual, self-contained, no more than 250 words, normally
  without references or uncommon undefined abbreviations.
- Keywords: 1--7 English keywords. Avoid unnecessarily long phrases and use
  abbreviations only when established.
- Highlights: encouraged, not stated as mandatory. If supplied, upload a
  separate editable file whose filename contains `highlights`, with 3--5
  bullets of at most 85 characters each.
- Competing interests: the online declarations tool must always be completed.
  With nothing to declare, select `I have nothing to declare`; upload the
  resulting unsigned `.doc` or `.docx` during the attach/upload-files step.
- Funding: with no funding, the guide recommends the sentence now used in v8:
  `This research did not receive any specific grant from funding agencies in
  the public, commercial, or not-for-profit sectors.`
- Generative AI: include a separate section immediately before the references
  titled `Declaration of generative AI and AI-assisted technologies in the
  manuscript preparation process`. Name the tool, state its purpose, describe
  human review/editing, and accept responsibility. AI tools cannot be authors.
  V8 also records Codex-assisted code development in the computational-method
  section because the current Elsevier policy separately asks for research-code
  use to be described with the methods.
- Research data: DAM applies Elsevier research-data Option C. Deposit, cite, and
  link the supporting materials in a relevant repository, or explain why they
  cannot be shared. V8 links the public repository containing code, tests,
  locked environment, proof note, fixed archive, and machine-readable outputs.
- Supplementary material: optional, but any supplement must be cited, described,
  and supplied at initial submission; it is posted as received. V8 instead uses
  the already public repository and fixed archive unless the authenticated form
  or editor asks for a separate supplement.
- References: no strict reference formatting is imposed at initial submission
  if the presentation is complete and consistent. The guide's production style
  uses square-bracket numbers with an alphabetically arranged list. Preprints
  must be marked clearly and include the preprint server or the word `preprint`
  and the DOI.
- Submission declaration: the work must not be under consideration elsewhere;
  prior preprint-style sharing is allowed. The public project manuscript is
  disclosed in the cover-letter draft. The completed DMGT submission is no
  longer under consideration.

## Upload and metadata fields

The journal guide and the official DAM Editorial Manager public entry confirm
the journal and workflow. The official Elsevier EM documentation shows the
following sequence; exact labels or optional fields may vary with the live DAM
configuration after the article type is selected.

1. Select article type `Contribution`.
2. At the first-file screen, upload
   `output/pdf/mixed_join_research_note_v8.pdf` as `Manuscript` (22 pages,
   438,048 bytes). The authenticated screen explicitly directs LaTeX authors
   to upload a compiled PDF and says source files will be requested at
   revision. Retain `drafts/mixed_join_research_note_v8.tex` and required
   class/package files for that stage; do not upload a whole-project ZIP.
3. Attach the declarations-tool `.doc/.docx` as the configured declaration or
   conflict-of-interest item.
4. If used, attach
   `drafts/mixed_join_research_note_v8_highlights.txt` in an accepted editable
   format under the Highlights item. Convert it to `.docx` if the live item
   restricts file extensions.
5. Provide the public repository link when the system prompts for research
   data or an external resource. The authenticated data/code availability
   dropdown supplied by the author on 2 September 2026 offers no dedicated
   public-repository option. Select `Other` and explain:

   ```text
   The source code, tests, and machine-readable computational results supporting this study are publicly available at https://github.com/Star5Dust/dual-general-position-mixed-joins.
   ```

   The screen warns that this explanation will be published verbatim. Do not
   select `No data was used` for a manuscript reporting computational outputs,
   or `available on request` when the materials are already public. Do not copy
   the option's example claim that a link was supplied at Attach Files unless
   that action has actually been verified. The public repository page was
   rechecked and lists `src`, `tests`, `experiments`, and `results`.
6. Complete journal-configured general information, classifications, review
   preferences, additional questions, and comments. Suggested/opposed reviewers
   and an editor request are configuration-dependent and must not be invented.
7. Verify or enter the manuscript title, abstract, keywords, sole author and
   corresponding-author details, and no-funding information.
8. Build/assemble the system's submission PDF, inspect it, and approve only
   after the uploaded manuscript, attached items and metadata appear correctly.
   A locally validated manuscript does not by itself verify the assembled
   submission PDF.

The DAM Guide for Authors does not state that a cover letter or graphical
abstract is mandatory. The concise optional cover-letter draft is stored at
`drafts/mixed_join_research_note_v8_cover_letter.md`; use it only if the live
form provides or requires a cover-letter field. The guide encourages, rather
than requires, highlights.

## Cover-letter facts

- Target and type: Discrete Applied Mathematics, Contribution.
- Aim: determine the dual general-position number of `K_r+T` and construct a
  maximum set.
- Main result: exhaustive two-branch classification and exact formula.
- Algorithmic result: four-state rooted-tree DP; value and reconstruction in
  linear time and space, with the full mixed-join set constructed in
  `O(r+|V(T)|)` time.
- Fit: exact algorithmic discrete mathematics backed by structural proofs.
- Honest boundary: no external application claim; fan graphs are a prior
  subfamily; Jiang's closest complete-first-factor result is a preprint;
  bounded computations test implementations but are not proofs.
- Availability: public GitHub repository and a fixed reproducibility archive.
- Submission status: not under consideration elsewhere.
- Public history: an earlier manuscript version is available in the repository;
  it has not been peer reviewed or formally published.

Funding, competing-interest declarations, AI disclosure, and reviewer
suggestions are intentionally not placed in the cover letter, following
Elsevier's general cover-letter guidance; they are supplied in their proper
manuscript or submission-system locations.
