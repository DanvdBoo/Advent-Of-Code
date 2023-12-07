import time
from aocd import get_data
from aocd import submit

class puzzle:
    def __init__(self, day: int, part1, part2, test1: bool, test2: bool):
        self.day = day
        self.year = 2023
        self.part1 = part1
        self.part2 = part2
        self.test1 = test1
        self.test2 = test2

    def run(self):
        data = get_data(day=self.day, year=self.year)
        testdata = open("testinput.txt", "r").read()

        print("----- PART 1 -----")
        start_time = time.time()
        tmp = self.part1(testdata if self.test1 else data)
        print("runtime: %s ms" % ((time.time() - start_time) * 1000))
        if self.test1:
            print("Result of part 1:", tmp)
        else:
            submit(tmp, part="a", day=self.day, year=self.year)

        print("----- PART 2 -----")
        start_time = time.time()
        tmp = self.part2(testdata if self.test2 else data)
        print("runtime: %s ms" % ((time.time() - start_time) * 1000))

        if self.test2:
            print("Result of part 2:", tmp)
        else:
            submit(tmp, part="b", day=self.day, year=self.year)
