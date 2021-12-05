x = 0
y = 0
aim = 0

for line in open("input.txt"):
    command, val = line.split()
    value = int(val)
    if command == "up":
        value = -value

    if command == "forward":
        x += value
        y += aim * value
    else:
        aim += value

print(x, y, x * y)
