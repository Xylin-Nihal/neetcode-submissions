class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        h={ i:[] for i in range(n)}
        for i,j in edges:
            h[i].append(j)
            h[j].append(i)
        visited=set()
        c=0
        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for j in h[i]:
                if j not in visited:
                    dfs(j)
        for i in range(n):
            if i not in visited:
                dfs(i)
                c+=1
        return c
