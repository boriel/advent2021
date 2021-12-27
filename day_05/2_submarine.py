from collections import defaultdict
table = defaultdict(int)

max_x = max_y = 0

for line in open("input.txt"):
    start, end = [x.strip() for x in line.split("->")]
    x1, y1 = [int(x) for x in start.split(",")]
    x2, y2 = [int(x) for x in end.split(",")]

    max_x = max(x1, x2)
    max_y = max(y1, y2)

    dx = x2 - x1
    dy = y2 - y1

    if dx != 0 and dy != 0 and abs(dx) != abs(dy):
        continue

    sx = 0 if dx == 0 else 1 if dx > 0 else -1
    sy = 0 if dy == 0 else 1 if dy > 0 else -1

    x0, y0 = x1, y1
    while (x0, y0) != (x2 + sx, y2 + sy):
        table[(x0, y0)] += 1
        x0 += sx
        y0 += sy


print(sum(1 for x in table.values() if x > 1))
# for y in range(max_y + 1):
#     for x in range(max_x + 1):
#         if table[(x, y)]:
#             print(table[(x, y)], end="")
#         else:
#             print(".", end="")
#     print()
