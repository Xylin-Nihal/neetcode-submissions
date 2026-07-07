class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=s[0]
        for i in range(len(s)):
            for j in range(i, len(s)+1):
                if s[i:j]==s[i:j][::-1]:
                    if len(s[i:j])>len(res):
                        res=s[i:j]
        return res