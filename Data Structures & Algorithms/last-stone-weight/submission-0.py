class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [stone * -1 for stone in stones]
        heapq.heapify(stones)

        while len(stones) >= 2:
            print(stones)
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            x = x-y
            
            heapq.heappush(stones,x)
        return stones[0]*-1