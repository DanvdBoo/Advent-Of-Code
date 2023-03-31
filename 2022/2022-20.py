from aocd import get_data
from aocd import submit

DAY = 20
YEAR = 2022


def part1(s):
    numbers = [[index, int(i)]
               for index, i in enumerate(s.splitlines())]
    orig_len = len(numbers)
    current_index = 0
    for i in range(0, orig_len):
        while numbers[current_index][0] < i:
            current_index += 1
            if current_index >= orig_len:
                current_index = 0
        current_num = numbers.pop(current_index)
        if current_num[1] >= 0:
            shift = current_num[1] % orig_len
            shift = shift + current_index if shift + current_index < orig_len else (shift + current_index) - (orig_len - 1)
        else:
            shift = -1 * (abs(current_num[1]) % orig_len)
            shift = shift + current_index if shift + current_index > 0 else shift + current_index + orig_len - 1
        numbers = numbers[:shift] + [current_num] + numbers[shift:]
        if shift <= 1 or shift >= orig_len - 2:
            breakpoint = True
    
    print([num[1] for num in numbers])
    
    zero_index = 0
    for i, number in enumerate(numbers):
        if number[1] == 0:
            zero_index = i
    diff = [1000 % len(numbers), 2000 % len(numbers), 3000 % len(numbers)]
    result = 0
    for i in range(len(diff)):
        d = diff[i] + zero_index
        diff[i] = d if d < len(numbers) else d - len(numbers)
        result += numbers[diff[i]][1]
    print(result)
    return
    submit(result, part="a", day=DAY, year=YEAR)


def part2(s):
    return
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
