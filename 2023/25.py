import random
from .boilerPlate2023 import puzzle

class Edge:
    def __init__(self, s, d) -> None:
        self.src = s
        self.dest = d

class Graph:
    def __init__(self, v, e) -> None:
        self.V = v
        self.E = e

        self.edge = []

class subset:
    def __init__(self, p, r) -> None:
        self.parent = p
        self.rank = r

def find(subsets, i):
    if subsets[i].parent != i:
        subsets[i].parent = find(subsets, subsets[i].parent)
    return subsets[i].parent

def Union(subsets, x, y):
    xroot = find(subsets, x)
    yroot = find(subsets, y)

    if subsets[xroot].rank < subsets[yroot].rank:
        subsets[xroot].parent = yroot
    elif subsets[xroot].rank > subsets[yroot].rank:
        subsets[yroot].parent = xroot
    else:
        subsets[yroot].parent = xroot
        subsets[xroot].rank += 1

def part1(s: str):
    _ = random.random()
    edges = []
    nodes = []
    for line in s.splitlines():
        ns = line.split(' ')
        n, r = ns[0].replace(':', ''), ns[1:]
        if n not in nodes:
            nodes.append(n)
        for node in r:
            edges.append((n, node))
            if node not in nodes:
                nodes.append(node)
    V = len(nodes)
    E = len(edges)
    g = Graph(V, E)
    for e in edges:
        g.edge.append(Edge(nodes.index(e[0]), nodes.index(e[1])))
    
    REQUIREDCUTS = 3
    cuts = 0
    sizes = {}
    count = 1
    # Karger's Algorithm
    # Repeat until required three cuts is found and als there are two groups.
    # Since it is randomized, can take more than 400 tries.
    while len(sizes) != 2 or cuts > REQUIREDCUTS:
        print("Try: " + str(count))
        count += 1
        subsets = []

        for v in range(V):
            subsets.append(subset(v, 0))
        
        vertices = V

        while vertices > 2:
            i = int(10000 * random.random()) % E

            subset1 = find(subsets, g.edge[i].src)
            subset2 = find(subsets, g.edge[i].dest)

            if subset1 == subset2:
                continue
            vertices -= 1
            Union(subsets, subset1, subset2)

        sizes = {}
        cuts = 0
        for i in range(E):
            subset1 = find(subsets, g.edge[i].src)
            subset2 = find(subsets, g.edge[i].dest)
            if subset1 != subset2:
                cuts += 1
            elif subset1 == subset2:
                if subset1 in sizes:
                    sizes[subset1] += 1
                else:
                    sizes[subset1] = 1
        print(cuts)

    # Count how many nodes are in each group.
    groups = {}
    for i in range(E):
        subset1 = find(subsets, g.edge[i].src)
        subset2 = find(subsets, g.edge[i].dest)
        if subset1 != subset2:
            cuts += 1
        elif subset1 == subset2:
            if subset1 in groups:
                if g.edge[i].src not in groups[subset1]:
                    groups[subset1].append(g.edge[i].src)
                if g.edge[i].dest not in groups[subset1]:
                    groups[subset1].append(g.edge[i].dest)
            else:
                groups[subset1] = [g.edge[i].src, g.edge[i].dest]

    result = 1
    for _, i in groups.items():
        result *= len(i)
    return result

def part2(s: str):
    result = s
    return 0

puzzle(25, part1, part2, False, True).run()
