class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sol = []

        def comb(remaining, start):
            if remaining == 0:
                res.append(sol[:])
                return

            if remaining < 0:
                return

            for i in range(start, len(nums)):
                sol.append(nums[i])
                comb(remaining - nums[i], i)  # i, not i+1
                sol.pop()

        comb(target, 0)
        return res