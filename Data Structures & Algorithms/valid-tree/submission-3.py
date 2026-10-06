class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        h = {i: [] for i in range(n)}

        for i, j in edges:
            h[i].append(j)
            h[j].append(i)

        visited = set()

        def dfs(node, parent):

            if node in visited:
                return False

            visited.add(node)

            for nei in h[node]:

                if nei == parent:
                    continue

                if not dfs(nei, node):
                    return False

            return True

        if not dfs(0, -1):
            return False

        return len(visited) == n