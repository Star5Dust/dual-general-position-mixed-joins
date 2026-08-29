# Local journal-specific LaTeX candidates

Date prepared: 29 August 2026

These five local-only files are submission-format derivatives of
`drafts/mixed_join_research_note_v4.tex`. In every file, the text from
`Introduction` through `Conclusion and limitations` is byte-for-byte identical
to the frozen v4 body. Only the preamble, front matter, declarations placement,
and (where required) bibliography presentation differ. No Google Drive file was
created or changed.

| Target journal | TeX file | Submission route | SHA-256 |
|---|---|---|---|
| Discussiones Mathematicae Graph Theory | `Discussiones_Mathematicae_Graph_Theory.tex` | Ordinary one-column, line-numbered `article` file for first submission; exact byte copy of v4 | `8E0BBFD7C2436AF9D0396CBA7C1954A47F75A1AEE2861CA933594320716578DF` |
| Graphs and Combinatorics | `Graphs_and_Combinatorics.tex` | Springer `svjour3`, `smallextended`, numeric references | `9C54A63EEF6B101F852ADD65C28090831587BB10484FC6CF48506E75F1E165CF` |
| Discrete Mathematics | `Discrete_Mathematics.tex` | Elsevier `elsarticle`, readable preprint layout, numeric references | `C3CD01734152F8E7FB32AD105AE6B6924FA391D191BA7D2D97A0603AC947F794` |
| Discrete Applied Mathematics | `Discrete_Applied_Mathematics.tex` | Elsevier `elsarticle`, readable preprint layout, numeric references | `D215AC66D586E4D0AACA330AD65466EBE5250CA2E3F6F182F1A4E0755803824F` |
| Computational and Applied Mathematics | `Computational_and_Applied_Mathematics.tex` | Springer Nature `sn-jnl`, line-numbered `sn-mathphys-ay` author--year route | `A102B5F3BD3BA1EA8CB012339D15E7993AB4E4A7F2D96FBC9DF79C54562B4E4D` |

## Required official class packages

- DMGT first submission uses the standard `article` class. The journal's
  `dmgt` class is an acceptance-stage requirement, not the current route.
- Graphs and Combinatorics requires Springer's official `svjour3.cls` and
  `svglov3.clo` files with the `smallextended` option.
- The two Elsevier files require the official `elsarticle.cls` package.
- Computational and Applied Mathematics requires the complete official
  Springer Nature `sn-jnl` authoring package. The manuscript uses an inline
  bibliography, so it does not depend on a project `.bib` file.

Official instructions checked for this conversion:

- DMGT guide: https://www.dmgt.uz.zgora.pl/system_pages/guide.php
- Graphs and Combinatorics submission guidelines:
  https://link.springer.com/journal/373/submission-guidelines
- Discrete Mathematics journal page:
  https://shop.elsevier.com/journals/discrete-mathematics/0012-365X
- Discrete Applied Mathematics journal page:
  https://shop.elsevier.com/journals/discrete-applied-mathematics/0166-218X
- Computational and Applied Mathematics submission guidelines:
  https://link.springer.com/journal/40314/submission-guidelines
- Springer Nature LaTeX support and templates:
  https://www.springernature.com/gp/authors/campaigns/latex-author-support

## Validation boundary

Pandoc parsed all five TeX files successfully. Static checks found, in each
file, 35 unique labels, 47 resolved `ref`/`eqref` uses, six bibliography
entries, 13 resolved citation commands, balanced environments, 13 theorem-like
statements, 13 proofs, zero submission placeholders, and the confirmed author
name and email. The DMGT alias has the same SHA-256 as v4, and v3/v4 remain
unchanged.

No TeX engine is installed in this workspace, so none of these five derivative
files has yet received a real compile, complete log review, or page-by-page PDF
inspection. They also still require the external human mathematical,
literature, and submission review recorded in `PROJECT_STATUS.md`. Submit only
one version to one journal at a time, and recheck the selected journal's live
instructions immediately before submission.
