from itertools import combinations

import pytest

from src.dual_gp_independent import (
    all_pairs_distances,
    direct_dual_gp_number,
    explicit_base_graph,
    graph_from_edges,
    is_convex,
    is_dual_general_position,
    is_general_position,
    labelled_graphs,
    layer_clique_characterization,
    lex_complete_first_factor,
    predicted_dual_gp_number,
    q2_by_partition_search,
)


def path_graph(order: int):
    return graph_from_edges(order, ((vertex, vertex + 1) for vertex in range(order - 1)))


def complete_graph(order: int):
    return graph_from_edges(order, combinations(range(order), 2))


def test_definition_checks_on_p3():
    path = explicit_base_graph(path_graph(3))
    distances = all_pairs_distances(path)

    assert distances[0][2] == 2
    assert is_general_position({0, 2}, distances)
    assert not is_general_position({0, 1, 2}, distances)
    assert is_convex({0, 1}, path, distances)
    assert not is_convex({0, 2}, path, distances)
    assert is_dual_general_position({0, 2}, path, distances)
    assert not is_dual_general_position({1}, path, distances)


def test_complete_first_product_keeps_explicit_layers():
    product = lex_complete_first_factor(2, path_graph(3))

    assert (0, 1) in product[(0, 0)]
    assert (0, 2) not in product[(0, 0)]
    assert {(1, 0), (1, 1), (1, 2)} <= product[(0, 0)]


@pytest.mark.parametrize(
    ("graph", "expected"),
    [
        (complete_graph(1), 1),
        (complete_graph(2), 2),
        (path_graph(3), 2),
        (path_graph(4), 2),
        (path_graph(5), 0),
        (graph_from_edges(4, ((0, 1), (0, 2), (0, 3))), 0),
        (graph_from_edges(3, ()), 0),
    ],
)
def test_q2_partition_search_boundary_values(graph, expected):
    assert q2_by_partition_search(graph) == expected


@pytest.mark.parametrize(
    ("m", "graph", "expected"),
    [
        (2, complete_graph(3), 6),
        (2, path_graph(3), 4),
        (2, path_graph(4), 4),
        (2, path_graph(5), 0),
        (2, graph_from_edges(4, ((0, 1), (0, 2), (0, 3))), 0),
        (3, path_graph(3), 6),
    ],
)
def test_formula_matches_direct_named_cases(m, graph, expected):
    direct = direct_dual_gp_number(lex_complete_first_factor(m, graph))
    predicted = predicted_dual_gp_number(m, graph)

    assert direct == expected
    assert predicted == expected


def test_layer_characterization_matches_every_subset_for_small_products():
    for graph in labelled_graphs(3):
        product = lex_complete_first_factor(2, graph)
        vertices = tuple(product)
        distances = all_pairs_distances(product)
        for size in range(len(vertices) + 1):
            for selected in combinations(vertices, size):
                assert is_dual_general_position(selected, vertices, distances) == (
                    layer_clique_characterization(2, graph, selected)
                )


def test_formula_rejects_m_equals_one_and_empty_base():
    with pytest.raises(ValueError, match="m >= 2"):
        predicted_dual_gp_number(1, path_graph(3))
    with pytest.raises(ValueError, match="nonempty"):
        predicted_dual_gp_number(2, ())


def test_labelled_graph_counts_are_complete():
    assert [sum(1 for _ in labelled_graphs(order)) for order in range(1, 5)] == [
        1,
        2,
        8,
        64,
    ]
