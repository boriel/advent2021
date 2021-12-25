data = open("input.txt").read()
status = [list(x) for x in data.strip().split("\n")]


def evolve(status):
    status1 = []
    for line in status:
        line1 = list(line)
        status1.append(line1)

        for i, c in enumerate(line):
            if line[i - 1] == ">" and c == ".":
                line1[i - 1] = "."
                line1[i] = ">"

    status = status1
    status1 = [list(x) for x in status]

    for i, line in enumerate(status):
        for j, c in enumerate(line):
            if c == "." and status[i - 1][j] == "v":
                status1[i][j] = "v"
                status1[i - 1][j] = "."

    return status1


prev = None
count = 0

while prev != status:
    prev = status
    status = evolve(status)
    count += 1

print(count)
