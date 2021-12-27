class Card:
    def __init__(self, lines):
        self.lines = [line.strip() for line in lines if line.strip()]
        self.pos = dict()
        assert len(self.lines) == 5
        self.numbers = [[0] * 5 for _ in range(5)]
        self.elems = []
        for i, line in enumerate(self.lines):
            elems = [int(x) for x in line.split(" ") if x]
            assert len(elems) == 5
            self.elems.append(elems)

            for j, elem in enumerate(elems):
                self.pos[elem] = (i, j)

        self.pending = set(self.pos.keys())

    def set(self, num: int) -> int:
        if num not in self.pending:
            return 0

        i, j = self.pos[num]
        self.numbers[i][j] = 1
        self.pending.remove(num)

        if sum(self.numbers[i][k] for k in range(5)) == 5 or sum(self.numbers[k][j] for k in range(5)) == 5:
            return num * sum(self.pending)

        return 0

    def __repr__(self):
        return '\n'.join(" ".join("%2i" % x for x in elems) for elems in self.elems)

    @property
    def state(self):
        return '\n'.join(''.join(str(x) for x in numbers) for numbers in self.numbers)


lines = open("input.txt").readlines()
numbers = [int(x) for x in lines.pop(0).split(",")]

cards = set()
played_numbers = []
while lines:
    cards.add(Card(lines[:6]))
    lines = lines[6:]

for num in numbers:
    played_numbers.append(num)
    for card in list(cards):
        score = card.set(num)
        if score:
            cards.remove(card)
            if not cards:
                print(played_numbers)
                print(card)
                print(sum(card.pending) * num)
