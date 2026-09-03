class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        c=0
        mm=0
        for i in range(len(prices)-1,0,-1):
            if prices[i]>=prices[i-1]:

                c=max(prices[i]-prices[i-1]+c,mm-prices[i])
            mm=max(prices[i],mm)
        return c