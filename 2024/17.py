from .boilerPlate2024 import puzzle

def part1(s: str):
    lines = s.splitlines()
    a = int(lines[0].replace('Register A: ', ''))
    b = int(lines[1].replace('Register B: ', ''))
    c = int(lines[2].replace('Register C: ', ''))
    p = [int(c) for c in lines[4].replace('Program: ', '').split(',')]
    output = []
    ptx = 0

    def getValue(co: int):
        nonlocal a, b, c
        if co < 4:
            return co
        if co == 4:
            return a
        if co == 5:
            return b
        if co == 6:
            return c
        print("Something went wrong")

    def doAction(opcode: int, v: int, fallback: int):
        nonlocal a, b, c, ptx
        if opcode == 0:
            a = a // (2 ** v)
        elif opcode == 1:
            b = b ^ fallback
        elif opcode == 2:
            b = v % 8
        elif opcode == 3:
            ptx = v - 2 if a != 0 else ptx
        elif opcode == 4:
            b = b ^ c
        elif opcode == 5:
            output.append(v % 8)
        elif opcode == 6:
            b = a // (2 ** v)
        elif opcode == 7:
            c = a // (2 ** v)

    while ptx < len(p):
        action, v = p[ptx], getValue(p[ptx + 1])
        doAction(action, v, p[ptx + 1])
        ptx += 2

    result = ','.join(str(x) for x in output)
    return result

# b = a % 8
# b = b ^ 5
# c = a >> b
# b = b ^ 6
# b = b ^ c
# out(b % 8)
# a = a >> 3
# jnz
def part2(s: str):
    lines = s.splitlines()
    p = [int(c) for c in lines[4].replace('Program: ', '').split(',')]
    result = 0
    def getOutput(a: int):
        b = a % 8
        b = b ^ 5
        c = a >> b
        b = b ^ 6
        b = b ^ c
        return b % 8
    result = 0

    def rec(r: int, ind: int):
        nonlocal p
        if ind == -1:
            return r
        r = r << 3
        for i in range(8):
            if getOutput(r | i) == p[ind]:
                res = rec(r | i, ind - 1)
                if res != -1:
                    return res
        return -1

    result = rec(0, -1 % len(p))
    return result

puzzle(17, part1, part2, False, False).run()