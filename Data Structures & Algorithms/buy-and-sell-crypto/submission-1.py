class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        maxx=0
        for i in range(1,len(prices)):
            if prices[i]<prices[l]:
                l=i
            c=prices[i]-prices[l]
            maxx=max(maxx,c)
        return maxx