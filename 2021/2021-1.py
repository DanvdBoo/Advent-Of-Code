from aocd import get_data
from aocd import submit

DAY = 1
YEAR = 2021

data = get_data(day=DAY, year=YEAR)
lines = data.splitlines()
increaseCount = 0

# PART I
# previousLine = int(lines[0])
# for line in lines:
#     line = int(line)
#     if line > previousLine:
#         increaseCount += 1
#     previousLine = line

# PART II
runningSums = [0] * len(lines)
for index, line in enumerate(lines):
    line = int(line)
    runningSums[index] += line
    if index < 1: continue
    runningSums[index-1] += line
    if index < 2: continue
    runningSums[index-2] += line
    if index < 3: continue
    if runningSums[index-2] > runningSums[index-3]:
        increaseCount += 1

submit(increaseCount, part="b", day=DAY, year=YEAR)
