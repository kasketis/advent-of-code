from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass


@dataclass(frozen=True)
class Cuboid:
    on: bool
    x: range
    y: range
    z: range

    def find_intersections(self, cuboids: Counter[Cuboid]) -> Counter:
        intersected_cuboids: Counter[Cuboid] = Counter()
        for existing_cuboid, count in cuboids.items():
            if intersected := self._intersect(existing_cuboid):
                intersected_cuboids[intersected] -= count
        return intersected_cuboids

    def _intersect(self, other: Cuboid) -> Cuboid | None:
        x_start = max(self.x.start, other.x.start)
        x_stop = min(self.x.stop, other.x.stop)
        y_start = max(self.y.start, other.y.start)
        y_stop = min(self.y.stop, other.y.stop)
        z_start = max(self.z.start, other.z.start)
        z_stop = min(self.z.stop, other.z.stop)
        return (
            Cuboid(
                self.on and other.on,
                range(x_start, x_stop),
                range(y_start, y_stop),
                range(z_start, z_stop),
            )
            if x_start <= x_stop and y_start <= y_stop and z_start <= z_stop
            else None
        )

    def volume(self) -> int:
        return (
            (self.x.stop - self.x.start)
            * (self.y.stop - self.y.start)
            * (self.z.stop - self.z.start)
        )

    @classmethod
    def from_txt(cls, txt: str) -> Cuboid | None:
        pattern = re.compile(
            r"^(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)$"
        )
        if matches := pattern.match(txt):
            switch, *xyz = matches.groups()
            x1, x2, y1, y2, z1, z2 = map(int, xyz)
            return cls(
                switch == "on",
                range(min(x1, x2), max(x1, x2) + 1),
                range(min(y1, y2), max(y1, y2) + 1),
                range(min(z1, z2), max(z1, z2) + 1),
            )
        return None


with open("input.txt") as f:
    lines = f.read().splitlines()

c: Counter[Cuboid] = Counter()
for line in lines:
    if cuboid := Cuboid.from_txt(line):
        c.update(cuboid.find_intersections(c))
        if cuboid.on:
            c[cuboid] += 1

print(sum(cuboid.volume() * count for cuboid, count in c.items()))
