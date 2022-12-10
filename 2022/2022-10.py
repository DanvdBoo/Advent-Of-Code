from aocd import get_data
from aocd import submit

DAY = 10
YEAR = 2022

def part1(s):
    currentCycle = 0
    x = 1
    result = 0
    for line in s.splitlines():
        currentCycle += 1
        if (currentCycle - 20) % 40 == 0:
            result += (x * currentCycle)
        if line.split(' ')[0] == "addx":
            currentCycle += 1
            if (currentCycle - 20) % 40 == 0:
                result += (x * currentCycle)
            x += int(line.split(' ')[1])

    submit(result, part="a", day=DAY, year=YEAR)


def part2(s):
    currentCycle = 0
    currentRowPixel = 0
    currentRow = 0
    pixels = [''] * 6
    x = 1
    result = 0
    for line in s.splitlines():
        currentCycle += 1
        if currentCycle != 1 and (currentCycle - 1) % 40 == 0:
            currentRow += 1
            currentRowPixel = 0
        if abs(currentRowPixel - x) <= 1:
            pixels[currentRow] += '#'
        else:
            pixels[currentRow] += '.'
        currentRowPixel += 1
        if line.split(' ')[0] == "addx":
            currentCycle += 1
            if (currentCycle - 1) % 40 == 0:
                currentRow += 1
                currentRowPixel = 0
            if abs(currentRowPixel - x) <= 1:
                pixels[currentRow] += '#'
            else:
                pixels[currentRow] += '.'
            currentRowPixel += 1
            x += int(line.split(' ')[1])

    print(pixels[0], len(pixels[0]))
    print(pixels[1], len(pixels[1]))
    print(pixels[2], len(pixels[2]))
    print(pixels[3], len(pixels[3]))
    print(pixels[4], len(pixels[4]))
    print(pixels[5], len(pixels[5]))
    # submit(result, part="b", day=DAY, year=YEAR)


DATA = get_data(day=DAY, year=YEAR)
TESTDATA = open("testinput.txt", "r").read()
part1(DATA)
part2(DATA)

# lines = data.splitlines()
#
# # SOLUTION
# for index, line in enumerate(lines):
#     result = index
