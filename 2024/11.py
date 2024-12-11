from .boilerPlate2024 import puzzle
from functools import lru_cache

def part1(s: str):
    @lru_cache(maxsize=None)
    def newStone(stone: int):
        if stone == 0:
            return [1]
        if len(str(stone)) % 2 == 0:
            stoneString = str(stone)
            return [int(stoneString[:len(stoneString)//2]), int(stoneString[len(stoneString)//2:])]
        else:
            return [stone * 2024]
    result = 0
    for num in s.split():
        cur = [int(num)]
        for _ in range(25):
            newcur = []
            for stone in cur:
                newcur += newStone(stone)
            cur = newcur
        result += len(cur)
    return result

def part2(s: str):
    result = 0
    for num in s.split():
        result += rec(int(num), 75)
    return result

@lru_cache(maxsize=None)
def rec(stone, depth):
    if depth == 0: return 1
    d = depth
    if stone == 0:
        return rec(1, d - 1)
    elif len(str(stone)) % 2 == 0:
        ss = str(stone)
        return rec(int(ss[:len(ss)//2]), d - 1) + rec(int(ss[len(ss)//2:]), d - 1)
    else:
        return rec(stone * 2024, d - 1)

puzzle(11, part1, part2, False, False).run()
