import operator
import sys


def adjacents_height(
    map_loc: tuple[int, int], *, height_map: list[list[str]]
) -> set[int]:
    adjacent_rel_loc = (0, -1), (1, 0), (0, 1), (-1, 0)
    adj_indexes = [
        tuple(map(operator.add, map_loc, rel_loc)) for rel_loc in adjacent_rel_loc
    ]
    heights = set()
    for adj_x, adj_y in adj_indexes:
        heights.add(
            int(height_map[adj_y][adj_x])
            if 0 <= adj_x < len(height_map[0]) and 0 <= adj_y < len(height_map)
            else sys.maxsize
        )
    return heights


with open("input.txt") as f:
    lines = list(map(lambda x: list(x), f.read().splitlines()))

low_points = []
for y in range(len(lines)):
    for x in range(len(lines[0])):
        height = int(lines[y][x])
        if height < min(adjacents_height((x, y), height_map=lines)):
            low_points.append(height)
print(sum(low_points) + len(low_points))
