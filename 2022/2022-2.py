from aocd import get_data
from aocd import submit

DAY = 2
YEAR = 2022

data = get_data(day=DAY, year=YEAR)
lines = data.splitlines()
result = 0

# SOLUTION
for index, line in enumerate(lines):
    sum = 0
    char = line.split()
    if char[1] == 'X':
        sum += 1
    elif char[1] == 'Y':
        sum += 2
    else:
        sum += 3

    if char[0] == 'A':
        if char[1] == 'X':
            sum += 3
        elif char[1] == 'Y':
            sum += 6
        else:
            sum += 0
    elif char[0] == 'B':
        if char[1] == 'X':
            sum += 0
        elif char[1] == 'Y':
            sum += 3
        else:
            sum += 6
    elif char[0] == 'C':
        if char[1] == 'X':
            sum += 6
        elif char[1] == 'Y':
            sum += 0
        else:
            sum += 3
    result += sum

submit(result, part="a", day=DAY, year=YEAR)

result = 0

# SOLUTION B
for index, line in enumerate(lines):
    sum = 0
    char = line.split()
    if char[1] == 'X':
        sum += 0
    elif char[1] == 'Y':
        sum += 3
    else:
        sum += 6

    if char[0] == 'A':
        if char[1] == 'X':
            sum += 3
        elif char[1] == 'Y':
            sum += 1
        else:
            sum += 2
    elif char[0] == 'B':
        if char[1] == 'X':
            sum += 1
        elif char[1] == 'Y':
            sum += 2
        else:
            sum += 3
    elif char[0] == 'C':
        if char[1] == 'X':
            sum += 2
        elif char[1] == 'Y':
            sum += 3
        else:
            sum += 1
    result += sum

submit(result, part="b", day=DAY, year=YEAR)
