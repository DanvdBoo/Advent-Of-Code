from .boilerPlate2023 import puzzle


def part1(s: str):
    result = 0
    for line in s.splitlines():
        cutLine = line.split(':')[1].split('|')
        winningNumbers = set(int(x) for x in cutLine[0].split())
        scratchNumbers = set(int(x) for x in cutLine[1].split())
        result += round(2**(len(winningNumbers & scratchNumbers) - 1))
    return result


def part2(s: str):
    result = 0
    copies = [1 for s in s.splitlines()]
    for index, line in enumerate(s.splitlines()):
        cutLine = line.split(':')[1].split('|')
        winningNumbers = set(int(x) for x in cutLine[0].split())
        scratchNumbers = set(int(x) for x in cutLine[1].split())
        matches = len(winningNumbers & scratchNumbers)
        for i in range(1, matches + 1):
            copies[index + i] += copies[index]
        result += copies[index]
    return result


puzzle(4, part1, part2, False, False).run()
