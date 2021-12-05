from collections import Counter

data = []

for i, line in enumerate(open("input.txt")):
    line = line.strip()
    if i == 0:
        data = [Counter() for _ in range(len(line))]

    for j, digit in enumerate(line):
        data[j].update([digit])

alpha = ''.join(str(x.most_common(1)[0][0]) for x in data)
beta = ''.join(str(x.most_common(2)[-1][0]) for x in data)

print(int(alpha, 2) * int(beta, 2))
