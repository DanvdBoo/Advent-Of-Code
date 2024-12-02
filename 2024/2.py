from .boilerPlate2024 import puzzle

def part1(s: str):
    result = 0
    for line in s.splitlines():
        nums = [int(x) for x in line.split()]
        asc = nums[0] - nums[1] < 0
        safe = True
        prev = nums[0]
        for next in nums[1::]:
            if asc and (prev - next >= 0 or prev - next < -3):
                safe = False
                break
            elif not asc and (prev - next <= 0 or prev - next > 3):
                safe = False
                break
            prev = next
        if safe:
            result += 1
    return result

def checkHazards(nums):
    asc = nums[0] - nums[1] < 0
    safe = True
    prev = nums[0]
    for next in nums[1::]:
        if asc and (prev - next >= 0 or prev - next < -3):
            safe = False
            break
        elif not asc and (prev - next <= 0 or prev - next > 3):
            safe = False
            break
        prev = next
    return safe

def part2(s: str):
    result = 0
    for line in s.splitlines():
        nums = [int(x) for x in line.split()]
        if checkHazards(nums):
            result += 1
        else:
            safeWitHazard = False
            for i in range(len(nums)):
                if checkHazards(nums[:i] + nums[i+1:]):
                    safeWitHazard = True
                    break
            if safeWitHazard:
                result += 1
    return result

puzzle(2, part1, part2, False, False).run()
