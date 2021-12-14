from collections import Counter, defaultdict

data = open('input.txt').read()
template, lines = data.strip().split('\n\n')
lines = lines.split('\n')
rules = {x: y for x, y in (line.split(' -> ') for line in lines)}
cache = defaultdict(Counter)


def evolve(code, rules, level=0):
    key = (code, level)
    if key in cache:
        return cache[key]

    if code not in rules or level == 0:
        cache[key] = Counter()
        return cache[key]

    letter = rules[code]
    cache[key] = evolve(code[0] + letter, rules, level - 1) + evolve(letter + code[1], rules, level - 1) + Counter(letter)
    return cache[key]


tot = Counter(template)
for i in range(len(template) - 1):
    tot += evolve(template[i: i + 2], rules, 40)

print(tot.most_common(1)[0][1] - tot.most_common(len(tot))[-1][1])
