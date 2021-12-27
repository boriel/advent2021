M = 10
lines = [x.strip() for x in open('input.txt').readlines()]

total = 0
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        up = M if i == 0 else int(lines[i-1][j])
        down = M if i == len(lines)-1 else int(lines[i+1][j])
        left = M if j == 0 else int(lines[i][j-1])
        right = M if j == len(line)-1 else int(lines[i][j+1])
        cval = int(c)
        if cval < min(up, down, left, right):
            total += cval + 1

print(total)
