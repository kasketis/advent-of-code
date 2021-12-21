from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, product
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Iterator

Position = tuple[int, int, int]


@dataclass
class Scanner:
    id_: int
    beacons: set[Position]
    position: tuple[int, int, int] = (0, 0, 0)

    def beacon_positions_combos(self) -> list[set[Position]]:
        facings = [
            lambda x, y, z: (x, y, z),
            lambda x, y, z: (x, y, -z),
            lambda x, y, z: (x, -y, z),
            lambda x, y, z: (x, -y, -z),
            lambda x, y, z: (-x, y, z),
            lambda x, y, z: (-x, -y, z),
            lambda x, y, z: (-x, -y, -z),
            lambda x, y, z: (-x, y, -z),
        ]

        rotations = [
            lambda x, y, z: (x, y, z),
            lambda x, y, z: (x, z, y),
            lambda x, y, z: (y, x, z),
            lambda x, y, z: (y, z, x),
            lambda x, y, z: (z, x, y),
            lambda x, y, z: (z, y, x),
        ]

        positions_combos = []
        for facing, rotation in product(facings, rotations):
            positions_combos.append(
                {facing(*rotation(*beacon)) for beacon in self.beacons}
            )
        return positions_combos

    @classmethod
    def from_txt(cls, txt: str, id_: int) -> Scanner:
        beacons_txt = txt.splitlines()[1:]
        beacons: set[Position] = set()
        for beacon_txt in beacons_txt:
            beacons.add(Position(map(int, beacon_txt.split(","))))
        return cls(id_, beacons)


with open("input.txt") as f:
    lines = f.read().split("\n\n")

scanners = []
for index, line in enumerate(lines):
    scanners.append(Scanner.from_txt(line, index))


def viewpoint(base: Scanner, to: Scanner) -> Iterator[tuple[set[Position], Position]]:
    for positions_combo in to.beacon_positions_combos():
        for x1, y1, z1 in base.beacons:
            for x2, y2, z2 in positions_combo:
                dx, dy, dz = x1 - x2, y1 - y2, z1 - z2
                absolute_beacon_positions = {
                    (x + dx, y + dy, z + dz) for x, y, z in positions_combo
                }
                yield absolute_beacon_positions, (dx, dy, dz)


checked_scanner_ids = set()
paired_scanner_ids = {0}
while len(paired_scanner_ids) != len(scanners):
    paired_scanners = [
        scanner
        for scanner in scanners
        if scanner.id_ in paired_scanner_ids and scanner.id_ not in checked_scanner_ids
    ]
    unpaired_scanners = [
        scanner for scanner in scanners if scanner.id_ not in paired_scanner_ids
    ]
    for paired_scanner in paired_scanners:
        checked_scanner_ids.add(paired_scanner.id_)
        for unpaired_scanner in unpaired_scanners:
            for beacon_positions, scanner_position in viewpoint(
                base=paired_scanner, to=unpaired_scanner
            ):
                if len(paired_scanner.beacons.intersection(beacon_positions)) >= 12:
                    unpaired_scanner.beacons = beacon_positions
                    unpaired_scanner.position = scanner_position
                    paired_scanner_ids.add(unpaired_scanner.id_)
                    break

# 19
total_beacons: set[Position] = set()
for scanner in scanners:
    total_beacons |= scanner.beacons
print(len(total_beacons))


# 19b
max_manhattan_distance = 0
for scanner1, scanner2 in combinations(scanners, 2):
    x1, y1, z1 = scanner1.position
    x2, y2, z2 = scanner2.position
    max_manhattan_distance = max(
        abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2), max_manhattan_distance
    )
print(max_manhattan_distance)
