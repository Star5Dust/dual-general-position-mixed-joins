"""Linear-time dynamic program for the mixed-join tree parameter.

For a tree ``T``, ``beta(T)`` is the maximum size of a vertex set ``X`` such
that each selected vertex has at most one selected neighbor and at most one
unselected neighbor.  This module is deliberately independent of the
shortest-path dual-general-position checker in ``dual_gp_independent.py``.

The public reconstruction routine returns both the optimum value and one
maximum set.  The implementation follows the rooted-tree recurrence proved in
``proofs/mixed_join_tree.md``.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import TypeAlias


Tree: TypeAlias = tuple[frozenset[int], ...]


@dataclass(frozen=True)
class BetaSolution:
    """The value of ``beta(T)`` together with one attaining vertex set."""

    value: int
    selected: frozenset[int]


@dataclass(frozen=True)
class _Entry:
    value: int
    child_labels: tuple[int, ...]


def is_beta_feasible(tree: Tree, selected: frozenset[int] | set[int]) -> bool:
    """Return whether ``selected`` satisfies the two local beta constraints."""
    _validate_tree(tree, 0)
    chosen = frozenset(selected)
    if not chosen <= frozenset(range(len(tree))):
        raise ValueError("the selected set contains a vertex outside the tree")
    return all(
        sum(neighbor in chosen for neighbor in tree[vertex]) <= 1
        and sum(neighbor not in chosen for neighbor in tree[vertex]) <= 1
        for vertex in chosen
    )


def maximum_beta_set(tree: Tree, root: int = 0) -> BetaSolution:
    """Compute ``beta(T)`` and reconstruct one maximum feasible set.

    The table state fixes whether the current vertex and its parent are
    selected.  An unselected current vertex imposes no local restriction.  A
    selected vertex of tree degree at least three is immediately infeasible;
    hence at most four child-label patterns ever need inspection in a selected
    state.  The running time and storage are both linear in ``|V(T)|``.
    """
    _validate_tree(tree, root)
    parent, children, traversal = _rooted_structure(tree, root)
    tables: list[dict[tuple[int, int | None], _Entry]] = [
        {} for _ in range(len(tree))
    ]

    for vertex in reversed(traversal):
        parent_labels: tuple[int | None, ...]
        if vertex == root:
            parent_labels = (None,)
        else:
            parent_labels = (0, 1)

        for parent_label in parent_labels:
            # If vertex is unselected, its children are independent and each
            # child sees an unselected parent.
            child_labels: list[int] = []
            value = 0
            for child in children[vertex]:
                available_labels = tuple(
                    candidate
                    for candidate in (0, 1)
                    if (candidate, 0) in tables[child]
                )
                label = max(
                    available_labels,
                    key=lambda candidate: (
                        tables[child][(candidate, 0)].value,
                        candidate,
                    ),
                )
                child_labels.append(label)
                value += tables[child][(label, 0)].value
            tables[vertex][(0, parent_label)] = _Entry(
                value=value,
                child_labels=tuple(child_labels),
            )

            parent_count = 0 if parent_label is None else 1
            degree = parent_count + len(children[vertex])
            if degree >= 3:
                continue

            best: _Entry | None = None
            for labels in product((0, 1), repeat=len(children[vertex])):
                if any(
                    (label, 1) not in tables[child]
                    for child, label in zip(children[vertex], labels)
                ):
                    continue
                selected_neighbors = (
                    (0 if parent_label is None else parent_label) + sum(labels)
                )
                unselected_neighbors = degree - selected_neighbors
                if selected_neighbors > 1 or unselected_neighbors > 1:
                    continue
                candidate = _Entry(
                    value=1
                    + sum(
                        tables[child][(label, 1)].value
                        for child, label in zip(children[vertex], labels)
                    ),
                    child_labels=labels,
                )
                if best is None or (candidate.value, candidate.child_labels) > (
                    best.value,
                    best.child_labels,
                ):
                    best = candidate
            if best is not None:
                tables[vertex][(1, parent_label)] = best

    root_label = max(
        (
            label
            for label in (0, 1)
            if (label, None) in tables[root]
        ),
        key=lambda label: (tables[root][(label, None)].value, label),
    )
    selected: set[int] = set()
    reconstruction_stack = [(root, root_label, None)]
    while reconstruction_stack:
        vertex, label, parent_label = reconstruction_stack.pop()
        if label:
            selected.add(vertex)
        entry = tables[vertex][(label, parent_label)]
        for child, child_label in zip(children[vertex], entry.child_labels):
            reconstruction_stack.append((child, child_label, label))
    result = BetaSolution(
        value=tables[root][(root_label, None)].value,
        selected=frozenset(selected),
    )
    if result.value != len(result.selected) or not is_beta_feasible(
        tree, result.selected
    ):
        raise AssertionError("internal DP reconstruction failure")
    return result


def beta_tree_dp(tree: Tree, root: int = 0) -> int:
    """Return ``beta(T)`` by the rooted-tree dynamic program."""
    return maximum_beta_set(tree, root).value


def mixed_join_dual_gp_number(r: int, tree: Tree) -> int:
    """Evaluate the proved formula for ``gp_d(K_r + T)``.

    This scoped interface requires ``r >= 1`` and a tree of order at least
    three, exactly as in the mixed-join theorem.  Among such trees, ``q_2(T)``
    is positive precisely for ``P_3`` and ``P_4``, and then equals two.
    """
    if r < 1:
        raise ValueError("r must be at least one")
    _validate_tree(tree, 0)
    if len(tree) < 3:
        raise ValueError("the mixed-join theorem requires tree order at least three")
    beta = beta_tree_dp(tree)
    q2 = 2 if _is_p3_or_p4(tree) else 0
    return beta if q2 == 0 else max(beta, r + q2)


def _is_p3_or_p4(tree: Tree) -> bool:
    if len(tree) == 3:
        return True
    return len(tree) == 4 and sorted(map(len, tree)) == [1, 1, 2, 2]


def _rooted_structure(
    tree: Tree, root: int
) -> tuple[list[int | None], list[tuple[int, ...]], list[int]]:
    parent: list[int | None] = [None] * len(tree)
    parent[root] = root
    traversal: list[int] = []
    stack = [root]
    while stack:
        vertex = stack.pop()
        traversal.append(vertex)
        for neighbor in sorted(tree[vertex], reverse=True):
            if parent[neighbor] is None:
                parent[neighbor] = vertex
                stack.append(neighbor)
    children = [
        tuple(sorted(neighbor for neighbor in tree[vertex] if parent[neighbor] == vertex))
        for vertex in range(len(tree))
    ]
    parent[root] = None
    return parent, children, traversal


def _validate_tree(tree: Tree, root: int) -> None:
    order = len(tree)
    if order == 0:
        raise ValueError("the tree must be nonempty")
    if not 0 <= root < order:
        raise ValueError("the root lies outside the tree")
    for vertex, neighbors in enumerate(tree):
        if vertex in neighbors:
            raise ValueError("loops are not allowed")
        if any(neighbor < 0 or neighbor >= order for neighbor in neighbors):
            raise ValueError("adjacency refers to an unknown vertex")
        if any(vertex not in tree[neighbor] for neighbor in neighbors):
            raise ValueError("adjacency is not symmetric")
    if sum(map(len, tree)) != 2 * (order - 1):
        raise ValueError("the graph is not a tree")
    seen = {root}
    stack = [root]
    while stack:
        vertex = stack.pop()
        for neighbor in tree[vertex]:
            if neighbor not in seen:
                seen.add(neighbor)
                stack.append(neighbor)
    if len(seen) != order:
        raise ValueError("the graph is not a tree")
