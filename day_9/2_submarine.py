M = 'Z'
lines = [x.strip() for x in open('input.txt').readlines()]
maxx, maxy = len(lines[0]) - 1, len(lines) - 1
pending = []

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        up = M if i == 0 else lines[i - 1][j]
        down = M if i == maxy else lines[i + 1][j]
        left = M if j == 0 else lines[i][j - 1]
        right = M if j == maxx else lines[i][j + 1]

        if c < min(up, down, left, right):
            pending.append((i, j))


def basin_size(i, j):
    size = 0
    pending = [(i, j)]
    visited = set()

    while pending:
        i, j = pending.pop()
        cval = lines[i][j]
        if cval == '9' or (i, j) in visited:
            continue
        visited.add((i, j))

        size += 1
        if i > 0 and lines[i - 1][j] > cval:
            pending.append((i - 1, j))
        if i < maxy and lines[i + 1][j] > cval:
            pending.append((i + 1, j))
        if j > 0 and lines[i][j - 1] > cval:
            pending.append((i, j - 1))
        if j < maxx and lines[i][j + 1] > cval:
            pending.append((i, j + 1))

    return size


basins_sizes = []

while pending:
    basins_sizes.append(basin_size(*pending.pop()))
    basins_sizes = sorted(basins_sizes)[-3:]

print(basins_sizes[0] * basins_sizes[1] * basins_sizes[2])
