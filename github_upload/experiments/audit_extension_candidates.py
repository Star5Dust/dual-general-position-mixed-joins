"""Bounded feasibility checks for post-Jiang extension candidates.

This is deliberately a small audit matrix, not a general-purpose enumerator.
It reuses the project's definition-first dual-general-position checker and
compares two restricted directions:

* mixed joins ``K_r + T`` for nonisomorphic trees of orders 3 through 7;
* path-first products ``P_n circ G`` on a few smallest noncomplete graphs.

The computations are evidence for target selection, not proofs.
"""

from __future__ import annotations

import argparse
import json
import platform
import sys
from itertools import combinations
from pathlib import Path

import networkx as nx

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from src.dual_gp_independent import (  # noqa: E402
    BaseGraph,
    ExplicitGraph,
    direct_dual_gp_number,
    graph_from_edges,
    labelled_graphs,
    q2_by_partition_search,
)


def path_graph(order: int) -> BaseGraph:
    """Return the path ``P_order`` in the project's base representation."""
    return graph_from_edges(order, ((vertex, vertex + 1) for vertex in range(order - 1)))


def complete_graph(order: int) -> BaseGraph:
    """Return ``K_order`` in the project's base representation."""
    return graph_from_edges(order, combinations(range(order), 2))


def is_complete(graph: BaseGraph) -> bool:
    """Test completeness, including the order-zero and order-one conventions."""
    return all(right in graph[left] for left, right in combinations(range(len(graph)), 2))


def base_from_networkx(graph: nx.Graph) -> BaseGraph:
    """Convert a graph labelled by consecutive integers into ``BaseGraph``."""
    if set(graph) != set(range(graph.number_of_nodes())):
        graph = nx.convert_node_labels_to_integers(graph, ordering="sorted")
    return graph_from_edges(graph.number_of_nodes(), graph.edges())


def mixed_join_complete_tree(r: int, tree: BaseGraph) -> ExplicitGraph:
    """Construct the mixed join ``K_r + T`` with tagged explicit vertices."""
    if r < 1:
        raise ValueError("the complete factor must be nonempty")
    if not tree:
        raise ValueError("the tree factor must be nonempty")
    complete_vertices = tuple(("K", vertex) for vertex in range(r))
    tree_vertices = tuple(("T", vertex) for vertex in range(len(tree)))
    vertices = complete_vertices + tree_vertices
    product: ExplicitGraph = {}
    for vertex in vertices:
        neighbors = set()
        for other in vertices:
            if vertex == other:
                continue
            if vertex[0] == "K" or other[0] == "K":
                neighbors.add(other)
            elif other[1] in tree[vertex[1]]:
                neighbors.add(other)
        product[vertex] = frozenset(neighbors)
    return product


def lexicographic_product(first: BaseGraph, second: BaseGraph) -> ExplicitGraph:
    """Construct ``first circ second`` with explicit pair-valued vertices."""
    if not first or not second:
        raise ValueError("both lexicographic-product factors must be nonempty")
    vertices = tuple(
        (first_vertex, second_vertex)
        for first_vertex in range(len(first))
        for second_vertex in range(len(second))
    )
    return {
        (first_vertex, second_vertex): frozenset(
            (other_first, other_second)
            for other_first, other_second in vertices
            if (
                first_vertex == other_first
                and other_second in second[second_vertex]
            )
            or other_first in first[first_vertex]
        )
        for first_vertex, second_vertex in vertices
    }


def beta_tree(tree: BaseGraph) -> int:
    """Evaluate the apex-avoiding mixed-join candidate parameter by subsets.

    A side ``X`` is counted when every selected vertex has at most one selected
    tree neighbor and at most one unselected tree neighbor.  The historical
    target-selection audit uses this helper through order seven; the later
    dedicated DP audit uses it through order twelve.
    """
    best = 0
    for mask in range(1 << len(tree)):
        selected = {vertex for vertex in range(len(tree)) if mask & (1 << vertex)}
        feasible = all(
            sum(neighbor in selected for neighbor in tree[vertex]) <= 1
            and sum(neighbor not in selected for neighbor in tree[vertex]) <= 1
            for vertex in selected
        )
        if feasible:
            best = max(best, len(selected))
    return best


