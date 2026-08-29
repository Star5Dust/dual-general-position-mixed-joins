"""Definition-first verification of the complete-first-factor formula.

This module deliberately does not import or copy the Jiang supplement.  Graphs
are stored as tuples of neighbor ``frozenset`` objects, product vertices remain
explicit ``(layer, base_vertex)`` pairs, and the formula side is evaluated by
enumerating two-clique partitions rather than by two-coloring the complement.

The routines are exponential and are intended only for small, auditable test
instances.  Computational agreement is evidence, not a mathematical proof.
"""

from __future__ import annotations

from collections import deque
from collections.abc import Hashable, Iterable, Iterator, Mapping
from itertools import combinations
from typing import TypeAlias


BaseGraph: TypeAlias = tuple[frozenset[int], ...]
Vertex: TypeAlias = Hashable
ExplicitGraph: TypeAlias = dict[Vertex, frozenset[Vertex]]
DistanceTable: TypeAlias = dict[Vertex, dict[Vertex, int]]
ProductVertex: TypeAlias = tuple[int, int]


def graph_from_edges(order: int, edges: Iterable[tuple[int, int]]) -> BaseGraph:
    """Build a loopless undirected graph on vertices ``0, ..., order - 1``."""
    if order < 0:
        raise ValueError("graph order must be nonnegative")
    adjacency = [set() for _ in range(order)]
    for left, right in edges:
        if not (0 <= left < order and 0 <= right < order):
            raise ValueError("edge endpoint lies outside the vertex set")
        if left == right:
            raise ValueError("loops are not allowed")
        adjacency[left].add(right)
        adjacency[right].add(left)
    return tuple(frozenset(neighbors) for neighbors in adjacency)


def labelled_graphs(order: int) -> Iterator[BaseGraph]:
    """Generate every labelled simple graph of the specified positive order."""
    if order < 1:
        return
    possible_edges = tuple(combinations(range(order), 2))
    for edge_count in range(len(possible_edges) + 1):
        for chosen_edges in combinations(possible_edges, edge_count):
            yield graph_from_edges(order, chosen_edges)


def explicit_base_graph(graph: BaseGraph) -> ExplicitGraph:
    """Convert a base graph to the generic explicit-adjacency representation."""
    _validate_base_graph(graph)
    return {vertex: graph[vertex] for vertex in range(len(graph))}


def lex_complete_first_factor(m: int, graph: BaseGraph) -> ExplicitGraph:
    """Construct ``K_m circ G`` with explicit pair-valued vertices."""
    if m < 1:
        raise ValueError("the number of layers must be positive")
    _validate_base_graph(graph)
    if not graph:
        raise ValueError("the base graph must be nonempty")

    vertices = tuple((layer, vertex) for layer in range(m) for vertex in range(len(graph)))
    product: ExplicitGraph = {}
    for layer, vertex in vertices:
        neighbors = {
            (other_layer, other_vertex)
            for other_layer, other_vertex in vertices
            if other_layer != layer
            or (other_layer == layer and other_vertex in graph[vertex])
        }
        product[(layer, vertex)] = frozenset(neighbors)
    return product


def all_pairs_distances(graph: Mapping[Vertex, frozenset[Vertex]]) -> DistanceTable:
    """Compute all distances by a fresh breadth-first search from each vertex."""
    if not graph:
        raise ValueError("distance table requires a nonempty graph")
    vertices = frozenset(graph)
    distances: DistanceTable = {}
    for source in graph:
        row = {source: 0}
        queue: deque[Vertex] = deque([source])
        while queue:
            current = queue.popleft()
            for neighbor in graph[current]:
                if neighbor not in vertices:
                    raise ValueError("adjacency refers to an unknown vertex")
                if current not in graph[neighbor]:
                    raise ValueError("adjacency is not symmetric")
                if neighbor not in row:
                    row[neighbor] = row[current] + 1
                    queue.append(neighbor)
        if len(row) != len(vertices):
            raise ValueError("dual general position is checked here only on connected graphs")
        distances[source] = row
    return distances


def is_general_position(selected: Iterable[Vertex], distances: DistanceTable) -> bool:
    """Test the definition: no selected vertex lies on a selected-pair geodesic."""
    chosen = tuple(selected)
    for first, second, third in combinations(chosen, 3):
        if _between(first, second, third, distances):
            return False
        if _between(first, third, second, distances):
            return False
        if _between(second, third, first, distances):
            return False
    return True


