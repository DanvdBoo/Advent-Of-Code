from aocd import get_data
from aocd import submit

DAY = 2
YEAR = 2023

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
    submit(result, part="a", day=DAY, year=YEAR)


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
    submit(result, part="b", day=DAY, year=YEAR)


DATA = get_data(day=DAY, year=YEAR)
TESTDATA = open("testinput.txt", "r").read()
part1(DATA)
part2(DATA)

# lines = data.splitlines()
#
# # SOLUTION
# for index, line in enumerate(lines):
#     result = index
