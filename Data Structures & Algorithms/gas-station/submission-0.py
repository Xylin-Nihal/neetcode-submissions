class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            t=1
            l=i
            res=gas[l]
            while t:
                res=res-cost[l]
                if res<0:
                    
                    break
                l=(l+1)%len(gas)
                if l==i:
                    return i
                res+=gas[l]
                print(res,l)
                
        return -1   



