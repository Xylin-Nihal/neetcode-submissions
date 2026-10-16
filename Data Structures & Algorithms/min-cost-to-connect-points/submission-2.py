class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n = len(points)

        visited = [False] * n
        min_dist = [float('inf')] * n

        min_dist[0] = 0

        total = 0

        for _ in range(n):

            # Find unvisited point with minimum distance
            u = -1

            for i in range(n):
                if not visited[i] and (u == -1 or min_dist[i] < min_dist[u]):
                    u = i

            # Add its cost
            visited[u] = True
            total += min_dist[u]

            # Update distances to other points
            for v in range(n):

                if not visited[v]:

                    x1, y1 = points[u]
                    x2, y2 = points[v]

                    dist = abs(x1 - x2) + abs(y1 - y2)

                    min_dist[v] = min(min_dist[v], dist)

        return total