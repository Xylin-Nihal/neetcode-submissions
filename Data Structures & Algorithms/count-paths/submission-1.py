class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        h = {}

        def ways(x, y):

            if (x, y) in h:
                return h[(x,y)]

            if x == m-1 and y == n-1:
                return 1

            if x >= m or y >= n:
                return 0

            result = ways(x+1,y) + ways(x,y+1) 

            h[(x, y)] = result

            return result
        return ways(0,0)
