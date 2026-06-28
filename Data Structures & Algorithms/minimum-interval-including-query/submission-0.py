class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        '''x=sorted(intervals,key=lambda x: x[1]-x[0]+1)
        print(x)
        return [1,2,3]'''
        res=[]
        for i in queries:
            ac=float("inf")
            for j in intervals:
                if j[0]<=i<=j[1]:
                    c=j[1]-j[0]+1
                    ac=min(ac,c)
            if ac==float("inf"):
                ac=-1
            res.append(ac)
        return res