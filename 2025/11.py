from .boilerPlate2025 import puzzle
import rustworkx as rx
from functools import cache

def part1(s: str):
    nodes = dict()
    graph = rx.PyDiGraph()
    for line in s.splitlines():
        n, con = line.split(':')
        if nodes.get(n) == None:
            nodes[n] = graph.add_node(n)
        for cs in con.split():
            c = cs.strip()
            if nodes.get(c) == None:
                nodes[c] = graph.add_node(c)
            graph.add_edge(nodes[n], nodes[c], None)
    return len(rx.all_simple_paths(graph, nodes['you'], nodes['out']))

def part2(s: str):
    lines = [l.split(': ') for l in s.splitlines()]
    g = {src: dst.split() for src,dst in lines}

    @cache
    def dfs(node: str, dac: bool, fft: bool):
        if node == 'out':
            return dac and fft
        return sum(dfs(dst, dac | (dst == 'dac'), fft | (dst == 'fft')) for dst in g[node])

    return dfs('svr', False, False)

puzzle(11, part1, part2, False, False).run()
