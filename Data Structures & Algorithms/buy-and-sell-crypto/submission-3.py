class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        mc=0
        for r in range(len(prices)):
            if prices[l]>prices[r]:
                l=r
            mc=max(mc,prices[r]-prices[l])
        return mc
