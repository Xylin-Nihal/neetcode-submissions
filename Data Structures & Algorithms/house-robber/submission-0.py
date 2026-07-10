class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        m1=max(nums[0],nums[1])
        m2=min(nums[0],nums[1])
        for i in range(2,len(nums)):
            if nums[i-1]==m1:
                nums[i]=nums[i]+m2
            else:
                nums[i]=nums[i]+m1
            
            
            m2=min(nums[i],m1)
            m1=max(nums[i],m1)
            
            
        return m1

