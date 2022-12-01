from aocd import get_data
from aocd import submit

DAY = 3
YEAR = 2021

data = get_data(day=DAY, year=YEAR)
lines = data.splitlines()
result = 0

# SOLUTION
bitStringSize = len(lines[0])
sums = [0] * bitStringSize
gamma = [0] * bitStringSize
epsilon = [0] * bitStringSize
for index, line in enumerate(lines):
    for i, char in enumerate(line):
        sums[i] += int(char)
for index, sum in enumerate(sums):
    avg = sum/len(lines)
    if avg < 0.5:
        epsilon[index] = 1
    else:
        gamma[index] = 1

result = int("".join(str(x) for x in gamma), 2) * int("".join(str(x) for x in epsilon), 2)

submit(result, part="a", day=DAY, year=YEAR)
# submit(result, part="b", day=DAY, year=YEAR)
