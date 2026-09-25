class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo={}
        def dfs(n):
            if n in memo:
                return memo[n]
            ans = 1

            for i in range(n + 1, len(nums)):
                if nums[i] > nums[n]:
                    ans = max(ans,1+ dfs(i))
            memo[n]=ans
            return memo[n]

        k = [1] * len(nums)

        for i in range(len(nums)):
            k[i] = dfs(i)

        return max(k)