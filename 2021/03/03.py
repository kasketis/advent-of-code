from collections import Counter

with open("input.txt") as f:
    lines = map(lambda x: list(x), f.read().split())
column_counters = [Counter(column) for column in list(zip(*lines))]
gamma_bits, epsilon_bits = zip(
    *[((cc.most_common()[0][0]), cc.most_common()[1][0]) for cc in column_counters]
)
gamma = int("".join(gamma_bits), 2)
epsilon = int("".join(epsilon_bits), 2)
print(gamma * epsilon)
