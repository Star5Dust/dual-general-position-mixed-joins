"""Bounded independent audit of the mixed-join theorem and beta-tree DP.

Two comparisons are kept separate:

* the linear-time DP is compared with exhaustive subset search for ``beta``;
* the resulting mixed-join formula is compared with the definition-first
  shortest-path checker.

The output is computational evidence and is not used as the proof.
"""

from __future__ import annotations

import argparse
import json
import platform
import sys
from pathlib import Path

import networkx as nx

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from experiments.audit_extension_candidates import (  # noqa: E402
    base_from_networkx,
    beta_tree,
    mixed_join_complete_tree,
)
from src.dual_gp_independent import direct_dual_gp_number  # noqa: E402
from src.mixed_join_tree import (  # noqa: E402
    is_beta_feasible,
    maximum_beta_set,
    mixed_join_dual_gp_number,
)


def _edges(tree: tuple[frozenset[int], ...]) -> list[list[int]]:
    return [
        [left, right]
        for left, neighbors in enumerate(tree)
        for right in sorted(neighbors)
        if left < right
    ]


def _beta_matrix(max_order: int = 12) -> dict[str, object]:
    comparisons = 0
    root_invariance_comparisons = 0
    mismatches: list[dict[str, object]] = []
    reconstruction_failures: list[dict[str, object]] = []
    summaries: list[dict[str, int]] = []
    for order in range(3, max_order + 1):
        trees = [
            base_from_networkx(tree)
            for tree in nx.generators.nonisomorphic_trees(order)
        ]
        values: list[int] = []
        for tree_index, tree in enumerate(trees):
            brute = beta_tree(tree)
            solution = maximum_beta_set(tree)
            comparisons += 1
            values.append(solution.value)
            if solution.value != brute:
                mismatches.append(
                    {
                        "tree_order": order,
                        "tree_index": tree_index,
                        "edges": _edges(tree),
                        "subset_search": brute,
                        "dp": solution.value,
                    }
                )
            if (
                len(solution.selected) != solution.value
                or not is_beta_feasible(tree, solution.selected)
            ):
                reconstruction_failures.append(
                    {
                        "tree_order": order,
                        "tree_index": tree_index,
                        "edges": _edges(tree),
                        "dp": solution.value,
                        "selected": sorted(solution.selected),
                    }
                )
            for root in range(order):
                rooted = maximum_beta_set(tree, root)
                root_invariance_comparisons += 1
                if rooted.value != solution.value:
                    mismatches.append(
                        {
                            "tree_order": order,
                            "tree_index": tree_index,
                            "edges": _edges(tree),
                            "root": root,
                            "root_zero_dp": solution.value,
                            "rerooted_dp": rooted.value,
                        }
                    )
        summaries.append(
            {
                "tree_order": order,
                "nonisomorphic_tree_count": len(trees),
                "beta_min": min(values),
                "beta_max": max(values),
            }
        )
    return {
        "orders": [3, max_order],
        "comparisons": comparisons,
        "root_invariance_comparisons": root_invariance_comparisons,
        "mismatch_count": len(mismatches),
        "mismatches": mismatches,
        "reconstruction_failure_count": len(reconstruction_failures),
        "reconstruction_failures": reconstruction_failures,
        "summaries": summaries,
    }


def _mixed_join_matrix(max_tree_order: int = 8) -> dict[str, object]:
    comparisons = 0
    mismatches: list[dict[str, object]] = []
    summaries: list[dict[str, int]] = []
    for order in range(3, max_tree_order + 1):
        trees = [
            base_from_networkx(tree)
            for tree in nx.generators.nonisomorphic_trees(order)
        ]
        for r in range(1, 5):
            for tree_index, tree in enumerate(trees):
                direct = direct_dual_gp_number(mixed_join_complete_tree(r, tree))
                formula = mixed_join_dual_gp_number(r, tree)
                comparisons += 1
                if direct != formula:
                    mismatches.append(
                        {
                            "tree_order": order,
                            "tree_index": tree_index,
                            "edges": _edges(tree),
                            "r": r,
                            "shortest_path_direct": direct,
                            "dp_formula": formula,
                        }
                    )
        summaries.append(
            {
                "tree_order": order,
                "nonisomorphic_tree_count": len(trees),
                "r_min": 1,
                "r_max": 4,
            }
        )
    return {
        "tree_orders": [3, max_tree_order],
        "r_values": [1, 2, 3, 4],
        "comparisons": comparisons,
        "mismatch_count": len(mismatches),
        "mismatches": mismatches,
        "summaries": summaries,
    }


def build_report() -> dict[str, object]:
    """Run both bounded verification matrices."""
    return {
        "schema_version": 1,
        "audit_date": "2026-08-28",
        "status": "computational verification evidence, not proof",
        "environment": {
            "python": platform.python_version(),
            "networkx": nx.__version__,
        },
        "beta_dp_vs_exhaustive_subset_search": _beta_matrix(),
        "mixed_join_formula_vs_shortest_path_definition": _mixed_join_matrix(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = build_report()
    rendered = json.dumps(report, indent=2, sort_keys=True)
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)


if __name__ == "__main__":
    main()
