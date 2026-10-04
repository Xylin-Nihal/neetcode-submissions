class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.x,self.k=nums,k
        heapq.heapify(self.x)
        while len(self.x)>self.k:
            heapq.heappop(self.x)

    def add(self, val: int) -> int:
        heapq.heappush(self.x,val)
        while len(self.x)>self.k:
            heapq.heappop(self.x)
        return self.x[0]

        
