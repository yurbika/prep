class Solution:
    def counter(self, i, j, grid):
        x = j
        y = i
        cnt = 0
        # top
        while y > -1:
            if grid[y][x] == 'E':
                cnt += 1
            if grid[y][x] == 'W':
                break
            y -= 1
        x = j
        y = i
        # bottom
        while y < len(grid):
            if grid[y][x] == 'E':
                cnt += 1
            if grid[y][x] == 'W':
                break
            y += 1
        x = j
        y = i
        # left
        while x > -1:
            if grid[y][x] == 'E':
                cnt += 1
            if grid[y][x] == 'W':
                break
            x -= 1

        x = j
        y = i
        # right
        while x < len(grid[i]):
            if grid[y][x] == 'E':
                cnt += 1
            if grid[y][x] == 'W':
                break
            x += 1

        return cnt

    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid or grid == []:
            return 0
        maxKills = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '0':
                    maxKills = max(maxKills, self.counter(i, j, grid))

        return maxKills
