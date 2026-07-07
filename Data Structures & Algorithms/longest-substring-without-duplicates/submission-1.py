class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h=set()
        l=0
        res=0      
        for r in range(len(s)):
            if s[r] in s:   
                while l<r and s[r] in h:
                    h.remove(s[l])
                    l+=1
            res=max(res,r-l+1)
            h.add(s[r])
        return res