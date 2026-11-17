class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        l=0
        r=0
        se=set()
        h={}
        res=[]
        for i in s:
            h[i]=1+h.get(i,0)
        for i in range(len(s)):
            se.add(s[i])
            h[s[i]]-=1
            if h[s[i]]==0:
                se.remove(s[i])
            if len(se)==0:
                res.append(i-r+1)
                r=i+1
        return res