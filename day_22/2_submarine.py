data = open("input.txt").read()


def volume(cuboid):
    f = lambda c: 1 if not c else (abs(c[0][1] - c[0][0]) + 1) * f(c[1:])
    return f(cuboid) if cuboid else 0


def is_valid(cuboid):
    return all(c[0] <= c[1] for c in cuboid)


def intersection(ca, cb):
    result = tuple((max(a[0], b[0]), min(a[1], b[1])) for a, b in zip(ca, cb))
    return result if is_valid(result) else None


def split(ca, cb):
    inter = intersection(ca, cb)
    if not inter:
        return [ca, cb]

    result = []
    (xa1, xa2), (ya1, ya2), (za1, za2) = ca
    (xb1, xb2), (yb1, yb2), (zb1, zb2) = cb

    xx = min(xa1, xb1), max(xa1, xb1), min(xa2, xb2) + 1, max(xa2, xb2) + 1
    yy = min(ya1, yb1), max(ya1, yb1), min(ya2, yb2) + 1, max(ya2, yb2) + 1
    zz = min(za1, zb1), max(za1, zb1), min(za2, zb2) + 1, max(za2, zb2) + 1

    for k in range(3):
        for j in range(3):
            for i in range(3):
                new_c = ((xx[i], xx[i + 1] - 1), (yy[j], yy[j + 1] - 1), (zz[k], zz[k + 1] - 1))
                if is_in(new_c, ca) or is_in(new_c, cb):
                    result.append(new_c)

    return [x for x in result if is_valid(x)]


def is_in(c1, c2):
    return intersection(c1, c2) == c1


def union(cuboids, cuboid):
    result = set()
    current_set = set(list(cuboids) + [cuboid])

    while current_set:
        new_c = current_set.pop()
        if all(not intersection(new_c, c) for c in current_set):
            result.add(new_c)
            continue

        for i, cur_c in enumerate(current_set):
            if intersection(new_c, cur_c):
                current_set.remove(cur_c)
                current_set.update(split(new_c, cur_c))
                break

    return result


cuboids = []

for line_num, line in enumerate(data.strip().split("\n")):
    print(line_num, line)
    status, limits = line.split()
    cuboid = tuple(tuple(int(i) for i in x[2:].split("..")) for x in limits.split(","))
    if status == "on" and any(is_in(cuboid, c) for c in cuboids):
        continue

    cuboids = [x for x in cuboids if not is_in(x, cuboid)]
    cuboids = [x for x in union(cuboids, cuboid) if not is_in(x, cuboid)]
    if status == "on":
        cuboids.append(cuboid)

print(sum(volume(c) for c in cuboids))
