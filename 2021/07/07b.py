import sys

with open("input.txt") as f:
    crabs = sorted(list(map(int, f.read().split(","))))

min_fuel = sys.maxsize
for x in range(crabs[0], crabs[-1] + 1):
    fuel = sum((abs(crab - x) * (abs(crab - x) + 1) // 2) for crab in crabs)
    if fuel < min_fuel:
        min_fuel = fuel
    else:
        break
print(min_fuel)
