from __future__ import annotations

import re
from dataclasses import dataclass
from itertools import chain


@dataclass(frozen=True)
class Board:
    nums: list[list[int]]
    combos: list[list[int]]

    def bingo(self, called_nums: list[int]) -> bool:
        for combo in self.combos:
            if set(combo) < set(called_nums):
                return True
        return False

    def unmatched_sum(self, called_nums: list[int]) -> int:
        return sum(num for num in list(chain(*self.nums)) if num not in called_nums)

    @classmethod
    def from_txt(cls, txt: str) -> Board:
        board_nums = [
            list(map(int, re.findall(r"\d+", row))) for row in txt.split("\n")
        ]
        board_combos = board_nums + list(map(list, zip(*board_nums)))
        return cls(board_nums, board_combos)


with open("input.txt") as f:
    draw_nums_lines, *board_lines = f.read().split("\n\n")
draw_nums = list(map(int, draw_nums_lines.split(",")))
boards = [Board.from_txt(line) for line in board_lines]


index = 5  # best case
while index < len(draw_nums):
    nums = draw_nums[:index]

    # 04
    for board in boards:
        if board.bingo(nums):
            print(board.unmatched_sum(nums) * nums[-1])
            index = len(draw_nums)
    index += 1

    # 04b
    for board_index, board in enumerate(boards):
        if board.bingo(nums):
            if len(boards) > 1:
                del boards[board_index]
            else:
                print(board.unmatched_sum(nums) * nums[-1])
                index = len(draw_nums)
    index += 1
