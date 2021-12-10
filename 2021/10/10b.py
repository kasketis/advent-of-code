from statistics import median

MAP = {")": "(", "]": "[", "}": "{", ">": "<"}
REV_SCORE_MAP = {"(": 1, "[": 2, "{": 3, "<": 4}

with open("input.txt") as f:
    lines = f.read().splitlines()

scores = []
for line in lines:
    queue = []
    corrupted = False
    for char in line:
        if not MAP.get(char):
            queue.append(char)
        elif MAP[char] == queue[-1]:
            queue.pop()
        else:
            corrupted = True
            break
    if not corrupted:
        line_score = 0
        for char in reversed(queue):
            line_score = (line_score * 5) + REV_SCORE_MAP[char]
        scores.append(line_score)
print(median(scores))
