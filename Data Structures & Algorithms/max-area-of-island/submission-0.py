class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        c = 0
        maxc = 0

        def dfs(i, j):
            nonlocal c
            c += 1
            grid[i][j] = 0

            if i + 1 < len(grid) and grid[i + 1][j] == 1:
                dfs(i + 1, j)

            if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
                dfs(i, j + 1)

            if i - 1 >= 0 and grid[i - 1][j] == 1:
                dfs(i - 1, j)

            if j - 1 >= 0 and grid[i][j - 1] == 1:
                dfs(i, j - 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i, j)
                    maxc = max(maxc, c)
                    c = 0

        return maxc