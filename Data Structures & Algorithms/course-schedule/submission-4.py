class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre={i:[] for i in range(numCourses)}
        visited=set()
        for i,j in  prerequisites:
            pre[i].append(j)
        def dfs(i):
            if i in visited:
                return False
            if pre[i]==[]:
                return True
            visited.add(i)
            for j in pre[i]:
                if not dfs(j):
                    return False
            visited.remove(i)
            pre[i]=[]
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True