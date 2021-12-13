data = open("input.txt").read()
lines = data.split("\n")
points = []


class Paper:
    def __init__(self, points):
        point_list = [tuple(int(k) for k in point.split(",")) for point in points]
        self.width = max(point[0] for point in point_list) + 1
        self.height = max(point[1] for point in point_list) + 1
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        for point in point_list:
            self.grid[point[1]][point[0]] = 1

    def __str__(self):
        return "\n".join("".join(".#"[self.grid[y][x]] for x in range(self.width)) for y in range(self.height))

    def fold_along_y(self, row):
        for i in range(min(row + 1, self.height - row)):
            self.grid[row - i] = [x | y for x, y in zip(self.grid[row - i], self.grid[row + i])]

        self.height = row

    def fold_along_x(self, col):
        for i in range(self.height):
            for j in range(min(col + 1, self.width - col)):
                self.grid[i][col - j] |= self.grid[i][col + j]

        self.width = col

    def count(self):
        return sum(self.grid[y][x] for x in range(self.width) for y in range(self.height))


paper = Paper(data.split("\n\n")[0].split("\n"))
print(paper.width, paper.height)

for fold in data.split("\n\n")[1].split("\n"):
    print(fold)
    if fold.startswith("fold along y="):
        y = int(fold.split("=")[1])
        paper.fold_along_y(y)
    elif fold.startswith("fold along x="):
        x = int(fold.split("=")[1])
        paper.fold_along_x(x)
    break

print(paper.count())
