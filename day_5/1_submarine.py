from collections import defaultdict
table = defaultdict(int)

max_x = max_y = 0

for line in open("input.txt"):
    start, end = [x.strip() for x in line.split("->")]
    x1, y1 = [int(x) for x in start.split(",")]
    x2, y2 = [int(x) for x in end.split(",")]

    if x1 > max_x:
        max_x = x1
    if x2 > max_x:
        max_x = x2
    if y1 > max_y:
        max_y = y1
    if y2 > max_y:
        max_y = y2

    if x1 != x2 and y1 != y2:
        continue

    if x1 == x2:
        if y1 > y2:
            y1, y2 = y2, y1
        for y in range(y1, y2 + 1):
            table[(x1, y)] += 1
    else:
        if x1 > x2:
            x1, x2 = x2, x1
        for x in range(x1, x2 + 1):
            table[(x, y1)] += 1

print(sum(1 for x in table.values() if x > 1))
# for y in range(max_y + 1):
#     for x in range(max_x + 1):
#         if table[(x, y)]:
#             print(table[(x, y)], end="")
#         else:
#             print(".", end="")
#     print()
