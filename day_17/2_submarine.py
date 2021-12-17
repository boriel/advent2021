X, Y = [(119, 176), (-141, -84)]
tray = set()


def check_hit(vx, vy, X, Y):
    x, y = 0, 0
    maxy = 0
    maxx = X[1]
    hit = False

    while True:
        tray.add((x, y))
        maxy = max(maxy, y)
        maxx = max(maxx, x)
        if X[0] <= x <= X[1] and Y[0] <= y <= Y[1]:
            hit = True

        if x > X[1] or x + (vx * vx + vx) // 2 < X[0] or y < Y[0]:
            return hit, maxx, maxy

        x += vx
        y += vy
        vx = vx - 1 if vx > 0 else vx + 1 if vx < 0 else 0
        vy -= 1


def paint(maxx, maxy, X, Y):
    for y in range(maxy, Y[0] - 1, -1):
        for x in range(maxx + 1):
            if (x, y) == (0, 0):
                c = 'S'
            elif (x, y) in tray:
                c = '#'
            elif X[0] <= x <= X[1] and Y[0] <= y <= Y[1]:
                c = 'T'
            else:
                c = '.'
            print(c, end="")
        print()


def search(X, Y):
    tray.clear()
    count = 0
    for vx in range(1, X[1] + 1):
        for vy in range(-Y[0] + 1, Y[0] - 1, -1):
            hit, mx, my = check_hit(vx, vy, X, Y)
            if hit:
                count += 1

    return count


print(search(X, Y))
