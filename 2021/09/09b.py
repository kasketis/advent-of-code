from __future__ import annotations

import math
import operator
from collections import Counter


def traverse_and_tag(map_loc: tuple[int, int], tag_id: int) -> bool:
    x, y = map_loc
    if 0 <= x < len(caves_map[0]) and 0 <= y < len(caves_map):
        not_wall = caves_map[y][x]
        untagged = caves_map[y][x] is True
        if not_wall and untagged:
            caves_map[y][x] = tag_id  # tag
            adjacent_rel_loc = (0, -1), (1, 0), (0, 1), (-1, 0)
            adj_indexes = [
                tuple(map(operator.add, map_loc, rel_loc))
                for rel_loc in adjacent_rel_loc
            ]
            for adj_x, adj_y in adj_indexes:
                traverse_and_tag((adj_x, adj_y), tag_id)
            return True
    return False


with open("input.txt") as f:
    lines = list(map(lambda x: list(x), f.read().splitlines()))

# mark walls as False
caves_map: list[list[bool | int]] = [
    [int(lines[y][x]) != 9 for x in range(len(lines[0]))] for y in range(len(lines))
]

# tag basins
basin_id = 0
for y in range(len(caves_map)):
    for x in range(len(caves_map[0])):
        if traverse_and_tag((x, y), basin_id):
            basin_id += 1

# filter out walls
basin_groups = [point for row in caves_map for point in row if point is not False]

largest_basins = [size for _, size in Counter(basin_groups).most_common()[:3]]
print(math.prod(largest_basins))
