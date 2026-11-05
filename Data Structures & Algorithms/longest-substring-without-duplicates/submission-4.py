class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h=set()
        c=0
        l=0
        for r in range(len(s)):
            if s[r] in h:
                while s[r] in h and l<r:
                    h.remove(s[l])
                    l+=1
            h.add(s[r])
            c=max(c,len(h))
        return c
        