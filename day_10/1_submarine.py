lines = [x.strip() for x in open("input.txt").readlines()]

def parse_line(line):
    cl = {"}": "{", "]": "[", ")": "(", ">": "<"}
    stack = []
    for c in line:
        if c in cl:
            if stack[-1] != cl[c]:
                return c
            stack.pop()
        else:
            stack.append(c)


values = {")": 3, "]": 57, "}": 1197, ">": 25137}
print(sum(values.get(parse_line(line), 0) for line in lines))
