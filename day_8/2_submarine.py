code = lambda x: ''.join(sorted(x))


def guess_code(input_):
    codes = sorted([code(x) for x in input_.split() if x], key=lambda x: len(x))
    result = {codes[0]: "1", codes[1]: "7", codes[2]: "4", codes[-1]: "8"}
    seg = {}

    seg[0] = list(set(codes[1]).difference(codes[0]))[0]

    for c in codes:
        if len(c) == 6:
            subset = list(set(codes[0]).difference(c))
            if subset:
                result[c] = "6"
                seg[2] = list(subset)[0]
                seg[5] = list(set(codes[0]).difference([seg[2]]))[0]
                break

    for c in codes:
        if len(c) == 5:
            if seg[2] in c and seg[5] in c:
                result[c] = "3"
            elif seg[2] in c:
                result[c] = "2"
            else:
                result[c] = "5"

    rev = {int(v): k for k, v in result.items()}
    seg[4] = list(set(rev[2]).difference(rev[3]))[0]

    for c in codes:
        if len(c) == 6 and c not in result:
            if seg[4] in c:
                result[c] = "0"
            else:
                result[c] = "9"

    return result


total = 0
for line in open("input.txt"):
    left, right = (x.strip() for x in line.split('|'))
    right_codes = right.split()
    map_code = guess_code(left)
    total += int(''.join(map_code[code(x)] for x in right_codes))

print(total)
