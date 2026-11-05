class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        d=[]
        h={}
        for i in nums:
            h[i]=h.get(i,0)+1
        for i in set(nums):
            heapq.heappush(d,[-h[i],i])
        res=[]
        for i in range(k):
            res.append(heapq.heappop(d)[1])
        return res