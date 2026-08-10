class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h=set()
        l=0
        c=0
        for r in range(len(s)):
            if s[r] in h:
                while l<r and s[r] in h:
                    h.remove(s[l])
                    l+=1
            h.add(s[r])
            c=max(c,r-l+1)
        return c
        