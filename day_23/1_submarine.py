data = """
#############
#...........#
###D#C#A#B###
  #C#D#A#B#
  #########
"""


class Scene:
    def __init__(self, data):
        grid = data.strip("\n").split("\n")

        self.scene = {}
        self.height = len(grid)
        self.width = max(len(x) for x in grid)
        self.goal_col = {
            "A": {(2, 3), (3, 3)},
            "B": {(2, 5), (3, 5)},
            "C": {(2, 7), (3, 7)},
            "D": {(2, 9), (3, 9)},
        }
        self.entrances = set((1, x) for x in (3, 5, 7, 9))
        self._state = set()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (c := grid[i][j]) in "ABCD.":
                    self.scene[(i, j)] = c
                    if c in "ABCD":
                        self._state.add((c, (i, j)))

        self.energy = 0

    @property
    def state(self):
        return tuple(sorted(self._state))

    def __str__(self):
        return "\n".join("".join(self.scene.get((i, j), "#") for j in range(self.width)) for i in range(self.height))

    def can_move(self, a, b):
        if self.scene.get(b) != "." or b in self.entrances or self.scene.get(a) not in "ABCD":
            return False

        amphi = self.scene[a]
        i0, j0 = a
        i1, j1 = b

        if a in self.goal_col[amphi] and self.scene.get((i0 + 1, j0), "#") in (amphi, "#"):
            return False

        if b in self.goal_col[amphi] and self.scene.get((i1 + 1, j1), "#") not in (amphi, "#"):
            return False

        if i1 > 1 and b not in self.goal_col[amphi]:
            return False

        if i1 == i0 or i1 > 1 and i0 > 1:
            return False

        while i0 > 1:
            i0 -= 1
            if self.scene[(i0, j0)] != ".":
                return False

        dj = 1 if j1 > j0 else -1
        while j0 != j1:
            j0 += dj
            if self.scene[(i0, j0)] != ".":
                return False

        while i0 < i1:
            i0 += 1
            if self.scene[(i0, j0)] != ".":
                return False

        return True

    def move_amphi(self, a, b):
        result = Scene(str(self))
        amphi = result.scene[a]
        result.scene[a] = "."
        result.scene[b] = amphi
        result._state.remove((amphi, a))
        result._state.add((amphi, b))

        return result

    def next_states(self):
        for amphi, (i0, j0) in self._state:
            for ni, nj in self.scene:
                if self.can_move((i0, j0), (ni, nj)):
                    next_state = self.move_amphi((i0, j0), (ni, nj))
                    energy = (abs(i0 - ni) + abs(j0 - nj)) * {"A": 1, "B": 10, "C": 100, "D": 1000}[amphi]
                    yield next_state, energy

    def is_done(self):
        for k, v in self.goal_col.items():
            if any(self.scene[p] != k for p in v):
                return False

        return True


TABLE = {}


def find_min(scene, min_e=10e10, depth=0):
    if scene.state in TABLE:
        return TABLE[scene.state]

    if scene.is_done():
        TABLE[scene.state] = ([scene], 0)
        return TABLE[scene.state]

    result = []
    for next_s, next_e in scene.next_states():
        path, e = find_min(next_s, min_e, depth+1)
        e += next_e

        if e < min_e:
            min_e = e
            result = path

    TABLE[scene.state] = ([scene] + result, min_e)
    return TABLE[scene.state]


s = Scene(data)

path, e = find_min(s)
print(e)

