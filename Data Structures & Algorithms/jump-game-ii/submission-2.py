class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        steps = nums[0]
        jumps = 1
        farthest = nums[0]

        for i in range(1, len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            steps -= 1

            if steps == 0:
                jumps += 1
                steps = farthest - i

        return jumps