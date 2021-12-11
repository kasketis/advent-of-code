from __future__ import annotations

import sys
from itertools import chain

ENERGY_FLASH_THRESHOLD = 9
FLASHED_TAG = -sys.maxsize


def adjacents(x: int, bound_x: int, bound_y: int) -> set[int]:
    right_adj = {-bound_x, -bound_x + 1, 1, bound_x, bound_x + 1}
    left_adj = {-bound_x - 1, -bound_x, -1, bound_x - 1, bound_x}
    if x % bound_x == 0:  # left bound
        rel_xs = right_adj
    elif (x + 1) % bound_x == 0:  # right bound
        rel_xs = left_adj
    else:  # middle
        rel_xs = right_adj | left_adj
    return {x + rel_x for rel_x in rel_xs if 0 <= x + rel_x < bound_y}


with open("input.txt") as f:
    lines = list(map(lambda x: [int(i) for i in x], f.read().splitlines()))
line_bound = len(lines[0])
dumbos = list(chain(*lines))

step = 0
while sum(dumbos) != 0:
    # step 1 - increase energy
    dumbos = [energy + 1 for energy in dumbos]

    # step 2 - traverse and flash
    while max(dumbos) > ENERGY_FLASH_THRESHOLD:
        to_flash = (
            index
            for index, energy in enumerate(dumbos)
            if energy > ENERGY_FLASH_THRESHOLD
        )
        for index in to_flash:
            dumbos[index] = FLASHED_TAG  # flashed
            for adj_index in adjacents(index, line_bound, len(dumbos)):
                if dumbos[adj_index] != FLASHED_TAG:
                    dumbos[adj_index] += 1

    # step 3 - reset
    dumbos = [0 if energy == FLASHED_TAG else energy for energy in dumbos]

    step += 1
print(step)
