
from typing import List
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        h = [(grid[0][0], 0, 0)]
        visited = set()

        while h:
            t, i, j = heapq.heappop(h)

            if (i, j) in visited:
                continue

            visited.add((i, j))

            if i == n - 1 and j == n - 1:
                return t

            for ni, nj in [
                (i - 1, j),
                (i + 1, j),
                (i, j - 1),
                (i, j + 1)
            ]:
                if 0 <= ni < n and 0 <= nj < n:
                    if (ni, nj) not in visited:
                        new_time = max(t, grid[ni][nj])
                        heapq.heappush(h, (new_time, ni, nj))
