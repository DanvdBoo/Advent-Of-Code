from .boilerPlate2024 import puzzle
import math

def part1(s: str):
    parts = s.split('\n\n')
    rules = {}
    for line in parts[0].splitlines():
        nums = [int(t) for t in line.split('|')]
        if rules.get(nums[0]) is None:
            rules[nums[0]] = ([], [nums[1]])
        else:
            rules[nums[0]][1].append(nums[1])
        if rules.get(nums[1]) is None:
            rules[nums[1]] = ([nums[0]], [])
        else:
            rules[nums[1]][0].append(nums[0])
    
    result = 0
    for line in parts[1].splitlines():
        nums = [int(t) for t in line.split(',')]
        correct = True
        for index, num in enumerate(nums):
            for prev in nums[:index]:
                if rules.get(num) is not None and prev in rules[num][1]:
                    correct = False
            for next in nums[index + 1:]:
                if rules.get(num) is not None and next in rules[num][0]:
                    correct = False
        if correct:
            result += nums[math.floor(len(nums)/2)]

    return result

def part2(s: str):
    parts = s.split('\n\n')
    rules = {}
    for line in parts[0].splitlines():
        nums = [int(t) for t in line.split('|')]
        if rules.get(nums[0]) is None:
            rules[nums[0]] = ([], [nums[1]])
        else:
            rules[nums[0]][1].append(nums[1])
        if rules.get(nums[1]) is None:
            rules[nums[1]] = ([nums[0]], [])
        else:
            rules[nums[1]][0].append(nums[0])
    
    result = 0
    for line in parts[1].splitlines():
        nums = [int(t) for t in line.split(',')]
        correct = True
        for index, num in enumerate(nums):
            for prev in nums[:index]:
                if rules.get(num) is not None and prev in rules[num][1]:
                    correct = False
            for i, next in enumerate(nums[index + 1:]):
                if rules.get(num) is not None and next in rules[num][0]:
                    correct = False
                    nums[index], nums[i + index + 1] = next, num
                    break
        if not correct:
            correct = False
            while correct == False:
                correct = True
                for index, num in enumerate(nums):
                    for prev in nums[:index]:
                        if rules.get(num) is not None and prev in rules[num][1]:
                            correct = False
                    for i, next in enumerate(nums[index + 1:]):
                        if rules.get(num) is not None and next in rules[num][0]:
                            correct = False
                            nums[index], nums[i + index + 1] = next, num
                            break
            result += nums[math.floor(len(nums)/2)]
    
    return result

puzzle(5, part1, part2, False, False).run()
