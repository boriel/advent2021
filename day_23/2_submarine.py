data = """
#############
#...........#
###D#C#A#B###
  #D#C#B#A#
  #D#B#A#C#
  #C#D#A#B#
  #########
"""


class Scene:
    def __init__(self, data):
        grid = data.strip("\n").split("\n")

        self.scene = {}
        self.height = len(grid)
        self.width = max(len(x) for x in grid)
        self.goal_col = {x: set((i, 1 + 2 * (ord(x) - 64)) for i in range(2, 6)) for x in "ABCD"}
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

        if a in self.goal_col[amphi] and all(self.scene.get((i0 + i, j0), "#") in (amphi, "#") for i in range(3)):
            return False

        if b in self.goal_col[amphi] and any(self.scene.get((i1 + i, j1), "#") not in (amphi, "#") for i in range(1, 3)):
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


def energy(scene1, scene2):
    state1 = scene1.state
    state2 = scene2.state

    if state1 == state2:
        return 0

    s1 = next((x for x in state1 if x not in state2), None)
    s2 = next((x for x in state2 if x not in state1), None)
    if s1 is not None and s2 is not None:
        amphi, (i0, j0) = s1
        _, (ni, nj) = s2
        energy = (abs(i0 - ni) + abs(j0 - nj)) * {"A": 1, "B": 10, "C": 100, "D": 1000}[amphi]
        return energy

    return None


TABLE = {}


def find_min(scene, min_e=10e10, depth=0):
    # print(depth, min_e)
    # print(scene)
    # print()
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
prev = None

for s in path:
    print(s)
    if prev is not None:
        print(energy(prev, s))
    print()
    prev = s

print(e)