def is_convex(
    subset: Iterable[Vertex],
    all_vertices: Iterable[Vertex],
    distances: DistanceTable,
) -> bool:
    """Test that every geodesic between two subset vertices stays in the subset."""
    inside = frozenset(subset)
    outside = frozenset(all_vertices) - inside
    for first, second in combinations(inside, 2):
        for middle in outside:
            if _between(first, second, middle, distances):
                return False
    return True


def is_dual_general_position(
    selected: Iterable[Vertex],
    all_vertices: Iterable[Vertex],
    distances: DistanceTable,
) -> bool:
    """Check general position together with convexity of the complement."""
    universe = frozenset(all_vertices)
    chosen = frozenset(selected)
    if not chosen <= universe:
        raise ValueError("the selected set is not contained in the graph")
    return is_general_position(chosen, distances) and is_convex(
        universe - chosen, universe, distances
    )


def direct_dual_gp_number(graph: ExplicitGraph) -> int:
    """Maximize directly over all vertex subsets, from the shortest-path definition."""
    distances = all_pairs_distances(graph)
    vertices = tuple(graph)
    for size in range(len(vertices), -1, -1):
        for selected in combinations(vertices, size):
            if is_dual_general_position(selected, vertices, distances):
                return size
    raise AssertionError("the empty set must always be feasible")


def q2_by_partition_search(graph: BaseGraph) -> int:
    """Compute ``q2(G)`` by enumerating all partitions into two induced cliques."""
    _validate_base_graph(graph)
    if not graph:
        raise ValueError("q2 is used here only for nonempty base graphs")
    vertices = frozenset(range(len(graph)))
    for size in range(len(graph), -1, -1):
        for first_side_tuple in combinations(range(len(graph)), size):
            first_side = frozenset(first_side_tuple)
            if _is_clique(graph, first_side) and _is_clique(graph, vertices - first_side):
                return size
    return 0


def predicted_dual_gp_number(m: int, graph: BaseGraph) -> int:
    """Evaluate the audited candidate ``m q2(G)`` by partition search."""
    if m < 2:
        raise ValueError("the complete-first-factor formula requires m >= 2")
    return m * q2_by_partition_search(graph)


def layer_clique_characterization(
    m: int,
    graph: BaseGraph,
    selected: Iterable[ProductVertex],
) -> bool:
    """Evaluate the set classification stated in Jiang's Theorem 3.1."""
    if m < 2:
        raise ValueError("the layer characterization requires m >= 2")
    _validate_base_graph(graph)
    if not graph:
        raise ValueError("the base graph must be nonempty")
    chosen = frozenset(selected)
    universe = frozenset(
        (layer, vertex) for layer in range(m) for vertex in range(len(graph))
    )
    if not chosen <= universe:
        raise ValueError("the selected set contains a vertex outside the product")
    if not chosen:
        return True
    base_vertices = frozenset(range(len(graph)))
    for layer in range(m):
        layer_side = frozenset(vertex for current, vertex in chosen if current == layer)
        if not _is_clique(graph, layer_side):
            return False
        if not _is_clique(graph, base_vertices - layer_side):
            return False
    return True


def _between(
    first: Vertex,
    second: Vertex,
    middle: Vertex,
    distances: DistanceTable,
) -> bool:
    """Return whether ``middle`` lies on at least one first-second geodesic."""
    return distances[first][second] == (
        distances[first][middle] + distances[middle][second]
    )


def _is_clique(graph: BaseGraph, vertices: frozenset[int]) -> bool:
    return all(right in graph[left] for left, right in combinations(vertices, 2))


def _validate_base_graph(graph: BaseGraph) -> None:
    order = len(graph)
    for vertex, neighbors in enumerate(graph):
        if vertex in neighbors:
            raise ValueError("loops are not allowed")
        if any(neighbor < 0 or neighbor >= order for neighbor in neighbors):
            raise ValueError("adjacency refers to an unknown vertex")
        if any(vertex not in graph[neighbor] for neighbor in neighbors):
            raise ValueError("adjacency is not symmetric")
