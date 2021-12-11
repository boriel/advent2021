input = open("input.txt", "r").read()


class Board:
    def __init__(self, data: str):
        self.data = [[int(x) for x in line] for line in data.strip().split("\n")]
        self.max_x = len(self.data[0]) - 1
        self.max_y = len(self.data) - 1

    def __str__(self):
        return "\n".join("".join(str(x) for x in line) for line in self.data)

    def evolve(self) -> int:
        flashes = 0
        pending = []

        for i in range(self.max_y + 1):
            for j in range(self.max_x + 1):
                self.data[i][j] = (self.data[i][j] + 1) % 10
                if not self.data[i][j]:
                    flashes += 1
                    pending.append((i, j))

        while pending:
            i, j = pending.pop()

            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    y = i + di
                    x = j + dj
                    if 0 <= y <= self.max_y and 0 <= x <= self.max_x and self.data[y][x]:
                        self.data[y][x] = (self.data[y][x] + 1) % 10
                        if self.data[y][x]:
                            continue

                        flashes += 1
                        pending.append((y, x))

        return flashes

    def flash(self):
        return not sum(sum(line) for line in self.data)


x = Board(input)
for i in range(1000):
    x.evolve()
    if x.flash():
        print(i + 1)
        break
