class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h={}
        res=[]
        y=[]
        import heapq
        for i in nums:
            if i in h:
                h[i]+=1
                
            else:
                h[i]=1
        for x,i in h.items():
            heapq.heappush(y,(-i,x))
        for i in range(k):
            res.append(heapq.heappop(y)[1])
        return res
