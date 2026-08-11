class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        r=0
        for i in s:
            if i==t[r]:
                r+=1
            if r>=len(t):
                break
        return len(t)-r