class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        if len(s)!=len(t):
            return False
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for j in t:
            if j in d:
                d[j]-=1
            else:
                return False
        for i in d:
            if d[i]!=0:
                return False
        return True
        