class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        c=[0]*26
        c2=[0]*26
        for i in s1:
            c[ord(i)-ord("a")]+=1
        for j in range(len(s1)):
            c2[ord(s2[j])-ord("a")]+=1
        if c==c2:
            return True
        l=0
        for r in range(len(s1),len(s2)):
            c2[ord(s2[l])-ord("a")]-=1
            c2[ord(s2[r])-ord("a")]+=1
            if c==c2:
                return True
            l+=1
        return False
        