def predicted_mixed_join_value(r: int, tree: BaseGraph) -> int:
    """Evaluate the two-branch feasibility reduction for ``K_r + T``."""
    q2 = q2_by_partition_search(tree)
    beta = beta_tree(tree)
    if q2 == 0:
        return beta
    return max(beta, r + q2)


def _mixed_join_matrix() -> dict[str, object]:
    comparisons = 0
    mismatches: list[dict[str, int]] = []
    summaries: list[dict[str, int]] = []
    for order in range(3, 8):
        trees = [
            base_from_networkx(tree)
            for tree in nx.generators.nonisomorphic_trees(order)
        ]
        beta_values = [beta_tree(tree) for tree in trees]
        q2_values = [q2_by_partition_search(tree) for tree in trees]
        summaries.append(
            {
                "tree_order": order,
                "nonisomorphic_tree_count": len(trees),
                "beta_min": min(beta_values),
                "beta_max": max(beta_values),
                "q2_positive_count": sum(value > 0 for value in q2_values),
            }
        )
        for r in range(1, 5):
            for tree_index, tree in enumerate(trees):
                direct = direct_dual_gp_number(mixed_join_complete_tree(r, tree))
                predicted = predicted_mixed_join_value(r, tree)
                comparisons += 1
                if direct != predicted:
                    mismatches.append(
                        {
                            "tree_order": order,
                            "tree_index": tree_index,
                            "r": r,
                            "direct": direct,
                            "predicted": predicted,
                        }
                    )

    star = graph_from_edges(4, ((0, 1), (0, 2), (0, 3)))
    star_counterexample = {
        "tree": "K_1,3",
        "q2": q2_by_partition_search(star),
        "beta": beta_tree(star),
        "values": [
            {
                "r": r,
                "direct_dual_gp_number": direct_dual_gp_number(
                    mixed_join_complete_tree(r, star)
                ),
            }
            for r in range(1, 5)
        ],
    }
    return {
        "comparisons": comparisons,
        "mismatch_count": len(mismatches),
        "mismatches": mismatches,
        "summaries": summaries,
        "star_counterexample": star_counterexample,
    }


def _path_first_matrix() -> dict[str, object]:
    comparisons = 0
    nonzero_cases: list[dict[str, int]] = []
    for path_order in (4, 5):
        for second_order in (2, 3):
            graphs = [
                graph for graph in labelled_graphs(second_order) if not is_complete(graph)
            ]
            for graph_index, graph in enumerate(graphs):
                value = direct_dual_gp_number(
                    lexicographic_product(path_graph(path_order), graph)
                )
                comparisons += 1
                if value != 0:
                    nonzero_cases.append(
                        {
                            "path_order": path_order,
                            "second_order": second_order,
                            "graph_index": graph_index,
                            "direct_dual_gp_number": value,
                        }
                    )

    second = next(graph for graph in labelled_graphs(2) if not is_complete(graph))
    value = direct_dual_gp_number(lexicographic_product(path_graph(6), second))
    comparisons += 1
    if value != 0:
        nonzero_cases.append(
            {
                "path_order": 6,
                "second_order": 2,
                "graph_index": 0,
                "direct_dual_gp_number": value,
            }
        )
    return {
        "comparisons": comparisons,
        "nonzero_case_count": len(nonzero_cases),
        "nonzero_cases": nonzero_cases,
    }


def build_report() -> dict[str, object]:
    """Run the bounded matrices and return a machine-readable report."""
    return {
        "schema_version": 1,
        "audit_date": "2026-08-28",
        "status": "computational feasibility evidence, not proof",
        "environment": {
            "python": platform.python_version(),
            "networkx": nx.__version__,
        },
        "mixed_join_Kr_plus_tree": _mixed_join_matrix(),
        "path_first_lexicographic_product": _path_first_matrix(),
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
