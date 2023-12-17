from functools import partial
from .boilerPlate2023 import puzzle

def part12(s: str, part1: bool):
    result = 0
    copies = [1 for s in s.splitlines()]
    for index, line in enumerate(s.splitlines()):
        cutLine = line.split(':')[1].split('|')
        winningNumbers = set(int(x) for x in cutLine[0].split())
        scratchNumbers = set(int(x) for x in cutLine[1].split())
        if part1:
            result += round(2**(len(winningNumbers & scratchNumbers) - 1))
        else:
            for i in range(1, len(winningNumbers & scratchNumbers) + 1):
                copies[index + i] += copies[index]
            result += copies[index]
    return result

puzzle(4, partial(part12, part1 = True), partial(part12, part1 = False), False, False).run()
