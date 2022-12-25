from aocd import get_data
from aocd import submit

DAY = 25
YEAR = 2022

def snafuToDec(value):
    times = 1
    result = 0
    for char in reversed(value):
        try:
            i = int(char)
        except:
            if char == '-':
                i = -1
            elif char == '=':
                i = -2
        result += i * times
        times *= 5
    return result

def pad(string, index):
    result = ''
    for i in range(index - len(string)):
        result += '0'
    return result + string

def decToSnafu(value):
    if value == 0:
        return '0'
    elif value == 1:
        return '1'
    elif value == 2:
        return '2'
    elif value == -1:
        return '-'
    elif value == -2:
        return '='
    times, index = 1, 0
    while True:
        maxValue = (2 * times) + ((times - 1) / 2)
        minValue = (-2 * times) - ((times - 1) / 2)
        if maxValue >= value and minValue <= value:
            break
        times *= 5
        index += 1
    if value < 0:
        if value <= (-2 * times) + ((times - 1) / 2):
            return '=' + pad(decToSnafu(value - (-2 * times)), index)
        else:
            return '-' + pad(decToSnafu(value - (-1 * times)), index)
    else:
        if value >= (2 * times) - ((times - 1) / 2):
            return '2' + pad(decToSnafu(value - (2 * times)), index)
        else:
            return '1' + pad(decToSnafu(value - (1 * times)), index)
    return 0

def part1(s):
    total = 0
    for line in s.splitlines():
        total += snafuToDec(line)
    result = decToSnafu(total)
    submit(result, part="a", day=DAY, year=YEAR)


def part2(s):
    return
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
