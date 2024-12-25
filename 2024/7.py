from .boilerPlate2024 import puzzle

def part1(s: str):
    result = 0

    def recur(sum, goal, nums):
        if nums == []:
            return sum == goal
        if sum > goal:
            return False
        num = nums[0]
        res = recur(sum + num, goal, nums[1:])
        if sum != 0 and not res:
            res = recur(sum * num, goal, nums[1:])
        return res

    for line in s.splitlines():
        goal, numsTmp = line.split(':')
        goal = int(goal)
        nums = [int(x) for x in numsTmp.split()]
        if recur(0, goal, nums):
            result += goal
    return result

def part2(s: str):
    result = 0

    def recur(sum, goal, nums):
        if nums == []:
            return sum == goal
        if sum > goal:
            return False
        num = nums[0]
        res = recur(sum + num, goal, nums[1:])
        if sum != 0 and not res:
            res = recur(sum * num, goal, nums[1:])
        if not res:
            res = recur(int(str(sum) + str(num)), goal, nums[1:])
        return res

    for line in s.splitlines():
        goal, numsTmp = line.split(':')
        goal = int(goal)
        nums = [int(x) for x in numsTmp.split()]
        if recur(0, goal, nums):
            result += goal
    return result

puzzle(7, part1, part2, False, False).run()
