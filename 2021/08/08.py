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

with open("input.txt") as f:
    lines = f.read().splitlines()

search_signal_lengths = set(map(len, {MAP[1], MAP[4], MAP[7], MAP[8]}))
matches = 0
for line in lines:
    _, output = (x.split() for x in line.split("|"))
    matches += sum(len(signal) in search_signal_lengths for signal in output)
print(matches)
