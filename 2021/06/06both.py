from collections import deque
from collections import Counter

with open("input.txt") as f:
    lanternfishes = Counter(map(int, f.read().split(",")))


def total_lanternfishes(init_lanternfishes: Counter, after_days: int) -> int:
    c = {i: init_lanternfishes[i] for i in range(9)}
    for day in range(after_days):
        rotated_values = deque(c.values())
        rotated_values.rotate(-1)
        c = {k: v for k, v in zip(c, rotated_values)}
        c[6] += c[8]
    return sum(c.values())

# 06
print(total_lanternfishes(init_lanternfishes=lanternfishes, after_days=80))

# 06b
print(total_lanternfishes(init_lanternfishes=lanternfishes, after_days=256))
