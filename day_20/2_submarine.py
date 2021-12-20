data = open("input.txt").read().strip().split("\n\n")
code = data[0].replace("\n", "")
img = [[x for x in line] for line in data[1].split("\n")]


class Image:
    def __init__(self, img_data, code):
        self.img = img_data
        self.code = code
        self.generation = 0
        self.default = "."

    def __str__(self):
        return "\n".join("".join(x for x in line) for line in self.img)

    def count(self, x="#"):
        return sum(sum(x == k for k in line) for line in self.img)

    @property
    def width(self):
        return len(self.img[0])

    @property
    def height(self):
        return len(self.img)

    def kernel(self, x, y):
        result = []
        for i in (-1, 0, 1):
            y1 = y + i
            for j in (-1, 0, 1):
                x1 = x + j
                result.append(self.img[y1][x1] if 0 <= y1 < self.height and 0 <= x1 < self.width else self.default)

        return result

    def grow(self):
        new_img = [[self.default] * (self.width + 2)]
        new_img.extend([self.default] + line + [self.default] for line in self.img)
        new_img.append([self.default] * (self.width + 2))
        self.img = new_img

    def update(self):
        new_img = [["." for j in range(self.width)] for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.width):
                k = int("".join({".": "0", "#": "1"}[x] for x in self.kernel(j, i)), 2)
                new_img[i][j] = self.code[k]

        self.img = new_img

    def evolve(self):
        self.grow()
        self.grow()
        self.update()


x = Image(img, code)
for i in range(50):
    x.default = {0: ".", 1: "#"}[i % 2]
    x.evolve()
    print(i + 1, x.count())

