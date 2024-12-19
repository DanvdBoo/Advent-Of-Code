from .boilerPlate2024 import puzzle
from functools import lru_cache

def part1(s: str):
    splt = s.split('\n\n')
    ts = [c for c in splt[0].split(', ')]
    ds = [c for c in splt[1].splitlines()]
    ts.sort(key=lambda l: -len(l))

    @lru_cache
    def rec(pattern: str):
        if pattern == '':
            return True
        success = False
        for t in ts:
            if pattern.startswith(t):
                success = rec(pattern[len(t):])
            if success:
                return success
        return False

    result = 0
    for d in ds:
        if rec(d):
            result += 1

    return result

def part2(s: str):
    splt = s.split('\n\n')
    ts = [c for c in splt[0].split(', ')]
    ds = [c for c in splt[1].splitlines()]
    ts.sort(key=lambda l: -len(l))

    @lru_cache
    def rec(pattern: str):
        if pattern == '':
            return 1
        c = 0
        for t in ts:
            if pattern.startswith(t):
                c += rec(pattern[len(t):])
        return c

    result = 0
    for d in ds:
        result += rec(d)

    return result

puzzle(19, part1, part2, False, False).run()
