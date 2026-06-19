class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        h={}
        for i in s:
            h[i]=1+h.get(i,0)
        c=0
        res=[]
        k=set()
        for i in range(len(s)):
            h[s[i]]-=1
            if s[i] not in k:
                k.add(s[i])
            c+=1
            if h[s[i]]==0:
                k.remove(s[i])
                if k==set():
                    res.append(c)
                    c=0
        return res 
                