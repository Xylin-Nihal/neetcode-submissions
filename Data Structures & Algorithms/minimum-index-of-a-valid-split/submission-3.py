class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count = {}
        
        for x in nums:
            count[x] = count.get(x, 0) + 1
        
        dominant = max(count, key=count.get)
        total = count[dominant]
        left = 0
        n = len(nums)
        
        for i in range(n):
            if nums[i] == dominant:
                left += 1
            
            right = total - left
            
            if left * 2 > i + 1 and right * 2 > n - i - 1:
                return i
        
        return -1