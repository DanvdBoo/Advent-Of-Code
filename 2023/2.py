from .boilerPlate2023 import puzzle

def part1(s: str):
    result = 0
    max = {'red': 12, 'green': 13, 'blue': 14}
    for line in s.splitlines():
        words = line.split(' ')
        gameN = int(words[1].replace(':', ''))
        isAllowed = True
        for i in range(int(len(words)/2 - 1)):
            currentNumber = int(words[2 + i * 2])
            color = words[3 + i * 2].replace(',', '').replace(';', '')
            if max[color] < currentNumber:
                isAllowed = False
        if isAllowed:
            result += gameN
    return result


def part2(s: str):
    result = 0
    for line in s.splitlines():
        max = {'red': 0, 'green': 0, 'blue': 0}
        words = line.split(' ')
        for i in range(int(len(words)/2 - 1)):
            currentNumber = int(words[2 + i * 2])
            color = words[3 + i * 2].replace(',', '').replace(';', '')
            if max[color] < currentNumber:
                max[color] = currentNumber
        result += max['blue'] * max['green'] * max['red']
    return result

puzzle(2, part1, part2, False, False).run()
