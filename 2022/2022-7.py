from aocd import get_data
from aocd import submit

DAY = 7
YEAR = 2022

def part1(s):
    files = {}
    directories = {}
    directories["/"] = 0
    currentPath = ""
    for line in s.splitlines():
        if line.split(" ")[1] == "cd":
            if line.split(" ")[2] != "..":
                if line.split(" ")[2] != "/":
                    if len(currentPath) != 0 and currentPath[-1] != "/":
                        currentPath += "/"
                currentPath += line.split(" ")[2]
            elif line.split(" ")[2] == "..":
                currentPath = currentPath[:currentPath.rfind("/")]
                if len(currentPath) == 0:
                    currentPath = "/"
            else:
                print("error")
        elif line.split(" ")[1] == "ls":
            files[currentPath] = {}
        else:
            if line.split(" ")[0] == "dir":
                dirString = currentPath
                if currentPath != "/":
                    dirString += "/"
                dirString += line.split(" ")[1]
                directories[dirString] = 0
            else:
                files[currentPath][line.split(" ")[1]] = int(line.split(" ")[0])
                copyCurrentPath = currentPath
                while len(copyCurrentPath) > 0:
                    directories[copyCurrentPath] += int(line.split(" ")[0])
                    copyCurrentPath = copyCurrentPath[:copyCurrentPath.rfind("/")]

    result = 0
    for dir in directories:
        if directories[dir] <= 100000:
            result += directories[dir]
    submit(result, part="a", day=DAY, year=YEAR)


def part2(s):
    files = {}
    directories = {}
    directories["/"] = 0
    currentPath = ""
    for line in s.splitlines():
        if line.split(" ")[1] == "cd":
            if line.split(" ")[2] != "..":
                if line.split(" ")[2] != "/":
                    if len(currentPath) != 0 and currentPath[-1] != "/":
                        currentPath += "/"
                currentPath += line.split(" ")[2]
            elif line.split(" ")[2] == "..":
                currentPath = currentPath[:currentPath.rfind("/")]
                if len(currentPath) == 0:
                    currentPath = "/"
            else:
                print("error")
        elif line.split(" ")[1] == "ls":
            files[currentPath] = {}
        else:
            if line.split(" ")[0] == "dir":
                dirString = currentPath
                if currentPath != "/":
                    dirString += "/"
                dirString += line.split(" ")[1]
                directories[dirString] = 0
            else:
                files[currentPath][line.split(" ")[1]] = int(line.split(" ")[0])
                copyCurrentPath = currentPath
                while len(copyCurrentPath) > 0:
                    directories[copyCurrentPath] += int(line.split(" ")[0])
                    copyCurrentPath = copyCurrentPath[:copyCurrentPath.rfind("/")]
                if currentPath != "/":
                    directories["/"] += int(line.split(" ")[0])

    result = 70000000
    target = 30000000 - (70000000 - directories["/"])
    for dir in directories:
        if directories[dir] >= target:
            print(directories[dir], dir)
            if directories[dir] < result:
                result = directories[dir]
    submit(result, part="b", day=DAY, year=YEAR)


DATA = get_data(day=DAY, year=YEAR)
part1(DATA)
part2(DATA)

# lines = data.splitlines()
#
# # SOLUTION
# for index, line in enumerate(lines):
#     result = index
