class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sset=set()
        l=0
        r=0
        maxc=0
        while r<len(s):
            if s[r] not in sset:
                sset.add(s[r])
                r+=1
                c=r-l
                maxc=max(maxc,c)
            else:
                sset.remove(s[l])
                
                l+=1
        return maxc