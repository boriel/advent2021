import functools

data = open("input.txt").read()
board = [[int(x) for x in line] for line in data.strip().split("\n")]


@functools.lru_cache
def find_min_risk(x, y):
    if (x, y) == (0, 0):
        return 0

    mx1 = find_min_risk(x - 1, y) if x > 0 else None
    my1 = find_min_risk(x, y - 1) if y > 0 else None
    return min(x for x in (mx1, my1) if x is not None) + board[y][x]


print(find_min_risk(len(board[0]) - 1, len(board) - 1))
