lines = [x.strip() for x in open("input.txt").readlines()]


def parse_line(line):
    cl = {"}": "{", "]": "[", ")": "(", ">": "<"}
    values = {"(": 1, "[": 2, "{": 3, "<": 4}
    stack = []
    for c in line:
        if c in cl:
            if stack[-1] != cl[c]:
                return 0
            stack.pop()
        else:
            stack.append(c)

    total = 0
    while stack:
        total = total * 5 + values[stack.pop()]

    return total


scores = sorted(x for x in [parse_line(line) for line in lines] if x)
print(scores[len(scores) // 2])
