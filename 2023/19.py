from .boilerPlate2023 import puzzle
import copy
import functools

def part1(input: str):
    workflows, parts = input.split('\n\n')
    w = {}
    for line in workflows.splitlines():
        n, formulas = line.split('{')
        f = formulas[:-1].split(',')
        w[n] = []
        for form in f:
            f1, res = '', ''
            try:
                f1, res = form.split(':')
            except:
                res = form
            w[n].append((f1, res))
    result = 0
    for part in parts.splitlines():
        x, m, a, s = part.split(',')
        x, m, a, s = int(x[3:]), int(m[2:]), int(a[2:]), int(s[2:-1])
        currWF = "in"
        while currWF != "A" and currWF != "R":
            for eq in w[currWF]:
                if eq[0] == '' or eval(eq[0]):
                    currWF = eq[1]
                    break
        if currWF == "A":
            result += x + m + a + s
    return result

def part2(input: str):
    workflows, _ = input.split('\n\n')
    w = {}
    for line in workflows.splitlines():
        n, formulas = line.split('{')
        f = formulas[:-1].split(',')
        w[n] = []
        for form in f:
            f1, res = '', ''
            try:
                f1, res = form.split(':')
            except:
                res = form
            w[n].append((f1, res))
    result = 0
    q = [('in', {'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]})]
    def getDiff(pair):
        return pair[1] - pair[0] + 1
    while q:
        f, r = q.pop()
        if f == 'A':
            result += getDiff(r['x']) * getDiff(r['m']) * getDiff(r['a']) * getDiff(r['s'])
            continue
        if f == 'R':
            continue
        for eq in w[f]:
            if eq[0] == '':
                q.append((eq[1], r))
                continue
            c = eq[0][0]
            symb = eq[0][1]
            num = int(eq[0][2:])
            if (num > r[c][0] and symb == '<') or (num < r[c][1] and symb == '>'):
                newR = copy.deepcopy(r)
                newR[c][0 if symb == '>' else 1] = num - 1 if num > r[c][0] and symb == '<' else num + 1 if num < r[c][1] and symb == '>' else r[c][0 if symb == '>' else 1]
                r[c][1 if symb == '>' else 0] = num if num > r[c][0] and symb == '<' else num if num < r[c][1] and symb == '>' else r[c][0 if symb == '>' else 1]
                q.append((eq[1], newR))
            else:
                q.append((eq[1], r))
                break
    return result

puzzle(19, part1, part2, False, False).run()
