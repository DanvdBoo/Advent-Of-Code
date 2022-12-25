from aocd import get_data
from aocd import submit

DAY = 21
YEAR = 2022

def calculate(currentJob, jobs):
    if type(jobs[currentJob]) == int:
        return jobs[currentJob]
    mathOperation = jobs[currentJob].split(' ')
    value1 = calculate(mathOperation[0], jobs)
    value2 = calculate(mathOperation[2], jobs)
    if mathOperation[1] == '+':
        return value1 + value2
    if mathOperation[1] == '-':
        return value1 - value2
    if mathOperation[1] == '*':
        return value1 * value2
    if mathOperation[1] == '/':
        return int(value1 / value2)

def containsHumn(currentJob, jobs):
    if currentJob == 'humn':
        return True
    if type(jobs[currentJob]) == int:
        return False
    mathOperation = jobs[currentJob].split(' ')
    return containsHumn(mathOperation[0], jobs) | containsHumn(mathOperation[2], jobs)

def calculateWithoutHumn(currentJob, jobs, requiredValue):
    if currentJob == 'humn':
        return requiredValue
    mathOperation = jobs[currentJob].split(' ')
    target, targetHumn = mathOperation[0], mathOperation[2]
    flipped = False
    if containsHumn(mathOperation[0], jobs):
        flipped = True
        target, targetHumn = targetHumn, target
    value = calculate(target, jobs)
    if mathOperation[1] == '+':
        return calculateWithoutHumn(targetHumn, jobs, requiredValue - value)
    if mathOperation[1] == '-':
        if flipped:
            return calculateWithoutHumn(targetHumn, jobs, value + requiredValue)
        return calculateWithoutHumn(targetHumn, jobs, value - requiredValue)
    if mathOperation[1] == '*':
        return calculateWithoutHumn(targetHumn, jobs, int(requiredValue / value))
    if mathOperation[1] == '/':
        if flipped:
            return calculateWithoutHumn(targetHumn, jobs, value * requiredValue)
        return calculateWithoutHumn(targetHumn, jobs, int(value / requiredValue))

def part1(s):
    jobs = {}
    for line in s.splitlines():
        job = line.split(': ')
        try:
            number = int(job[1])
            jobs[job[0]] = number
        except:
            jobs[job[0]] = job[1]
    result = calculate('root', jobs)
    submit(result, part="a", day=DAY, year=YEAR)


def part2(s):
    jobs = {}
    for line in s.splitlines():
        job = line.split(': ')
        try:
            number = int(job[1])
            jobs[job[0]] = number
        except:
            jobs[job[0]] = job[1]
    mathOperation = jobs['root'].split(' ')
    if (containsHumn(mathOperation[0], jobs)):
        value = calculate(mathOperation[2], jobs)
        result = calculateWithoutHumn(mathOperation[0], jobs, value)
    else:
        value = calculate(mathOperation[0], jobs)
        result = calculateWithoutHumn(mathOperation[2], jobs, value)
    submit(result, part="b", day=DAY, year=YEAR)


DATA = get_data(day=DAY, year=YEAR)
TESTDATA = open("testinput.txt", "r").read()
part1(DATA)
part2(DATA)

# lines = data.splitlines()
#
# # SOLUTION
# for index, line in enumerate(lines):
#     result = index
