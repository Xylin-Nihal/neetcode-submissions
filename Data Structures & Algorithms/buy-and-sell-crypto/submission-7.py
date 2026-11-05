class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mc=0
        l=prices[0]
        for i in range(1,len(prices)):
            if prices[i]>l:
                mc=max(mc,prices[i]-l)
                print(mc)
            else:
                l=prices[i]
                print("no")
        return mc