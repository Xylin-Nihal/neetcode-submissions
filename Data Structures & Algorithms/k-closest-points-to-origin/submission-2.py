class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        import math
        h=[]
        res=[]
        for i in range(len(points)):
            heapq.heappush(h,((math.sqrt(points[i][0]**2 + points[i][1]**2),points[i]))) 
        for i in range(k):
            res.append(heapq.heappop(h)[1])
        return res