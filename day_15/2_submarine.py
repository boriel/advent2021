N=5
data = open("input.txt").read()
board = [[1 + (i + j + int(x) - 1) % 9 for i in range(N) for x in line] for j in range(N) for line in data.strip().split("\n")]


def converge(world, board):
    pending = set()
    maxy = len(board) - 1
    maxx = len(board[0]) - 1

    for y in range(maxy):
        for x in range(maxx):
            pending.add((x, y))

    while pending:
        x, y = pending.pop()
        if not (0 <= x <= maxy) or not (0 <= y <= maxy):
            continue

        if (x, y) == (0, 0):
            risk = 0
        else:
            rN = world[y - 1][x] if y > 0 else None
            rS = world[y + 1][x] if y < maxy else None
            rE = world[y][x + 1] if x < maxx else None
            rW = world[y][x - 1] if x > 0 else None
            risk = board[y][x] + min(x for x in (rN, rS, rE, rW) if x is not None)

        if risk != world[y][x]:
            world[y][x] = risk
            pending.add((x + 1, y))
            pending.add((x - 1, y))
            pending.add((x, y + 1))
            pending.add((x, y - 1))


world = [[0 for x in line] for line in board]
converge(world, board)
print(world[-1][-1])
