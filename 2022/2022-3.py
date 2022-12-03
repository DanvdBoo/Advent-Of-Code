from aocd import get_data
from aocd import submit

DAY = 3
YEAR = 2022

data = get_data(day=DAY, year=YEAR)
lines = data.splitlines()
charAdd = 0
groupAdd = 0
groupCommon = []
groupIndex = 0

# SOLUTION
for index, line in enumerate(lines):
    lineDone = False
    tempList = []
    if index % 3 == 0:
        if index > 1 and groupCommon[0] <= 'z' and groupCommon[0] >= 'a':
            groupAdd += ord(groupCommon[0]) - 96
        elif index > 1:
            groupAdd += ord(groupCommon[0]) - 38
        groupCommon = []
    halfway = int(len(line) / 2)
    for lineIndex, char in enumerate(line):
        if index % 3 == 0:
            groupIndex = int(index / 3) - 1
            if char not in groupCommon:
                groupCommon.append(char)
        else:
            if char in groupCommon and char not in tempList:
                tempList.append(char)
        if not lineDone and lineIndex < halfway:
            if char in line[halfway:]:
                if char <= 'z' and char >= 'a':
                    charAdd += ord(char) - 96
                else:
                    charAdd += ord(char) - 38
                lineDone = True
    if index % 3 != 0:
        groupCommon = tempList

if groupCommon[0] <= 'z' and groupCommon[0] >= 'a':
    groupAdd += ord(groupCommon[0]) - 96
else:
    groupAdd += ord(groupCommon[0]) - 38

submit(charAdd, part="a", day=DAY, year=YEAR)
submit(groupAdd, part="b", day=DAY, year=YEAR)
