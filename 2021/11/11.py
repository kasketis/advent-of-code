from __future__ import annotations

import sys
from itertools import chain

FLASH_ENERGY_THRESHOLD = 9
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
flat_line = list(chain(*lines))

flashes = 0
step = 0
while step < 100:
    # step 1 - increase energy
    flat_line = [x + 1 for x in flat_line]

    # step 2 - traverse and flash
    while max(flat_line) > FLASH_ENERGY_THRESHOLD:
        to_flash = (
            index
            for index, energy in enumerate(flat_line)
            if energy > FLASH_ENERGY_THRESHOLD
        )
        for flash_x in to_flash:
            flat_line[flash_x] = FLASHED_TAG  # flashed
            flashes += 1
            for adj_x in adjacents(flash_x, line_bound, len(flat_line)):
                if flat_line[adj_x] != FLASHED_TAG:
                    flat_line[adj_x] += 1

    # step 3 - reset
    flat_line = [0 if x == FLASHED_TAG else x for x in flat_line]

    step += 1
print(flashes)
