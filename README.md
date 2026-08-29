# Dual General Position in Mixed Joins

This repository contains a research manuscript, proofs, algorithms, tests, and
reproducible computational checks for the dual general position number of the
mixed join

$$
K_r+T,
$$

where `r >= 1` and `T` is a tree of order at least three.

## Main result

Define

$$
\beta(T)=\max\{|X|:\Delta(T[X])\le 1,
|N_T(x)\setminus X|\le 1\text{ for every }x\in X\}.
$$

The manuscript proves

$$
gp_d(K_r+T)=
\begin{cases}
r+2, & T\in\{P_3,P_4\},\\
\beta(T), & \text{otherwise}.
\end{cases}
$$

It also gives a local characterization of feasible sets for `beta(T)` and a
linear-time dynamic program that reconstructs a maximum feasible set.

## Read the manuscript

- [Compiled v7 manuscript (PDF)](output/pdf/mixed_join_research_note_v7.pdf)
- [Current v7 LaTeX source](drafts/mixed_join_research_note_v7.tex)
- [Proof-development note](proofs/mixed_join_tree.md)
- [Literature positioning and search limits](notes/mixed_join_literature_positioning.md)
- [Collaborator reading guide](notes/collaborator_reading_guide.md)

V6 is frozen. V7 changes only the reproducibility-location wording by naming
this public repository; it does not change the mathematics. Any later revision
must use a new version number rather than overwrite an archived source.

## Reproducibility

The fixed supplementary archive is available here:

- [mixed_join_v6_reproducibility.zip](artifacts/mixed_join_v6_reproducibility.zip)

From the repository root, run the checks in an isolated environment:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r .\requirements-lock.txt
.\.venv\Scripts\python.exe -m pytest -q .\tests
.\.venv\Scripts\python.exe .\experiments\audit_mixed_join_dp.py `
  --output .\results\mixed_join_dp_audit_rerun.json
```

On macOS or Linux, replace the Python path by `.venv/bin/python`. See
[REPRODUCIBILITY.md](REPRODUCIBILITY.md) for the environment and audit scope.
The archived verification run produced 30 passing tests and zero failures in
all recorded audit categories.

## Repository map

- `src/`: dynamic program and definition-first checking code;
- `tests/`: pytest regression tests;
- `experiments/`: reproducible audit drivers;
- `results/`: machine-readable archived results;
- `proofs/`: proof and proof-audit notes;
- `notes/`: literature, review, and project documentation;
- `drafts/`: frozen manuscript sources and version history;
- `artifacts/`: fixed supplementary archive and retained build artifacts;
- `output/pdf/`: reading copy of the current manuscript.

## Verification boundaries

The manuscript contains mathematical proofs. The finite computations support
and test the implementation, but they are not proofs. This repository is not a
claim of global novelty or priority, and the manuscript has not undergone
human peer review. The exact literature and verification boundaries are
recorded in the manuscript and supporting notes.

The current v7 manuscript artifacts have the following SHA-256 digests:

- TeX: `8668552914DFC5B177FC951D102C3A8BB75EB0DFD92E5495DE51DED7A902D992`
- PDF: `B10D50C0A77F76AD24E87A78DCFC9C9A1D9D7385FD42D38AA311C1989C887500`
- ZIP: `0E91BAAC07EFA121784CA94355C93F304A7AF8FF89AB480E952E9C62DC316A33`

## License

No license has yet been selected. Public visibility permits reading and
forking through GitHub, but it does not by itself grant a general reuse
license. Code and manuscript/documentation licensing should be chosen
explicitly before a formal public release or archival deposit.
