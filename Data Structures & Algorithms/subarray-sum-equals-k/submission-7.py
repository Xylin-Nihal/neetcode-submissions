class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = cur = 0
        prefix = defaultdict(int)
        prefix[0] = 1
        for num in nums:
            cur += num
            if cur - k in prefix:
                res += prefix[cur - k]
            prefix[cur] += 1
        return res