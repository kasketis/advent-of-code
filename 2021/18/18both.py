from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from itertools import permutations


@dataclass
class SnailFishNumber:
    value: int
    depth: int


def flatten(number: int | list[int], depth: int = 0) -> list[SnailFishNumber]:
    if isinstance(number, int):
        return [SnailFishNumber(value=number, depth=depth)]
    return flatten(number[0], depth + 1) + flatten(number[1], depth + 1)


def reduce(numbers: list[SnailFishNumber]) -> list[SnailFishNumber]:
    if to_explode := [
        (index, number) for index, number in enumerate(numbers) if number.depth > 4
    ]:
        (left_index, left_number), (right_index, right_number) = to_explode[:2]

        if left_index > 0:
            prev_number = numbers[left_index - 1]
            prev_number.value += left_number.value
            numbers[left_index - 1] = prev_number

        if right_index < len(numbers) - 1:
            next_number = numbers[right_index + 1]
            next_number.value += right_number.value
            numbers[right_index + 1] = next_number

        numbers = [
            number
            for index, number in enumerate(numbers)
            if index not in {left_index, right_index}
        ]
        numbers.insert(
            left_index, SnailFishNumber(value=0, depth=left_number.depth - 1)
        )
        return numbers

    if to_split := [
        (index, number) for index, number in enumerate(numbers) if number.value > 9
    ]:
        index, number = to_split[0]
        new_left_number = number.value // 2
        new_right_number = number.value - new_left_number
        numbers[index] = SnailFishNumber(value=new_left_number, depth=number.depth + 1)
        numbers.insert(
            index + 1, SnailFishNumber(value=new_right_number, depth=number.depth + 1)
        )

    return numbers


def magnitude(numbers_txt: tuple[str, ...]) -> int:
    numbers: list[SnailFishNumber] = flatten(eval(numbers_txt[0]))
    for number_txt in numbers_txt[1:]:
        numbers += flatten(eval(number_txt))
        for num in numbers:
            num.depth += 1

        while (reduced_numbers := reduce(deepcopy(numbers))) != numbers:
            numbers = reduced_numbers

    while len(numbers) > 1:
        prev_number: SnailFishNumber | None = None
        for index, cur_number in enumerate(numbers):
            if prev_number and prev_number.depth == cur_number.depth:
                numbers[index] = SnailFishNumber(
                    value=(3 * prev_number.value) + (2 * cur_number.value),
                    depth=cur_number.depth - 1,
                )
                del numbers[index - 1]
                break
            prev_number = cur_number

    return numbers[0].value


with open("input.txt") as f:
    lines = tuple(f.read().splitlines())

# 18
print(magnitude(lines))

# 18b
max_magnitude = 0
for perm in permutations(lines, 2):
    max_magnitude = max(magnitude(perm), max_magnitude)
print(max_magnitude)
