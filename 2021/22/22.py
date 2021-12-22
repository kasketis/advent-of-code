import re
from itertools import product

with open("input.txt") as f:
    lines = f.read().splitlines()

pattern = re.compile(
    r"^(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)$"
)
on = set()
for line in lines:
    if matches := pattern.match(line):
        switch, *xyz = matches.groups()
        x1, x2, y1, y2, z1, z2 = map(int, xyz)
        cuboid = set(
            product(
                range(max(x1, -50), min(x2, 50) + 1),
                range(max(y1, -50), min(y2, 50) + 1),
                range(max(z1, -50), min(z2, 50) + 1),
            )
        )
        if switch == "on":
            on |= cuboid
        else:
            on -= cuboid

print(len(on))
