# Internal review package manifest

Date: 29 August 2026
Scope: mixed join `K_r+T`, `r>=1`, and trees `T` of order at least three

This manifest identifies the stable files needed to review and reproduce the
current internal research note. It does not create an archive, copy files, or
make a novelty or priority claim. Byte counts are filesystem lengths and all
digests are SHA-256, computed on the files as stored in this workspace.

## Current verification status

- The Markdown manuscript and latest v3 LaTeX manuscript preserve 13 numbered
  statements, 13 proofs, 40 display formulas, all computational totals, five
  artifact hashes, and five `UNKNOWN` statements. Pandoc 2.12 parsed v3
  successfully. Static checks found 35 unique labels, 46 resolved
  `ref`/`eqref` uses, 11 resolved citation uses, four bibliography entries, and
  a correctly nested environment stack.
- The most recent test run returned `29 passed in 0.44s`; pytest also reported
  one non-mathematical cache-write warning because `.pytest_cache` was not
  writable in this session.
- The archived mixed-join audit contains 985 DP/subset comparisons, 11,003
  root-invariance comparisons, 985 reconstruction checks, and 184
  formula/definition comparisons, with zero failures in every category.
- The frozen v2 baseline compiled to 13 pages. Its displayed log had no error,
  undefined reference/citation, underfull box, missing character, or rerun
  request, but reported one 2.68097-point longtable-width overfull for each of
  the two alignment chunks. Visual review also found two low-severity lead-in
  breaks. Those three items are the complete target list for v3.
- V3 compiled externally with pdfTeX 1.40.27 / TeX Live 2025 to 13 A4 pages.
  The complete displayed log contains no TeX/LaTeX error, warning,
  overfull/underfull box, undefined reference/citation, missing character, or
  rerun request. All 13 pages were rendered and inspected; the two lead-ins
  now remain with their formula/table, the first reproducibility table is
  inside the text area, and no clipping, overlap, black box, missing glyph,
  unresolved `??`, orphan heading, or new layout regression was found.
- The v3 PDF has 22 font resources, all embedded, subsetted, and
  Unicode-mapped. All 57 internal links resolve, six URI links are
  structurally valid, all 58 named destinations resolve, and all 16 bookmarks
  point to valid pages. Text-coordinate checks found no character outside the
  page boxes.
- The v3 attachment is 347,402 bytes with SHA-256
  `566A99646FFEA83983445A1F2BEBEE44B122911061304AC4DBCC839A948D2712`
  and declares `/Linearized 1 /L 347402`; the displayed log records the
  pre-delivery `output.pdf` as 343,570 bytes. The content, metadata, and
  v3-specific pagination are consistent, but byte-for-byte attachment/log
  identity is not established. The complete displayed log arrived as a
  10-page Safari/iOS PDF printout, 45,700 bytes with SHA-256
  `9E1A279A710538140F70403CD50EC921A9A17B91A0B27E26BC8F54589C60CC5D`,
  rather than as the native plain-text `.log`; exact raw-log and source-hash
  provenance therefore remain unavailable.

## Core review files

| Path | Bytes | SHA-256 |
|---|---:|---|
| `README.md` | 2,979 | `D3EDB568B7E0443BE00B4F8B7B1D5DF308FFC3CCA966FBDE8B894EDC4DBC446C` |
| `notes/collaborator_reading_guide.md` | 10,414 | `E47F0B6DEE0256E0741491E8070BF2B8F8F5D9183ED2D03A63F8F249BCA23F7A` |
| `drafts/mixed_join_research_note_v3.tex` | 44,087 | `35C9D1D4816D3C7B39381FF42F5CCAB7064131870AB2458D256B09DA22FF53A6` |
| `drafts/mixed_join_research_note_v2.tex` | 43,773 | `D648DD44CA321475BCA94CBB29C86F22A218738FAE1546C372AAD774F6FAFF1F` |
| `drafts/TEX_VERSION_HISTORY.md` | 7,571 | `804B06E73CA6F13AC65FB1DB7FD90B71C472FA2693B719904F8C2F4F86AF93C0` |
| `drafts/mixed_join_research_note.md` | 36,960 | `9A76A7E8E6AE9BD0505224234C5BEF6379F713B4753D11FB11F5AEEA03E531A7` |
| `proofs/mixed_join_tree.md` | 10,400 | `65D23FAD3BA238FC068AD97963C1E136C8E5DD5C9DAEC29B76F84FC9A3D06409` |
| `notes/mixed_join_literature_positioning.md` | 19,931 | `0C1224F133C40ED22FC7BE828575D683384602233DEB8183CD9000D558A53D97` |

