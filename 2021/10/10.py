MAP = {")": "(", "]": "[", "}": "{", ">": "<"}
SCORE_MAP = {")": 3, "]": 57, "}": 1197, ">": 25137}

with open("input.txt") as f:
    lines = f.read().splitlines()

score = 0
for line in lines:
    queue = []
    for char in line:
        if not MAP.get(char):
            queue.append(char)
        elif MAP[char] == queue[-1]:
            queue.pop()
        else:
            score += SCORE_MAP[char]
            break
print(score)
