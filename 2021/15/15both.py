import heapq
from collections import defaultdict
from itertools import chain

Risk = int
Node = tuple[int, int]
Graph = dict[Node, dict[Node, int]]


def generate_graph(
    risk_levels: list[list[Risk]],
) -> Graph:
    graph: Graph = defaultdict(lambda: defaultdict(int))
    max_x, max_y = len(risk_levels[0]), len(risk_levels)
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            for rel_x, rel_y in (0, -1), (1, 0), (0, 1), (-1, 0):
                adj_x = x + rel_x
                adj_y = y + rel_y
                if 0 <= adj_x < max_x and 0 <= adj_y < max_y:
                    graph[(x, y)][(adj_x, adj_y)] = risk_levels[adj_y][adj_x]
    return graph


def min_risk(graph: Graph, entry: Node, exit_: Node):
    visited = set()
    queue: list[tuple[Risk, Node]] = [(0, entry)]
    total_risk = 0
    node = entry
    while node != exit_:
        total_risk, node = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            for adjacent, risk in graph[node].items():
                heapq.heappush(queue, (total_risk + risk, adjacent))
    return total_risk


with open("input.txt") as f:
    lines = [[int(risk) for risk in line] for line in f.read().splitlines()]

cave_entry: Node = (0, 0)

# 15
small_cave: list[list[Risk]] = lines
small_cave_graph = generate_graph(small_cave)
small_cave_exit: Node = (len(small_cave[0]) - 1, len(small_cave) - 1)
print(min_risk(small_cave_graph, cave_entry, small_cave_exit))

# 15b
large_cave: list[list[Risk]] = []
for tile_y in range(5):
    for line in lines:
        row: list[list[Risk]] = []
        for tile_x in range(5):
            row.append(
                [
                    risk if (risk := initial_risk + tile_y + tile_x) == 9 else risk % 9
                    for initial_risk in line
                ]
            )
        large_cave.append(list(chain(*row)))

large_cave_graph = generate_graph(large_cave)
large_cave_exit: Node = (len(large_cave[0]) - 1, len(large_cave) - 1)
print(min_risk(large_cave_graph, cave_entry, large_cave_exit))
