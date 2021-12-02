with open("input.txt") as f:
    lines = map(lambda x: x.split(), f.readlines())

aim = horizontal = depth = 0
for ins, units in lines:
    units = int(units)
    if ins == "forward":
        horizontal += units
        depth += units * aim
    else:
        aim += units if ins == "down" else units * -1
print(horizontal * depth)
