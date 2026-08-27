class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = defaultdict(tuple)
        wordDict = set(wordDict)

        def dfs(l, r):
            if (l, r) in memo:
                return memo[(l, r)]

            if l >= len(s):
                return True

            if r >= len(s):
                return False

            x = r

            while l < len(s) and r < len(s):

                if s[l:r+1] in wordDict:

                    if r == len(s) - 1:
                        return True

                    if dfs(r+1, r+1):
                        return True

                r += 1

            memo[(l, x)] = False
            return False

        return dfs(0, 0)