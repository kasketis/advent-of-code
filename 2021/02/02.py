from collections import defaultdict

with open("input.txt") as f:
    lines = map(lambda x: x.split(), f.readlines())

c = defaultdict(int)
for ins, units in lines:
    c[ins] += int(units)

# alternative
# c = Counter(chain(*((ins,) * int(units) for ins, units in lines)))

print((c["down"] - c["up"]) * c["forward"])



