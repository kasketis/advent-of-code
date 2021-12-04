from collections import Counter


def filter_(lines_: list[list[str]], *, eq_bit: int) -> int:
    position = 0
    while len(lines_) > 1:
        columns = list(zip(*lines_))
        bit_freq = Counter(columns[position]).most_common()
        chosen_bit = (
            str(eq_bit) if bit_freq[0][1] == bit_freq[1][1] else bit_freq[1 - eq_bit][0]
        )
        lines_ = [
            lines_[index]
            for index, bit in enumerate(columns[position])
            if bit == chosen_bit
        ]
        position += 1
    return int("".join(lines_[0]), 2)


with open("input.txt") as f:
    lines = list(map(lambda x: list(x), f.read().split()))
oxygen = filter_(lines, eq_bit=1)
co2 = filter_(lines, eq_bit=0)
print(oxygen * co2)
