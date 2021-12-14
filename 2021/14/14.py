from collections import Counter

with open("input.txt") as f:
    lines = list(map(lambda x: x.split("\n"), f.read().split("\n\n")))
polymer: str = lines[0][0]
rules: dict[str, str] = dict(rule.split(" -> ") for rule in lines[1])

for step in range(10):
    step_polymer: list[str] = []
    for index, el in enumerate(polymer):
        step_polymer.append(el)
        if (index < len(polymer) - 1) and (
            pol_element := rules.get(el + polymer[index + 1])
        ):
            step_polymer.append(pol_element)
    polymer = "".join(step_polymer)

most_common = Counter(polymer).most_common()
print(most_common[0][1] - most_common[-1][1])
