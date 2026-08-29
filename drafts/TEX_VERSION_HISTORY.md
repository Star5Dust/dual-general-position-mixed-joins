# LaTeX version history

Date adopted: 29 August 2026

## Rule

Numbered LaTeX drafts are immutable once a later version is created. Every
layout or content change starts by copying the highest numbered draft to
`mixed_join_research_note_v(N+1).tex`; the older numbered file is retained and
is never overwritten. The matching Google Drive layout uses one folder per
version, `ai4math/vN/`, with the TeX file stored as
`mixed_join_research_note.tex` inside that folder.

The local unnumbered `mixed_join_research_note.tex` is a legacy duplicate of
v2 and is no longer the editing target. Earlier pre-numbering history is
identified by hashes in `PROJECT_STATUS.md`; no missing v1 file is reconstructed
or inferred.

## Recorded versions

| Version | Local source | SHA-256 | Compile/review state |
|---|---|---|---|
| v2 | `drafts/mixed_join_research_note_v2.tex` | `D648DD44CA321475BCA94CBB29C86F22A218738FAE1546C372AAD774F6FAFF1F` | Externally compiled with pdfTeX 1.40.27 / TeX Live 2025. The complete supplied log reports a successful 13-page build and one repeated longtable-width warning; all 13 supplied PDF pages were inspected. |
| v3 | `drafts/mixed_join_research_note_v3.tex` | `35C9D1D4816D3C7B39381FF42F5CCAB7064131870AB2458D256B09DA22FF53A6` | Current compiled/reviewed baseline. The layout-only changes reserve space for two lead-ins and narrow the first reproducibility table. pdfTeX 1.40.27 / TeX Live 2025 produced 13 pages; the supplied complete displayed log contains no error, warning, overfull/underfull box, undefined reference/citation, missing character, or rerun request. All 13 pages passed structural and visual review, including the three v2 regression targets. |
| v4 | `drafts/mixed_join_research_note_v4.tex` | `8E0BBFD7C2436AF9D0396CBA7C1954A47F75A1AEE2861CA933594320716578DF` | Current local DMGT first-submission candidate. It adds one-column line numbering, the verified sole-author metadata and declarations, keywords, 2020 MSC codes, two verified positioning references, and a transparent Codex-use disclosure; it removes the internal-draft banner and rewrites internal `UNKNOWN` markers as publication-facing limitations without resolving the underlying project `UNKNOWN` items. Pandoc and structural checks pass with zero submission placeholders. V4 has not been run through a TeX engine or visually reviewed and is not ready to submit until external human review and the real compile/log/page audit are complete. |

## Journal-name derivatives of v4

The files below are journal-format derivatives, not new mathematical content
versions. Their text from `Introduction` through `Conclusion and limitations`
is byte-for-byte identical to the corresponding v4 span. A future change to a
theorem, proof, computation, citation, or limitation must begin in v5; after
that review-driven revision is approved, the required journal derivative can
be regenerated from v5 instead of editing divergent mathematical copies.

| Target journal | Local source | Bytes | SHA-256 | Format and validation state |
|---|---|---:|---|---|
| Discussiones Mathematicae Graph Theory | `drafts/journal_versions/Discussiones_Mathematicae_Graph_Theory.tex` | 46,222 | `8E0BBFD7C2436AF9D0396CBA7C1954A47F75A1AEE2861CA933594320716578DF` | Exact byte copy of v4; ordinary one-column, line-numbered `article` route for first submission. |
| Graphs and Combinatorics | `drafts/journal_versions/Graphs_and_Combinatorics.tex` | 46,171 | `9C54A63EEF6B101F852ADD65C28090831587BB10484FC6CF48506E75F1E165CF` | Springer `svjour3` with `smallextended`; journal front matter, numeric references, and post-reference declarations. |
| Discrete Mathematics | `drafts/journal_versions/Discrete_Mathematics.tex` | 46,156 | `C3CD01734152F8E7FB32AD105AE6B6924FA391D191BA7D2D97A0603AC947F794` | Elsevier `elsarticle` preprint route with journal front matter and Elsevier-style declarations. |
| Discrete Applied Mathematics | `drafts/journal_versions/Discrete_Applied_Mathematics.tex` | 46,172 | `D215AC66D586E4D0AACA330AD65466EBE5250CA2E3F6F182F1A4E0755803824F` | Elsevier `elsarticle` preprint route with journal front matter and Elsevier-style declarations. |
| Computational and Applied Mathematics | `drafts/journal_versions/Computational_and_Applied_Mathematics.tex` | 46,241 | `A102B5F3BD3BA1EA8CB012339D15E7993AB4E4A7F2D96FBC9DF79C54562B4E4D` | Springer Nature `sn-jnl`, line-numbered `sn-mathphys-ay` author--year route; bibliography alphabetized with author--year labels. |

All five files passed Pandoc parsing and the structural/content-identity scan.
No TeX engine is installed locally, so none of the journal derivatives has a
real compilation, log audit, page count, or visual-review result. The class
dependencies, official instruction links, and exact validation boundary are
recorded in `drafts/journal_versions/README.md`.

## Drive mapping

- v2 folder ID: `1QjW44nhUeXm45qBMRMCBVkJllfNebPjO`; existing TeX file ID:
  `1SVkC2udd2568CXOuzXFYp-23tUrR_M81`.
- v3 folder ID: `1JKUCmJoC7E18skB_FmfbwxtTqG_GvXx_`; new TeX file ID:
  `1A2MepYtCLU80SR9pb011T-lM7iyU2X8M`.
- v4 is intentionally local-only. The user explicitly requested no Google
  Drive operation for the journal-targeting and submission-preparation stage;
  no cloud folder or file was created or updated.
- All five journal-name derivatives are also intentionally local-only. No Drive
  folder or file was created, read, or changed while producing them.

The supplied v2 PDF attachment is 347,353 bytes with SHA-256
`CBAD3BEE3568FEC000847095610D021F7C40F1CDADF6D0CB21818B8E372A649C`,
whereas the supplied log records its pre-delivery `output.pdf` as 343,488
bytes. The attachment header contains `/Linearized 1 /L 347353`, and its
content, metadata, and warning line numbers are consistent with v2. The byte
difference is therefore consistent with post-compile linearization, but
byte-for-byte attachment/log identity is not established.

The supplied v3 PDF attachment is 347,402 bytes with SHA-256
`566A99646FFEA83983445A1F2BEBEE44B122911061304AC4DBCC839A948D2712`.
Its header declares `/Linearized 1 /L 347402`, whereas the displayed log
records the pre-delivery `output.pdf` as 343,570 bytes. The 13-page content,
pdfTeX producer, creation time, 58 named destinations, and v3-specific layout
changes are consistent across the two artifacts, but byte-for-byte identity
is not established. The displayed log was supplied as a 10-page Safari/iOS
PDF printout, 45,700 bytes with SHA-256
`9E1A279A710538140F70403CD50EC921A9A17B91A0B27E26BC8F54589C60CC5D`.
It preserves readable content from the pdfTeX banner through PDF statistics,
but it is not the native plain-text `.log` file and cannot establish the raw
log bytes or the exact TeX-source hash used by the external compiler.
