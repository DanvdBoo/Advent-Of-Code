from aocd import get_data
from aocd import submit

DAY = 1
YEAR = 2022

data = get_data(day=DAY, year=YEAR)
lines = data.splitlines()
result = 0

# SOLUTION
for index, line in enumerate(lines):
    result = index

print(result)
submit(result, part="a", day=DAY, year=YEAR)
submit(result, part="b", day=DAY, year=YEAR)
