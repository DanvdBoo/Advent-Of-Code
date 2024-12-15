from .boilerPlate2024 import puzzle

dirs = {'<': (0, -1), '^': (-1, 0), '>': (0, 1), 'v': (1, 0)}

def part1(s: str):
    g, m = s.split('\n\n')
    grid = [[c for c in line] for line in g.splitlines()]
    m = m.replace('\n', '')
    bot = (-1, -1)
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == '@':
                bot = (x, y)
    for c in m:
        nx, ny = bot[0] + dirs[c][0], bot[1] + dirs[c][1]
        if grid[nx][ny] == '.':
            grid[bot[0]][bot[1]] = '.'
            grid[nx][ny] = '@'
            bot = (nx, ny)
        elif grid[nx][ny] == 'O':
            tx, ty = nx, ny
            while grid[tx][ty] == 'O':
                tx, ty = tx + dirs[c][0], ty + dirs[c][1]
            if grid[tx][ty] == '.':
                grid[tx][ty] = 'O'
                grid[nx][ny] = '@'
                grid[bot[0]][bot[1]] = '.'
                bot = (nx, ny)
    result = 0
    for x in range(len(grid)):
        l = ''
        for y in range(len(grid[0])):
            l += grid[x][y]
            if grid[x][y] == 'O':
                result += 100 * x + y
        print(l)
    return result

def part2(s: str):
    g, m = s.split('\n\n')
    grid = [[c for c in line.replace('#', '##').replace('.', '..').replace('O', '[]').replace('@', '@.')] for line in g.splitlines()]
    m = m.replace('\n', '')
    bot = (-1, -1)
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == '@':
                bot = (x, y)
    for c in m:
        nx, ny = bot[0] + dirs[c][0], bot[1] + dirs[c][1]
        if grid[nx][ny] == '.':
            grid[bot[0]][bot[1]] = '.'
            grid[nx][ny] = '@'
            bot = (nx, ny)
        elif grid[nx][ny] == '[' or grid[nx][ny] == ']':
            if c == '<' or c == '>':
                ty = ny
                pty = ny
                while grid[nx][ty] == '[' or grid[nx][ty] == ']':
                    pty = ty
                    ty = ty + dirs[c][1]
                if grid[nx][ty] == '#':
                    continue
                while ty != ny:
                    grid[nx][ty], grid[nx][pty] = grid[nx][pty], grid[nx][ty]
                    ty = ty + -1 * dirs[c][1]
                    pty = pty + -1 * dirs[c][1]
                grid[nx][ny] = '@'
                grid[bot[0]][bot[1]] = '.'
                bot = (nx, ny)
            else:
                ys = {bot[0]: [bot[1]]}
                ptx = bot[0]
                tx = nx
                passable = True
                while True:
                    tmp = []
                    end = True
                    for l in ys[ptx]:
                        if grid[tx][l] == '[' and l not in tmp:
                            end = False
                            tmp.append(l)
                            if l + 1 not in tmp:
                                tmp.append(l + 1)
                        elif grid[tx][l] == ']' and l not in tmp:
                            end = False
                            tmp.append(l)
                            if l - 1 not in tmp:
                                tmp.append(l - 1)
                        elif grid[tx][l] == '#':
                            passable = False
                            break
                    if not passable: break
                    if end: break
                    ys[tx] = tmp
                    ptx = tx
                    tx += dirs[c][0]
                if not passable: continue
                while tx != nx:
                    for l in ys[ptx]:
                        grid[ptx][l], grid[tx][l] = grid[tx][l], grid[ptx][l]
                    tx += -1 * dirs[c][0]
                    ptx += -1 * dirs[c][0]
                grid[nx][ny] = '@'
                grid[bot[0]][bot[1]] = '.'
                bot = (nx, ny)
    result = 0
    for x in range(len(grid)):
        l = ''
        for y in range(len(grid[0])):
            l += grid[x][y]
            if grid[x][y] == '[':
                result += 100 * x + y
        print(l)
    return result

puzzle(15, part1, part2, False, False).run()
