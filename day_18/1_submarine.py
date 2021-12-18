LB, RB = '[', ']'
CO = ','

data = open("input.txt").read()
lines = data.strip().split("\n")
number = [int(x) if x.isdecimal() else x for x in lines[0]]


class SnailNumber:
    def __init__(self, seq):
        self.seq = [int(x) if str(x).isdecimal() else x for x in seq]
        self.explode()
        self.split()

    def explode(self):
        seq = self.seq
        level = 0

        for i, c in enumerate(seq):
            if c == LB:
                level += 1
            elif c == RB:
                level -= 1
                if level > 3:
                    break
        else:
            return

        L, R = seq[i - 3], seq[i - 1]
        for j in range(i - 4, 0, -1):
            if isinstance(seq[j], int):
                seq[j] += L
                break

        for j in range(i, len(seq)):
            if isinstance(seq[j], int):
                seq[j] += R
                break

        seq[i - 4: i + 1] = [0]
        self.explode()
        self.split()

    def split(self):
        for i, c in enumerate(self.seq):
            if isinstance(c, int) and c > 9:
                self.seq[i: i + 1] = [LB, c // 2, CO, (c + 1) // 2, RB]
                self.explode()
                break

    def __add__(self, other):
        if not isinstance(other, SnailNumber):
            other = SnailNumber(other)

        return SnailNumber([LB] + self.seq + [CO] + other.seq + [RB])

    def __str__(self):
        return ''.join(str(x) for x in self.seq)

    @property
    def magnitude(self):
        stack = []
        for c in self.seq:
            if isinstance(c, int):
                stack.append(c)
            elif c == RB:
                r = stack.pop()
                l = stack.pop()
                stack.append(3 * l + 2 * r)

        return stack[0]


num = SnailNumber(lines[0])
for line in lines[1:]:
    num += line

print(num)
print(num.magnitude)
