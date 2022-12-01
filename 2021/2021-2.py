from aocd import get_data
from aocd import submit

DAY = 2
YEAR = 2021

data = get_data(day=DAY, year=YEAR)
lines = data.splitlines()
result = 0

# SOLUTION PART I
Horizontal = 0
Depth = 0
Aim = 0
for index, line in enumerate(lines):
    temp = line.split()
    if temp[0] == "forward":
        Horizontal += int(temp[1])
        Depth += Aim * int(temp[1])
    elif temp[0] == "down":
        Aim += int(temp[1])
    elif temp[0] == "up":
        Aim -= int(temp[1])
result = Horizontal * Depth

# submit(result, part="a", day=DAY, year=YEAR)
submit(result, part="b", day=DAY, year=YEAR)
