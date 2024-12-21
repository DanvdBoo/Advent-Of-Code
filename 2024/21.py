from .boilerPlate2024 import puzzle
from itertools import permutations
from functools import lru_cache

kp = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], ['x', '0', 'A']]
kp = {key: (x, y) for y, line in enumerate(kp) for x, key in enumerate(line) if key != 'x'}
dp = [['x', '^', 'A'], ['<', 'v', '>']]
dp = {key: (x, y) for y, line in enumerate(dp) for x, key in enumerate(line) if key != 'x'}
ds = [(0, -1, '^'), (1, 0, '>'), (0, 1, 'v'), (-1, 0, '<')]
ds = {t[2]: (t[0], t[1]) for t in ds}

@lru_cache
def findPath(seq, d=2, ukp=True, cur=None):
    g = kp if ukp else dp
    if not seq:
        return 0
    if not cur:
        cur = g['A']
    
    cx, cy = cur
    px, py = g[seq[0]]
    dx, dy = px - cx, py - cy

    bs = ''
    if dx > 0:
        bs += '>'*dx
    if dx < 0:
        bs += '<'*-dx
    if dy > 0:
        bs += 'v'*dy
    if dy < 0:
        bs += '^'*-dy

    if d:
        ps = []
        for p in set(permutations(bs)):
            ncx, ncy = cx, cy
            for b in p:
                dx, dy = ds[b]
                ncx += dx
                ncy += dy
                if (ncx, ncy) not in g.values():
                    break
            else:
                ps.append(findPath(p+('A',), d - 1, False))
        minlen = min(ps)
    else:
        minlen = len(bs) + 1
    return minlen + findPath(seq[1:], d, ukp, (px, py))

def part1(s: str):
    result = 0
    for l in s.splitlines():
        result += int(l[0:3]) * findPath(l)
    return result

def part2(s: str):
    result = 0
    for l in s.splitlines():
        result += int(l[0:3]) * findPath(l, 25)
    return result

puzzle(21, part1, part2, False, False).run()
