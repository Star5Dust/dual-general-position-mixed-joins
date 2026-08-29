# Internal review package manifest

Date: 29 August 2026
Scope: mixed join `K_r+T`, `r>=1`, and trees `T` of order at least three

This manifest identifies the stable files needed to review and reproduce the
current internal research note. It does not create an archive, copy files, or
make a novelty or priority claim. Byte counts are filesystem lengths and all
digests are SHA-256, computed on the files as stored in this workspace.

## Current verification status

- V6 is the current DMGT-style initial-submission candidate. Pandoc parsed it
  successfully. Static checks found 35 unique labels, 50 resolved
  `ref`/`eqref` uses, 13 resolved citation keys, six bibliography entries, 13
  theorem-like statements, 13 proofs, a correctly nested environment stack,
  and zero submission placeholders.
- The most recent test run returned `30 passed in 0.33s` with no warning.
- The archived mixed-join audit contains 985 DP/subset comparisons, 11,003
  root-invariance comparisons, 985 local reconstruction checks, 184
  formula/definition comparisons, and 184 definition-first checks of the
  reconstructed tree-side sets, with zero failures in every category.
- MiKTeX-pdfTeX 4.27 / pdfTeX 1.40.29 compiled v6 through three passes to 14
  A4 pages. The retained native log contains no error, warning,
  overfull/underfull box, undefined reference/citation, missing character, or
  rerun request.
- All PDF fonts are embedded. The email and external URI annotations were
  enumerated, text extraction contains no unresolved marker, and all 14 pages
  were rendered and inspected without finding clipping, overlap, broken
  tables, black boxes, missing glyphs, orphan headings, or abnormal pagination.
- The v6 compiler PDF is copied byte-for-byte into `output/pdf/`; the native
  log and unmodified compiler PDF remain in `artifacts/v6_build/`.

## Core review files

| Path | Bytes | SHA-256 |
|---|---:|---|
| `README.md` | 3,105 | `EB4314D3061F13FED0A6DE8910D00D167393F04A1EFBD1C901FC7B7403D4F950` |
| `notes/collaborator_reading_guide.md` | 9,217 | `B8E89FF894E9607C6E16B09C3C98EA8FAFB75ED11F466477799511FC91C74F8A` |
| `drafts/mixed_join_research_note_v6.tex` | 49,825 | `6C8C1812C64FB3B55909A7CFC82383944A93D4C34DBD1423DBC839FA51E0B9FE` |
| `output/pdf/mixed_join_research_note_v6.pdf` | 470,046 | `C41FDA75669A253273CF05BC90F0B04DE9020884F982B1E6E56784583919DE44` |
| `artifacts/v6_build/mixed_join_research_note_v6.log` | 27,395 | `7696F4DCF9A5AF6B1F2EC40E0F899CFDA4DEF4ED883A8973FFC05B2007BC13D1` |
| `artifacts/mixed_join_v6_reproducibility.zip` | 21,868 | `0E91BAAC07EFA121784CA94355C93F304A7AF8FF89AB480E952E9C62DC316A33` |
| `notes/glm_5_3_review_adjudication.md` | 7,209 | `B812A198C15E0760E160D66686C632FBE8EA0C4BC5C2A5DEE15833D24F095D45` |
| `drafts/TEX_VERSION_HISTORY.md` | 8,928 | `BF2CA512F5175C2BB1FE634870D578CDD53787DE986B35172D5CE03EF4B1DA14` |
| `proofs/mixed_join_tree.md` | 10,400 | `65D23FAD3BA238FC068AD97963C1E136C8E5DD5C9DAEC29B76F84FC9A3D06409` |
| `notes/mixed_join_literature_positioning.md` | 19,931 | `0C1224F133C40ED22FC7BE828575D683384602233DEB8183CD9000D558A53D97` |

Recommended reading order is the collaborator guide, v6 TeX/PDF, GLM 5.3 and
earlier AI adjudication notes, reproducibility archive, version history,
proof-development note, and literature-positioning note. V2--v5 remain frozen
historical versions. The five v4-derived journal-name files remain format
references only and must not be submitted.

## Reproducibility dependency closure

