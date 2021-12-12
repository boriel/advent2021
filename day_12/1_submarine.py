from collections import defaultdict

START = 'start'
END = 'end'

data = open("input.txt").read().strip()


class Graph:
    def __init__(self, input_):
        lines = input_.strip().split("\n")
        self.nodes = defaultdict(list)
        for line in lines:
            a, b = line.split('-')
            self.nodes[a].append(b)
            self.nodes[b].append(a)

    def all_paths_from(self, node, visited=None):
        if node == END:
            yield [END]
            return

        if visited is None:
            visited = set()

        for next in self.nodes[node]:
            if next == next.lower() and next in visited:
                continue

            for path in self.all_paths_from(next, visited.union([next])):
                yield [node] + path

    def __str__(self):
        return "\n".join(f"{x} -> {','.join(y)}" for x, y in self.nodes.items())


graph = Graph(data)
#paths = sorted(','.join(p) for p in graph.all_paths_from(START, {START}))
paths = []
for p in graph.all_paths_from(START, {START}):
    for x in p:
        if x == x.lower() and x not in (START, END):
            paths.append(p)
            break

# print("\n".join(paths))
print(len(paths))
