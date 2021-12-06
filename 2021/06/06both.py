from collections import Counter, deque

with open("input.txt") as f:
    lanternfishes = Counter(map(int, f.read().split(",")))


def total_lanternfishes(init_lanternfishes: Counter, after_days: int) -> int:
    day_counter = {i: init_lanternfishes[i] for i in range(9)}
    for day in range(after_days):
        next_day_counter = deque(day_counter.values())
        next_day_counter.rotate(-1)
        day_counter = {k: v for k, v in zip(day_counter, next_day_counter)}
        day_counter[6] += day_counter[8]
    return sum(day_counter.values())


# 06
print(total_lanternfishes(init_lanternfishes=lanternfishes, after_days=80))

# 06b
print(total_lanternfishes(init_lanternfishes=lanternfishes, after_days=256))
