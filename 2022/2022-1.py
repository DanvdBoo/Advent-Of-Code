from aocd import get_data
from aocd import submit

DAY = 1
YEAR = 2022

data = get_data(day=DAY, year=YEAR)
lines = data.splitlines()
result = [0]
resultIndex = 0

# SOLUTION
for index, line in enumerate(lines):
    if line == '':
        resultIndex += 1
        result.append(0)
    else:
        result[resultIndex] += int(line)

result.sort()
max = result[resultIndex]
top3 = result[resultIndex] + result[resultIndex - 1] + result[resultIndex - 2]

submit(max, part="a", day=DAY, year=YEAR)
submit(top3, part="b", day=DAY, year=YEAR)
