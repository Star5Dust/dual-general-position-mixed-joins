import networkx as nx
import pytest

from experiments.audit_extension_candidates import (
    beta_tree,
    base_from_networkx,
    mixed_join_complete_tree,
    path_graph,
)
from src.dual_gp_independent import (
    all_pairs_distances,
    direct_dual_gp_number,
    graph_from_edges,
    is_dual_general_position,
)
from src.mixed_join_tree import (
    beta_tree_dp,
    is_beta_feasible,
    maximum_beta_set,
    mixed_join_dual_gp_number,
)


def test_beta_dp_named_values_and_reconstruction():
    star = graph_from_edges(4, ((0, 1), (0, 2), (0, 3)))
    subdivided_star = graph_from_edges(
        7,
        ((0, 1), (0, 2), (0, 3), (1, 4), (2, 5), (3, 6)),
    )

    for tree, expected in (
        (path_graph(3), 2),
        (path_graph(4), 3),
        (path_graph(5), 4),
        (star, 3),
        (subdivided_star, 6),
    ):
        solution = maximum_beta_set(tree)
        assert solution.value == expected
        assert len(solution.selected) == expected
        assert is_beta_feasible(tree, solution.selected)


def test_degree_three_vertex_cannot_be_selected():
    star = graph_from_edges(4, ((0, 1), (0, 2), (0, 3)))

    assert not is_beta_feasible(star, {0})
    assert is_beta_feasible(star, {1, 2, 3})


def test_beta_dp_matches_subset_search_and_is_root_independent():
    for order in range(3, 9):
        for nx_tree in nx.generators.nonisomorphic_trees(order):
            tree = base_from_networkx(nx_tree)
            expected = beta_tree(tree)
            assert beta_tree_dp(tree) == expected
            assert {beta_tree_dp(tree, root) for root in range(order)} == {expected}


def test_mixed_join_formula_matches_shortest_path_checker_on_small_matrix():
    for order in range(3, 7):
        for nx_tree in nx.generators.nonisomorphic_trees(order):
            tree = base_from_networkx(nx_tree)
            for r in range(1, 4):
                assert mixed_join_dual_gp_number(r, tree) == (
                    direct_dual_gp_number(mixed_join_complete_tree(r, tree))
                )


def test_reconstructed_tree_side_set_is_dual_gp_and_separates_weaker_problem():
    # Root 0, internal vertices 1 and 2, and two leaves below each internal
    # vertex form the depth-two complete binary tree used in the manuscript.
    tree = graph_from_edges(
        7,
        ((0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)),
    )
    solution = maximum_beta_set(tree)
    assert solution.value == 4
    assert solution.selected == frozenset({3, 4, 5, 6})

    # The weaker induced-maximum-degree-one condition admits five vertices.
    weaker_witness = frozenset({0, 3, 4, 5, 6})
    assert all(
        sum(neighbor in weaker_witness for neighbor in tree[vertex]) <= 1
        for vertex in weaker_witness
    )
    assert not is_beta_feasible(tree, weaker_witness)

    for r in range(1, 5):
        mixed_join = mixed_join_complete_tree(r, tree)
        selected = frozenset(("T", vertex) for vertex in solution.selected)
        assert is_dual_general_position(
            selected, mixed_join, all_pairs_distances(mixed_join)
        )


def test_long_path_reconstruction_does_not_use_python_recursion():
    tree = path_graph(2500)
    solution = maximum_beta_set(tree)

    assert solution.value == len(solution.selected)
    assert is_beta_feasible(tree, solution.selected)


def test_tree_and_scope_validation():
    cycle = graph_from_edges(3, ((0, 1), (1, 2), (2, 0)))
    disconnected_with_cycle = graph_from_edges(
        4, ((0, 1), (1, 2), (2, 0))
    )

    with pytest.raises(ValueError, match="nonempty"):
        beta_tree_dp(())
    with pytest.raises(ValueError, match="not a tree"):
        beta_tree_dp(cycle)
    with pytest.raises(ValueError, match="not a tree"):
        beta_tree_dp(disconnected_with_cycle)
    with pytest.raises(ValueError, match="outside"):
        beta_tree_dp(path_graph(3), root=3)
    with pytest.raises(ValueError, match="at least one"):
        mixed_join_dual_gp_number(0, path_graph(3))
    with pytest.raises(ValueError, match="order at least three"):
        mixed_join_dual_gp_number(1, path_graph(2))
