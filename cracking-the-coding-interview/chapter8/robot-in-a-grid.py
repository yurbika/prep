import random

r = 10
c = 10


grid = [['o' for j in range(c)] for i in range(r)]


for i in range(20):
    grid[random.randint(0, r - 1)
         ][random.randint(0, c - 1)
           ] = 'X'

# for i in grid:
#     print(i)


def findPath(grid, r, c, curPosX, curPosY, path, memo):
    if grid[0][0] == 'X':
        return False

    if curPosY == (r-1) and curPosX == (c-1):
        path = True
        grid[curPosY][curPosX] = '#'
        return path

    if curPosX == len(grid[r-1]):
        return path

    if curPosY == len(grid):
        return path

    if grid[r-1][c-1] == 'X':
        return False

    if grid[curPosY][curPosX] == 'X' or (curPosX, curPosY) in memo:
        return path

    grid[curPosY][curPosX] = '#'

    if not path:
        path = findPath(grid, r, c, curPosX+1, curPosY, path, memo)

    if not path:
        path = findPath(grid, r, c, curPosX, curPosY+1, path, memo)

    if not path:
        grid[curPosY][curPosX] = 'o'
        memo += [(curPosX, curPosY)]

    return path


if findPath(grid, r, c, 0, 0, False, []):
    for i in grid:
        print(i)
