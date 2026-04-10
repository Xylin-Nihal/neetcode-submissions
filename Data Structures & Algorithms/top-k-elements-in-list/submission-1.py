class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h={}
        l=[[] for i in range(len(nums)+1)]
        x=[]
        for i in nums:
            if i in h:
                h[i]+=1
                
            else:
                h[i]=1
        for n,p in h.items():
            l[p].append(n)
        for i in range(len(l)-1,0,-1):
            for n in l[i]:
                x.append(n)
                if len(x)==k:
                    return x
                
