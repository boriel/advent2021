data = open("input.txt").read()


def lim(x):
    return -L if x < -L else L if x > L else x


def llim(c):
    if all(x < -L for x in c) or all(x > L for x in c):
        return 0, 0

    return lim(c[0]), lim(c[1]) + 1


L = 50
W = 2 * L + 1
reactor = [[[0] * W for i in range(W)] for j in range(W)]

for line in data.strip().split("\n"):
    status, limits = line.split()
    s = int(status == "on")
    cuboid = tuple(tuple(int(i) for i in x[2:].split("..")) for x in limits.split(","))

    for x in range(*llim(cuboid[0])):
        for y in range(*llim(cuboid[1])):
            for z in range(*llim(cuboid[2])):
                reactor[z][y][x] = s


print(sum(sum(sum(line) for line in plane) for plane in reactor))
