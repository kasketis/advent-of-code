from __future__ import annotations

from collections import defaultdict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Callable


def generate_graph(edges: list[str]) -> dict[str, set[str]]:
    graph = defaultdict(set)
    for edge in edges:
        a, b = edge.split("-")
        graph[a].add(b)
        graph[b].add(a)
    return graph


def find_all_paths(
    graph: dict[str, set[str]],
    *,
    start_node: str,
    end_node: str,
    filter_: Callable[..., bool],
    path: list[str] | None = None,
) -> list[list[str]]:
    if path is None:
        path = []

    if filter_(start_node, path):
        return []

    path = path + [start_node]
    if start_node == end_node:
        return [path]

    paths = []
    for node in graph.get(start_node, []):
        extended_paths = find_all_paths(
            graph,
            start_node=node,
            end_node=end_node,
            filter_=filter_,
            path=path,
        )
        for p in extended_paths:
            paths.append(p)
    return paths


def filter_a(node: str, path: list[str]) -> bool:
    return node in path and node.islower()


def filter_b(node: str, path: list[str]) -> bool:
    if node in path:
        if node == "start":
            return True
        elif node.islower():
            small_caves = [path_node for path_node in path if path_node.islower() and path_node != "start"]
            return len(small_caves) > len(set(small_caves))
    return False


with open("input.txt") as f:
    lines = f.read().splitlines()


g = generate_graph(lines)

# 12
paths_a = find_all_paths(g, start_node="start", end_node="end", filter_=filter_a)
print(len(paths_a))

# 12b
paths_b = find_all_paths(g, start_node="start", end_node="end", filter_=filter_b)
print(len(paths_b))