Recommended reading order is the collaborator guide, dynamic v5 candidate and
AI-review adjudication, v3 LaTeX manuscript and its reviewed compiled
artifacts, v2 warning-bearing baseline, Markdown manuscript, version history,
proof-development note, and literature-positioning note. V3 is the latest
compiled submission-style draft; v2 is retained unchanged for provenance, and
the Markdown file is an earlier readable source with the same main theorem.

The frozen AI-reviewed source `drafts/mixed_join_research_note_v4.tex`, the
adjudicated candidate `drafts/mixed_join_research_note_v5.tex`, its review
adjudication note, the five
journal-name derivatives under `drafts/journal_versions/`, and
`notes/target_journals_and_author_info.md` are submission-preparation files,
not replacements for this compiled v3 review baseline. V4 and the derivatives
contain the verified sole-author metadata and declarations and zero submission
placeholders. V5 contains only adjudicated minor precision changes and has
passed static checks, but it has not been compiled or visually reviewed. These
files are therefore listed with the mutable handoff files below rather than
added to the stable review-package digest table.

## Reproducibility dependency closure

| Path | Bytes | SHA-256 |
|---|---:|---|
| `requirements.txt` | 54 | `74BBC0D1430A450DF9DAB292A76970B01A9CDB84922E419BA24FF26704F12E9B` |
| `src/__init__.py` | 75 | `ED1639318E17C6FF6C2B89761E68E2304314B2081B7A4F674C85D46BF40F19F0` |
| `src/mixed_join_tree.py` | 8,514 | `D3DDAB46510B217BF9C442CC57302953C4D0C29F208DD7ADE06381F2D90A8B9D` |
| `src/dual_gp_independent.py` | 9,021 | `D7BA1C520DC6991E78CB8BAE609A598E6BBF950DA03C1EAC9BA4D30D1EFFF231` |
| `experiments/audit_mixed_join_dp.py` | 6,465 | `93BA42DB963CAB3F2EE34DAC9CF36511FF6332A84543F44A22ACD48BBB974D44` |
| `experiments/audit_extension_candidates.py` | 9,291 | `A463CE202995000F324BDB7F90D2821B1B97AB38911E3E8941DFFC381F8393F6` |
| `results/mixed_join_dp_audit.json` | 2,881 | `C4489D2A7202AD1413EED2FBC551E6CBDFEB6FC5BB10FF32F4899B747C3F4E90` |
| `tests/test_dual_gp_independent.py` | 3,306 | `DC838B029F97760FD67006CF582ECB205AE22AEE7F492CE1A5065680A6BA1674` |
| `tests/test_extension_feasibility.py` | 1,705 | `58EFBF1D99269B8081CA1F3A41FF212254AB46FE8132781299BEA82DEF5D9D80` |
| `tests/test_mixed_join_tree.py` | 2,984 | `D48F5F0972A3B28D8D9FA58C095E5707D5A5CB5F5C3A8D1E8B51ED61AB3CC447` |

The main audit directly imports `src/mixed_join_tree.py`,
`src/dual_gp_independent.py`, and three graph/search helpers from
`experiments/audit_extension_candidates.py`. The test suite imports the same
modules. NetworkX is required for tree enumeration and pytest is required for
the tests. `requirements.txt` records the broader project environment; the
freshly checked versions were CPython 3.13.5, NetworkX 3.6.1, and pytest 9.1.1.
The requirements file does not pin versions. A run under different Python or
NetworkX versions can reproduce the logical counts while producing a
byte-different JSON file because the report embeds environment versions; a
JSON hash difference alone is therefore not a mathematical failure.

The two verification routes use different checking logic, but they share the
audit driver and NetworkX-generated tree samples. They are not two completely
disjoint software stacks. The JSON report is generated output, not an input to
the theorem or DP.

## Optional historical provenance

| Path | Bytes | SHA-256 |
|---|---:|---|
| `notes/extension_feasibility_audit.md` | 12,536 | `4653E46C27937D1411110A180D30BEC02A9D482CA1E44FC065E9E70E3B61305E` |
| `results/extension_feasibility_audit.json` | 1,730 | `271FC505E7F21761CA652059E42B5B6FEAE8FF98A3ECD00C4F62B56125B0E950` |
| `notes/literature_notes.md` | 38,212 | `BC7632DDC395D7E4C1BD0E41E6B8ED2456A57FD3A1E19E77C7D8BE3F00533B32` |

