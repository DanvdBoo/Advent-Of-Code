from .boilerPlate2023 import puzzle


def part1(s: str):
    result = 0
    for line in s.splitlines():
        cutLine = line.split(' ')
        winningN = []
        currentScore = 0
        ownNumbers = False
        for n in cutLine:
            if n == 'Card' or n.count(':') >= 1 or n == '':
                continue
            if n == '|':
                ownNumbers = True
                continue
            num = int(n)
            if ownNumbers:
                if num in winningN:
                    if currentScore == 0:
                        currentScore = 1
                    else:
                        currentScore *= 2
            else:
                winningN.append(num)
        result += currentScore
    return result


def part2(s: str):
    copies = [1 for s in s.splitlines()]
    for index, line in enumerate(s.splitlines()):
        cutLine = line.split(' ')
        winningN = []
        count = 0
        ownNumbers = False
        for n in cutLine:
            if n == 'Card' or n.count(':') >= 1 or n == '':
                continue
            if n == '|':
                ownNumbers = True
                continue
            num = int(n)
            if ownNumbers:
                if num in winningN:
                    count += 1
            else:
                winningN.append(num)
        mult = copies[index]
        for i in range(1, count + 1):
            copies[index + i] += mult
    return sum(copies)


puzzle(4, part1, part2, False, False).run()
