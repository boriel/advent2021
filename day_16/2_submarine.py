L = 4
hex2bin = {x: "".join(str((int(x, 16) >> i) & 1) for i in range(L - 1, -1, -1)) for x in "0123456789ABCDEF"}
data = open("input.txt").read().strip()


def hex_to_bin(hex_):
    return list("".join(hex2bin[c] for c in hex_))


def lex(data, n):
    result = int("0" + "".join(data[:n]), 2)
    for i in range(n):
        data.pop(0)

    return result


def parse_literal(data):
    s = ""

    bit = 1
    while bit:
        bit = lex(data, 1)
        s += "".join(data[:L])
        lex(data, L)

    lex(data, len(s) % L)
    return int("0" + s, 2)


def parse(data):
    version = lex(data, 3)
    type_id = lex(data, 3)

    if type_id == 4:
        literal = parse_literal(data)
        return literal

    if lex(data, 1):
        num_subpackets = lex(data, 11)
        subpackets = [parse(data) for i in range(num_subpackets)]
    else:
        tot_length = lex(data, 15)
        sub_data = data[:tot_length]
        lex(data, tot_length)
        subpackets = []

        while sub_data:
            subpackets.append(parse(sub_data))

    dispatch = {
        0: sum,
        1: lambda x: x[0] if len(x) == 1 else x[0] * dispatch[1](x[1:]),
        2: min,
        3: max,
        5: lambda x: int(x[0] > x[1]),
        6: lambda x: int(x[0] < x[1]),
        7: lambda x: int(x[0] == x[1])
    }

    return dispatch[type_id](subpackets)


print(parse(hex_to_bin(data)))
