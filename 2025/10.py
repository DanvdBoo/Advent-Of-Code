from .boilerPlate2025 import puzzle
from collections import deque
from scipy.optimize import linprog

def getToggles(ts: str, target: int):
    nums = [int(x) for x in ts.split(',')]
    r = 0b0
    for x in nums:
        r = r | (0b1 << target >> x)
    return r

def part1(s: str):
    result = 0
    for line in s.splitlines():
        parts = line.split(' ')
        target = [0 if x == '.' else 1 for x in parts[0].strip('[]')]
        switches = [getToggles(x.strip('()'), len(target) - 1) for x in parts[1:-1]]
        target = sum(c << i for i, c in enumerate(reversed(target)))
        q = deque(((0b0, 0), ))
        visited = set()
        visited.add(0b0)

        while q:
            cur, depth = q.popleft()

            if cur == target:
                result += depth
                break
            for switch in switches:
                n = cur ^ switch
                if n not in visited:
                    visited.add(n)
                    q.append((n, depth + 1))
    return result

def part2(s: str):
    result = 0
    for line in s.splitlines():
        parts = line.split(' ')
        target = tuple(map(int, parts[-1].strip('}{').split(',')))
        switches = [set(map(int, x.strip('()').split(','))) for x in parts[1:-1]]

        c = [1] * len(switches)
        A_eq = [[(i in sw) for sw in switches] for i in range(len(target))]
        r = linprog(c, A_eq=A_eq, b_eq=target, integrality=1).fun
        result += r
    return int(result)

puzzle(10, part1, part2, False, False).run()
