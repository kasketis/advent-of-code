from __future__ import annotations

MAP = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}


def signal_to_digit(signal: str) -> int:
    signal = "".join(sorted(signal))
    for k, v in MAP.items():
        if v == signal:
            return k
    raise RuntimeError(f"Failed to map {signal=}")


def char_freq_map(digits_map: dict[int, str]) -> dict[str, tuple[set, int]]:
    map_ = {}
    for c in "abcdefg":
        nums = [len(signal) for signal in digits_map.values() if c in signal]
        map_[c] = (set(nums), len(nums))
    return map_


with open("input.txt") as f:
    lines = f.read().splitlines()

output_sum = 0
for line in lines:
    patterns, output = (x.split() for x in line.split("|"))
    patterns_map = dict(zip(range(len(MAP)+1), patterns))

    char_map = {
        k2: k1
        for k1, v1 in char_freq_map(MAP).items()
        for k2, v2 in char_freq_map(patterns_map).items()
        if v1 == v2
    }

    decoded_signals = [
        signal.translate(signal.maketrans(char_map)) for signal in output
    ]
    output_sum += int(
        "".join(
            [str(signal_to_digit(decoded_signal)) for decoded_signal in decoded_signals]
        )
    )
print(output_sum)
