class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        wordDict = set(wordDict)
        memo = {}

        def dfs(l):
            if l == len(s):
                return True

            if l in memo:
                return memo[l]

            for r in range(l + 1, len(s) + 1):

                if s[l:r] in wordDict:
                    if dfs(r):
                        memo[l] = True
                        return True

            memo[l] = False
            return False

        return dfs(0)