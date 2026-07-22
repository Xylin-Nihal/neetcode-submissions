class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        i=2
        
        
        while i<len(cost):
           cost[i]=cost[i]+min(cost[i-1],cost[i-2])
           i+=1
        return min(cost[-1],cost[-2]) 
            