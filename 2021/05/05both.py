import re
from collections import Counter
from itertools import chain

with open("input.txt") as f:
    lines = f.read().splitlines()
pattern = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")
hydro_vents_edges = [
    tuple(map(int, matches.groups()))
    for line in lines
    if (matches := pattern.match(line))
]

# 05
hydro_vents_points: list[list[tuple[int, int]]] = []
for x1, y1, x2, y2 in hydro_vents_edges:
    if x1 == x2:
        hydro_vents_points.append(
            [(x1, min(y1, y2) + i) for i in range(abs(y1 - y2) + 1)]
        )
    elif y1 == y2:
        hydro_vents_points.append(
            [(min(x1, x2) + i, y1) for i in range(abs(x1 - x2) + 1)]
        )
overlapping_points = sum(
    freq > 1 for _, freq in Counter(chain(*hydro_vents_points)).most_common()
)
print(overlapping_points)

# 05b
hydro_vents_points: list[list[tuple[int, int]]] = []
for x1, y1, x2, y2 in hydro_vents_edges:
    if x1 == x2:
        hydro_vents_points.append(
            [(x1, min(y1, y2) + i) for i in range(abs(y1 - y2) + 1)]
        )
    elif y1 == y2:
        hydro_vents_points.append(
            [(min(x1, x2) + i, y1) for i in range(abs(x1 - x2) + 1)]
        )
    elif abs(x1 - x2) == abs(y1 - y2):
        xs = [x1 + i if x2 >= x1 else x1 - i for i in range(abs(x1 - x2) + 1)]
        ys = [y1 + i if y2 >= y1 else y1 - i for i in range(abs(y1 - y2) + 1)]
        hydro_vents_points.append([(x, y) for x, y in zip(xs, ys)])
overlapping_points = sum(
    freq > 1 for _, freq in Counter(chain(*hydro_vents_points)).most_common()
)
print(overlapping_points)
