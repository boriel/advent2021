from collections import defaultdict, Counter

START = 'start'
END = 'end'

data = open("input.txt").read()


class Graph:
    def __init__(self, input_):
        lines = input_.strip().split("\n")
        self.nodes = defaultdict(list)
        for line in lines:
            a, b = line.split('-')
            self.nodes[a].append(b)
            self.nodes[b].append(a)

    def all_paths_from(self, node, visited=None, twice=False):
        if node == END:
            yield [END]
            return

        if visited is None:
            visited = set()

        prev_twice = twice
        for next in self.nodes[node]:
            twice = prev_twice
            if next == next.lower() and next in visited:
                if twice or next == START:
                    continue
                twice = True

            for path in self.all_paths_from(next, visited.union([next]), twice):
                yield [node] + path

    def __str__(self):
        return "\n".join(f"{x} -> {','.join(y)}" for x, y in self.nodes.items())


graph = Graph(data)
#paths = sorted(','.join(p) for p in graph.all_paths_from(START, {START}))
#print("\n".join(paths))
print(sum(1 for _ in graph.all_paths_from(START, {START})))