| Path | Bytes | SHA-256 |
|---|---:|---|
| `requirements.txt` | 54 | `74BBC0D1430A450DF9DAB292A76970B01A9CDB84922E419BA24FF26704F12E9B` |
| `requirements-lock.txt` | 340 | `4811AEA9E5C13E192FB5865D7095ECBA19A33887ACC1D567AB5368E1D31DDE5E` |
| `REPRODUCIBILITY.md` | 1,442 | `C287D53518F003976243CEFB00B29E4E41881F32D4FFA6AD1F51F8937DFF0E36` |
| `src/__init__.py` | 75 | `ED1639318E17C6FF6C2B89761E68E2304314B2081B7A4F674C85D46BF40F19F0` |
| `src/mixed_join_tree.py` | 8,514 | `D3DDAB46510B217BF9C442CC57302953C4D0C29F208DD7ADE06381F2D90A8B9D` |
| `src/dual_gp_independent.py` | 9,021 | `D7BA1C520DC6991E78CB8BAE609A598E6BBF950DA03C1EAC9BA4D30D1EFFF231` |
| `experiments/audit_mixed_join_dp.py` | 7,978 | `AE55D305A2893B987E348F64273A7F3CD49738E202BBCD5ACCE48F7161366DCA` |
| `experiments/audit_extension_candidates.py` | 9,291 | `A463CE202995000F324BDB7F90D2821B1B97AB38911E3E8941DFFC381F8393F6` |
| `results/mixed_join_dp_audit.json` | 3,031 | `1FBCD77D2457F5EED9CC1ED518E47D097145EF0DF36648A3F21BA36D9AC1B7F9` |
| `tests/test_dual_gp_independent.py` | 3,306 | `DC838B029F97760FD67006CF582ECB205AE22AEE7F492CE1A5065680A6BA1674` |
| `tests/test_extension_feasibility.py` | 1,705 | `58EFBF1D99269B8081CA1F3A41FF212254AB46FE8132781299BEA82DEF5D9D80` |
| `tests/test_mixed_join_tree.py` | 4,103 | `20B6EA2F1F2B2493C606F638775EE4498F975020915E35D04E4021703D2B70BA` |

The main audit directly imports `src/mixed_join_tree.py`,
`src/dual_gp_independent.py`, and three graph/search helpers from
`experiments/audit_extension_candidates.py`. The test suite imports the same
modules. NetworkX is required for tree enumeration and pytest is required for
the tests. `requirements.txt` records the broader direct dependencies, while
`requirements-lock.txt` pins the complete installed environment. The freshly
checked versions were CPython 3.13.5, NetworkX 3.6.1, and pytest 9.1.1. A run
under a different Python or NetworkX version can reproduce the logical counts
while producing a byte-different JSON file because the report embeds
environment versions; a JSON hash difference alone is therefore not a
mathematical failure.

The two verification routes use different checking logic, but they share the
audit driver and NetworkX-generated tree samples. The DP/subset comparison also
shares the two local constraints defining `beta(T)` and therefore tests the
implementation rather than that structural reduction. The shortest-path route
tests the theorem and the reconstructed tree-side set from the definition. The
JSON report is generated output, not an input to the theorem or DP.

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
updated when each stage closes, and hashing the manifest inside itself would be
self-referential. The v4/v5 sources and journal derivatives are frozen
historical references. The target-journal note and journal-version index are
paired with the mutable submission workflow. Their omission from the digest
tables is intentional, not a missing dependency.

## Verified commands

From the repository root in PowerShell:

```powershell
.\.venv\Scripts\python.exe -m pytest -q .\tests
.\.venv\Scripts\python.exe .\experiments\audit_mixed_join_dp.py --output .\results\mixed_join_dp_audit.json
& pandoc .\drafts\mixed_join_research_note_v6.tex --from=latex --to=native | Out-Null
Get-ChildItem .\drafts\journal_versions\*.tex | ForEach-Object { & 'E:\Anaconda\Scripts\pandoc.exe' $_.FullName --from=latex --to=native | Out-Null; if ($LASTEXITCODE -ne 0) { throw "Pandoc failed: $($_.Name)" } }
& 'C:\Users\yyt\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex.exe' --enable-installer --interaction=nonstopmode --halt-on-error --file-line-error --output-directory=.\artifacts\v6_build .\drafts\mixed_join_research_note_v6.tex
```

The first command most recently returned 30 passing tests. The second command
most recently reproduced all five zero-failure audit categories; it overwrites
the canonical JSON path, so a reviewer who wants to preserve the archived file
should provide a different `--output` path and compare the two JSON objects.
The third command returned exit code zero and is only a Pandoc reader/static
syntax check. The final command was run three times; its last native log and
compiler PDF are preserved under `artifacts/v6_build/`.

V6 has completed the source, computation, compile, native-log, font/link, and
14-page visual checks recorded above. The initial four web-AI attempts and the
later GLM 5.3 adversarial report have been adjudicated. This is not human peer
review. Any later content revision must start v7 rather than overwrite the
preserved v3, v4, v5, or v6 files.

## Claim boundary

The proof and computation status above is internal. Jiang's future publication
status, the exact fan formula in the version-of-record body, an established
equivalent name or simpler closed form for `beta(T)`, subscription-index
coverage, global novelty/priority, final publishability/journal placement, and
the out-of-scope graph directions remain `UNKNOWN` as recorded in
`PROJECT_STATUS.md`. This manifest changes none of those statuses.
