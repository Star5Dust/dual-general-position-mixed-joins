from src.dual_gp_independent import direct_dual_gp_number, graph_from_edges

from experiments.audit_extension_candidates import (
    beta_tree,
    lexicographic_product,
    mixed_join_complete_tree,
    path_graph,
    predicted_mixed_join_value,
)


def test_mixed_join_has_complete_cross_adjacency_and_tree_internal_edges():
    product = mixed_join_complete_tree(2, path_graph(3))

    assert ("K", 1) in product[("K", 0)]
    assert ("T", 2) in product[("K", 0)]
    assert ("T", 1) in product[("T", 0)]
    assert ("T", 2) not in product[("T", 0)]


def test_lexicographic_product_respects_first_and_second_factor_edges():
    edgeless_two = graph_from_edges(2, ())
    product = lexicographic_product(path_graph(4), edgeless_two)

    assert (1, 0) in product[(0, 0)]
    assert (1, 1) in product[(0, 0)]
    assert (0, 1) not in product[(0, 0)]
    assert (2, 0) not in product[(0, 0)]


def test_beta_tree_named_values():
    star = graph_from_edges(4, ((0, 1), (0, 2), (0, 3)))

    assert beta_tree(path_graph(3)) == 2
    assert beta_tree(path_graph(4)) == 3
    assert beta_tree(path_graph(5)) == 4
    assert beta_tree(star) == 3


def test_mixed_join_prediction_matches_direct_named_cases():
    star = graph_from_edges(4, ((0, 1), (0, 2), (0, 3)))

    assert predicted_mixed_join_value(4, star) == 3
    assert direct_dual_gp_number(mixed_join_complete_tree(4, star)) == 3
    assert predicted_mixed_join_value(2, path_graph(3)) == 4
    assert direct_dual_gp_number(mixed_join_complete_tree(2, path_graph(3))) == 4


def test_small_path_first_candidate_has_zero_value():
    product = lexicographic_product(path_graph(4), path_graph(3))

    assert direct_dual_gp_number(product) == 0
