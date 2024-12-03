import re
from .boilerPlate2024 import puzzle

def part1(s: str):
    result = 0
    matches = re.finditer(r'mul[(]\d{,3},\d{,3}[)]', s)
    for x in matches:
        nums = re.findall(r'\d+', x.group())
        result += int(nums[0]) * int(nums[1])
    return result

def part2(s: str):
    donts = s.split("don't()")
    new = donts[0]
    for substring in donts[1:]:
        index = substring.find("do()")
        if index != -1:
            new += substring[index:]
    return part1(new)

puzzle(3, part1, part2, False, False).run()
