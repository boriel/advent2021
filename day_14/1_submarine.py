from collections import Counter

data = open('input.txt').read()

template, lines = data.strip().split('\n\n')
lines = lines.split('\n')
rules = {x: y for x, y in (line.split(' -> ') for line in lines)}


def evolve(template, rules):
    positions = []
    for k, v in rules.items():
        for i in range(len(template)):
            if template[i:i+len(k)] == k:
                positions.append((i, v))

    result = list(template)
    for i, (k, v) in enumerate(sorted(positions, key=lambda x: x[0]), start=1):
        result.insert(k + i, v)

    return ''.join(result)


for i in range(10):
    template = evolve(template, rules)

c = Counter(template)
print(c.most_common(len(c)))
print(c.most_common(1)[0][1] - c.most_common(len(c))[-1][1])
