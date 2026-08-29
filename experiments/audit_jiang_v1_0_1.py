"""Run the project's structurally independent Jiang v1.0.1 checks."""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import sys
import time
from itertools import combinations, product
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from src.dual_gp_independent import (
    BaseGraph,
    all_pairs_distances,
    direct_dual_gp_number,
    graph_from_edges,
    is_dual_general_position,
    labelled_graphs,
    layer_clique_characterization,
    lex_complete_first_factor,
    predicted_dual_gp_number,
)


def prufer_tree(sequence: tuple[int, ...]) -> BaseGraph:
    """Decode one Prüfer sequence without using a graph library."""
    order = len(sequence) + 2
    degrees = [1] * order
    for vertex in sequence:
        degrees[vertex] += 1
    edges: list[tuple[int, int]] = []
    for vertex in sequence:
        leaf = min(index for index, degree in enumerate(degrees) if degree == 1)
        edges.append((leaf, vertex))
        degrees[leaf] -= 1
        degrees[vertex] -= 1
    final_pair = tuple(index for index, degree in enumerate(degrees) if degree == 1)
    edges.append((final_pair[0], final_pair[1]))
    return graph_from_edges(order, edges)


def labelled_trees(order: int):
    """Generate all labelled trees using Prüfer's bijection."""
    if order == 1:
        yield graph_from_edges(1, ())
        return
    for sequence in product(range(order), repeat=order - 2):
        yield prufer_tree(sequence)


def compare_maximum(
    family: str,
    m: int,
    graph: BaseGraph,
    index: int,
    mismatches: list[dict[str, object]],
) -> None:
    direct = direct_dual_gp_number(lex_complete_first_factor(m, graph))
    predicted = predicted_dual_gp_number(m, graph)
    if direct != predicted:
        mismatches.append(
            {
                "family": family,
                "index": index,
                "m": m,
                "adjacency_lists": [sorted(neighbors) for neighbors in graph],
                "direct": direct,
                "predicted": predicted,
            }
        )


def classification_comparisons(m: int, graph: BaseGraph) -> tuple[int, list[dict[str, object]]]:
    product_graph = lex_complete_first_factor(m, graph)
    vertices = tuple(product_graph)
    distances = all_pairs_distances(product_graph)
    checked = 0
    mismatches: list[dict[str, object]] = []
    for size in range(len(vertices) + 1):
        for selected in combinations(vertices, size):
            direct = is_dual_general_position(selected, vertices, distances)
            classified = layer_clique_characterization(m, graph, selected)
            checked += 1
            if direct != classified:
                mismatches.append(
                    {
                        "m": m,
                        "adjacency_lists": [sorted(neighbors) for neighbors in graph],
                        "selected": [list(vertex) for vertex in selected],
                        "direct": direct,
                        "classified": classified,
                    }
                )
    return checked, mismatches


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run() -> dict[str, object]:
    started = time.perf_counter()
    maximum_mismatches: list[dict[str, object]] = []
    family_counts: dict[str, int] = {}

    for m, maximum_order in ((2, 4), (3, 3)):
        family = f"all_labelled_m{m}_orders_1_to_{maximum_order}"
        count = 0
        for order in range(1, maximum_order + 1):
            for graph in labelled_graphs(order):
                compare_maximum(family, m, graph, count, maximum_mismatches)
                count += 1
        family_counts[family] = count

    tree_family = "all_labelled_trees_order_5_m2"
    tree_count = 0
    for graph in labelled_trees(5):
        compare_maximum(tree_family, 2, graph, tree_count, maximum_mismatches)
        tree_count += 1
    family_counts[tree_family] = tree_count

    named_cases = (
        ("K5", 2, graph_from_edges(5, combinations(range(5), 2))),
        ("empty5", 2, graph_from_edges(5, ())),
        ("P5", 2, graph_from_edges(5, ((0, 1), (1, 2), (2, 3), (3, 4)))),
        ("C5", 2, graph_from_edges(5, ((0, 1), (1, 2), (2, 3), (3, 4), (4, 0)))),
        ("K2_union_K3", 2, graph_from_edges(5, ((0, 1), (2, 3), (2, 4), (3, 4)))),
        ("P4_m3", 3, graph_from_edges(4, ((0, 1), (1, 2), (2, 3)))),
    )
    for index, (label, m, graph) in enumerate(named_cases):
        compare_maximum(label, m, graph, index, maximum_mismatches)
    family_counts["named_boundary_cases"] = len(named_cases)

    classification_checked = 0
    classification_mismatches: list[dict[str, object]] = []
    for m in (2, 3):
        for order in range(1, 4):
            for graph in labelled_graphs(order):
                checked, mismatches = classification_comparisons(m, graph)
                classification_checked += checked
                classification_mismatches.extend(mismatches)

    source_path = REPO_ROOT / "src" / "dual_gp_independent.py"
    result: dict[str, object] = {
        "schema_version": 1,
        "python_version": platform.python_version(),
        "python_implementation": platform.python_implementation(),
        "platform": platform.platform(),
        "implementation_sha256": file_sha256(source_path),
        "driver_sha256": file_sha256(Path(__file__).resolve()),
        "maximum_family_counts": family_counts,
        "maximum_comparisons": sum(family_counts.values()),
        "maximum_mismatches": len(maximum_mismatches),
        "classification_set_comparisons": classification_checked,
        "classification_mismatches": len(classification_mismatches),
        "elapsed_seconds": time.perf_counter() - started,
    }
    if maximum_mismatches:
        result["maximum_mismatch_details"] = maximum_mismatches
    if classification_mismatches:
        result["classification_mismatch_details"] = classification_mismatches
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    result = run()
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if arguments.output is not None:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_text(rendered, encoding="utf-8")
    sys.stdout.write(rendered)
    return int(bool(result["maximum_mismatches"] or result["classification_mismatches"]))


if __name__ == "__main__":
    raise SystemExit(main())
