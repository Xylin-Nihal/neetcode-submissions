class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        cache=defaultdict()
        def dfs(i,j):
            if len(triangle)-1==i:
                cache[(i,j)]=triangle[i][j]
            if (i,j) in cache:
                return cache[(i,j)]
            cache[(i,j)]=triangle[i][j]+min(dfs(i+1,j),dfs(i+1,j+1))
            return cache[(i,j)]
        return dfs(0,0)
            