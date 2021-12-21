from collections import defaultdict


data = open("input.txt").read().strip()


class Scanner:
    def __init__(self, name, probes):
        self.name = name
        self.probes = set([tuple(int(x) for x in probe) for probe in probes])
        self._update_dists()

    def _update_dists(self):
        self.dists = defaultdict(set)

        for p1 in self.probes:
            for p2 in self.probes:
                if p1 == p2:
                    continue

                k = tuple(sorted([p1, p2]))
                dist = tuple((x - y) for x, y in zip(*k))
                self.dists[dist].add(k)

    def __str__(self):
        return f"{self.name}\n" + "\n".join(str(x) for x in sorted(self.probes))

    def relative_coords_to(self, other, L=12):
        common_dists = [k for k in self.dists if k in other.dists]

        for dist in common_dists:
            for v1 in self.dists[dist]:
                for v2 in other.dists[dist]:
                    offset = self._vector_offset(v1, v2)
                    if len(self.probes.intersection(self._shift_coord(x, offset) for x in other.probes)) >= L:
                        return offset

        return None

    @staticmethod
    def _vector_coords(v, offset=(0, 0)):
        return tuple(tuple(i + j for i, j in zip(offset, x)) for x in v)

    @staticmethod
    def _vector_offset(v1, v2):
        return tuple(x - y for x, y in zip(v1[0], v2[0]))

    @staticmethod
    def _shift_coord(coord, offset):
        return tuple(x + y for x, y in zip(coord, offset))

    @staticmethod
    def _rotate_coord(coord, axis):
        x, y, z = coord
        return {
            "x": (x, -z, y),
            "y": (z, y, -x),
            "z": (-y, x, z),
        }[axis.lower()]

    def _rotate_along(self, coord, x=0, y=0, z=0):
        for i in range(x):
            coord = self._rotate_coord(coord, "x")

        for i in range(y):
            coord = self._rotate_coord(coord, "y")

        for i in range(z):
            coord = self._rotate_coord(coord, "z")

        return coord

    def rotate_along(self, x=0, y=0, z=0):
        probes = [self._rotate_along(probe, x, y, z) for probe in self.probes]
        name = f"{self.name} :: {(x, y, z)}"
        return Scanner(name=name, probes=probes)

    def translate(self, x=0, y=0, z=0):
        self.probes = [tuple(a + b for a, b in zip((x, y, z), probe)) for probe in self.probes]
        return self

    def find_relative_orientation(self, other):
        for rz in range(4):
            for ry in range(4):
                for rx in range(4):
                    s1 = other.rotate_along(rx, ry, rz)
                    offset = self.relative_coords_to(s1)
                    if offset:
                        return offset, (rx, ry, rz)

    def join(self, other: 'Scanner'):
        c = self.find_relative_orientation(other)
        if not c:
            return False

        offset, (rx, ry, rz) = c
        other = other.rotate_along(rx, ry, rz).translate(*offset)
        self.probes.update(other.probes)
        self._update_dists()

        return True

    def copy(self):
        return Scanner(name=f"{self.name}'", probes=self.probes)


scanners = []
for chunk in data.strip().split("\n\n"):
    lines = chunk.split("\n")
    scanners.append(Scanner(lines[0], [line.split(",") for line in lines[1:]]))


s = scanners.pop()
while scanners:
    for i in range(len(scanners) - 1, -1, -1):
        if s.join(scanners[i]):
            scanners.pop(i)

print(len(s.probes))
