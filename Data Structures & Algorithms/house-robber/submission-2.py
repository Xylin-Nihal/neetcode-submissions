class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums)
        x=[-1]*len(nums)
        x[0],x[1]=nums[0],nums[1]
        for i in range(len(nums)):
            for j in range(i+2,len(nums)):
                x[j]=max(x[j],x[i]+nums[j])
        return max(x[-1],x[-2])
        