class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        x = sorted(candidates)
        res = []
        sol = []

        def comb(target, nums):
            if target == 0:
                res.append(sol[:])
                return

            if target < 0:
                return

            for i in range(len(nums)):
                # Skip duplicates at the same level
                if i > 0 and nums[i] == nums[i - 1]:
                    continue

                sol.append(nums[i])
                comb(target - nums[i], nums[i + 1:])
                sol.pop()

        comb(target, x)
        return res