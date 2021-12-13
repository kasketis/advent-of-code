from __future__ import annotations

from dataclasses import dataclass


@dataclass(unsafe_hash=True)
class OrigamiPoint:
    x: int
    y: int

    def fold(self, instruction: str) -> None:
        axis, num = instruction.split("=")
        if self.__dict__[axis] > int(num):
            self.__dict__[axis] -= 2 * (self.__dict__[axis] - int(num))

    @classmethod
    def from_txt(cls, txt: str) -> OrigamiPoint:
        return cls(*map(int, txt.split(",")))


with open("input.txt") as f:
    points, instructions = map(lambda x: x.split("\n"), f.read().split("\n\n"))

origami_points: list[OrigamiPoint] = [OrigamiPoint.from_txt(point) for point in points]
origami_instructions: list[str] = [ins.split()[-1] for ins in instructions if ins]

# 13a
for point in origami_points:
    point.fold(origami_instructions[0])
print(len(set(origami_points)))

# 13b
for ins in origami_instructions[1:]:
    for point in origami_points:
        point.fold(ins)

max_x = max_y = 0
for origami_point in origami_points:
    max_x = max(origami_point.x, max_x)
    max_y = max(origami_point.y, max_y)
board = [[" "] * (max_x + 1) for _ in range(max_y + 1)]
for origami_point in origami_points:
    board[origami_point.y][origami_point.x] = "#"
for _ in board:
    print("".join(_))
