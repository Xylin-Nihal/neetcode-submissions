class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        x = deque()
        c = 0
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    c += 1
                elif grid[i][j] == 2:
                    x.append([i, j])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        while x and c > 0:
            size = len(x)
            for _ in range(size):
                m, n = x.popleft()
                for k, l in directions:
                    if (0 <= m+k < len(grid) and
                        0 <= n+l < len(grid[0]) and
                        grid[m+k][n+l] == 1):
                        x.append([m+k, n+l])
                        grid[m+k][n+l] = 2
                        c -= 1
            res += 1
        if c == 0:
            return res
        return -1