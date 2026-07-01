class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        mc=0
        res=0
        for i in range(len(customers)):
            mc=max(customers[i][0]+customers[i][1],mc+customers[i][1])
            res+=mc-customers[i][0]
        return res/len(customers)
