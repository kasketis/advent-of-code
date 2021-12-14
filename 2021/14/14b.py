from collections import Counter

with open("input.txt") as f:
    lines = list(map(lambda x: x.split("\n"), f.read().split("\n\n")))
polymer: str = lines[0][0]
rules: dict[str, str] = dict(rule.split(" -> ") for rule in lines[1])

polymer_counter: dict[tuple[str, str], int] = Counter(zip(polymer, polymer[1:]))
for step in range(40):
    step_counter: dict[tuple[str, str], int] = Counter()
    for (el_a, el_b), num in polymer_counter.items():
        if pol_element := rules.get(el_a + el_b):
            step_counter[(el_a, pol_element)] += num
            step_counter[(pol_element, el_b)] += num
    polymer_counter = step_counter

c = Counter({polymer[-1]: 1})
for (el_a, el_b), num in polymer_counter.items():
    c[el_a] += num
    c[el_b] += num
most_common = c.most_common()
print(most_common[0][1] // 2 - most_common[-1][1] // 2)
