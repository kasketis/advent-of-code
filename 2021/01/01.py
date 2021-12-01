with open("input.txt") as f:
    lines = list(map(int, f.readlines()))
print(sum(a < b for a, b in zip(lines, lines[1:])))
