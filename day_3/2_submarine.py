from collections import Counter

data = [x.strip() for x in open("input.txt")]
o2 = data
co2 = data

o2_prefix = ""
co2_prefix = ""
i = 0

while i < len(data[0]):
    c = Counter(x[i] for x in o2)
    if c["0"] == c["1"]:
        o2_prefix += "1"
    else:
        o2_prefix += c.most_common(1)[0][0]
    o2 = [x for x in o2 if x.startswith(o2_prefix)]

    c = Counter(x[i] for x in co2)
    if c["0"] == c["1"]:
        co2_prefix += "0"
    else:
        co2_prefix += c.most_common(2)[-1][0]

    co2 = [x for x in co2 if x.startswith(co2_prefix)]
    i += 1

print(o2_prefix + '\n' + co2_prefix)
print(int(o2_prefix, 2) * int(co2_prefix, 2))