The first two files are needed only to trace target selection, the earlier 92
mixed-join comparisons, the 17 dormant path-first cases, and the provenance of
the retained `K_{1,3}` counterexample. They are not added to the main audit
totals because the 92 mixed-join cases overlap the larger matrix.
The literature notes preserve the earlier citation-chain audit referenced by
the current positioning note; they are not required to check the theorem or
rerun the computation. The formerly recorded
`notes/literature_search_log.md` is not present in this workspace, and its
recovery remains `UNKNOWN`; it is not silently represented as included.

The earlier complete-first-factor/Jiang audit, its reports, and locally cached
third-party papers are also outside this minimum mixed-join package. The
ignored `papers_local/` directory must not be treated as a distributable
artifact without a separate rights and provenance check.

## Dynamic handoff files intentionally not hashed

- `PROJECT_STATUS.md`;
- `notes/research_log.md`;
- `drafts/mixed_join_research_note_v4.tex`;
- `drafts/mixed_join_research_note_v5.tex`;
- `notes/external_ai_review_adjudication.md`;
- `drafts/journal_versions/README.md`;
- `drafts/journal_versions/Discussiones_Mathematicae_Graph_Theory.tex`;
- `drafts/journal_versions/Graphs_and_Combinatorics.tex`;
- `drafts/journal_versions/Discrete_Mathematics.tex`;
- `drafts/journal_versions/Discrete_Applied_Mathematics.tex`;
- `drafts/journal_versions/Computational_and_Applied_Mathematics.tex`;
- `notes/target_journals_and_author_info.md`;
- `notes/review_package_manifest.md` (this file).

These files remain part of a complete internal handoff, but status and log are
updated when each stage closes, v5 may be superseded after later review and
typesetting validation, and hashing the
manifest inside itself would be self-referential. The target-journal note and
journal-version index are paired with that mutable submission workflow rather
than the compiled v3 package. Their omission from the digest tables is
intentional, not a missing dependency.

## Verified commands

From the repository root in PowerShell:

```powershell
.\.venv\Scripts\python.exe -m pytest -q .\tests
.\.venv\Scripts\python.exe .\experiments\audit_mixed_join_dp.py --output .\results\mixed_join_dp_audit.json
& 'E:\Anaconda\Scripts\pandoc.exe' .\drafts\mixed_join_research_note_v3.tex --from=latex --to=native | Out-Null
Get-ChildItem .\drafts\journal_versions\*.tex | ForEach-Object { & 'E:\Anaconda\Scripts\pandoc.exe' $_.FullName --from=latex --to=native | Out-Null; if ($LASTEXITCODE -ne 0) { throw "Pandoc failed: $($_.Name)" } }
```

The first command most recently returned 29 passing tests and the cache-write
warning recorded above. The second command
most recently reproduced all four zero-failure audit categories; it overwrites
the canonical JSON path, so a reviewer who wants to preserve the archived file
should provide a different `--output` path and compare the two JSON objects.
The third command returned exit code zero and is only a Pandoc reader/static
syntax check.

The v3 PDF, complete displayed log, and all 13 rendered pages have now been
checked. The typesetting stage is complete with no remaining warning or visual
defect. The native plain-text `.log` was not supplied, so the printable log
content is verified but its original bytes are not archived here. No TeX
engine was installed in this workspace. Four independent web-AI review
attempts of frozen v4 have been adjudicated: one was a detailed proof audit,
one contained a rejected false critical objection, one was editorial only,
and one did not receive the manuscript. V5 incorporates the supported minor
corrections. This is not human peer review. V5 still needs a real
compile/log/page audit; after content approval, only the selected journal
derivative should be regenerated. Any later content revision must start v6
rather than overwrite the preserved v3, v4, or v5 files.

## Claim boundary

The proof and computation status above is internal. Jiang's future publication
status, the exact fan formula in the version-of-record body, an established
equivalent name or simpler closed form for `beta(T)`, subscription-index
coverage, global novelty/priority, final publishability/journal placement, and
the out-of-scope graph directions remain `UNKNOWN` as recorded in
`PROJECT_STATUS.md`. This manifest changes none of those statuses.
