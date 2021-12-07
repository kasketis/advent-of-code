from statistics import median

with open("input.txt") as f:
    crabs = list(map(int, f.read().split(",")))

m = median(crabs)
min_fuel = sum(abs(crab - m) for crab in crabs)
print(min_fuel)
