# Reproducing the mixed-join computations

The computational checks are supporting evidence and are not used as proofs.
The proofs in the manuscript are self-contained.

## Environment

The archived run used CPython 3.13.5 on Windows 11 build 26100. The exact
Python package versions are recorded in `requirements-lock.txt`.

From the root of an extracted archive, create an isolated environment and
run the checks as follows in Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r .\requirements-lock.txt
.\.venv\Scripts\python.exe -m pytest -q .\tests
.\.venv\Scripts\python.exe .\experiments\audit_mixed_join_dp.py `
  --output .\results\mixed_join_dp_audit.json
```

On macOS or Linux, replace `.\.venv\Scripts\python.exe` by
`.venv/bin/python` and use the shell line-continuation convention of the
chosen shell.

The audit compares the tree dynamic program with exhaustive search over the
two defining local constraints, checks root invariance and reconstruction,
compares the mixed-join formula with a definition-first shortest-path search,
and checks every reconstructed tree-side set in the small mixed-join matrix
directly from the definition of dual general position.

The main report is `results/mixed_join_dp_audit.json`. The earlier
target-selection report is `results/extension_feasibility_audit.json` and is
not added to the main totals because its mixed-join instances overlap.
