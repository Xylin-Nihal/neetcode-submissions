class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=[1]
        s=[1]
        x=1
        for i in range(1,len(nums)):
            x=x*nums[i-1]
            p.append(x)
        x=1
        for i in range(len(nums),1,-1):
            x=x*nums[i-1]
            s.append(x)
        s=s[::-1]
        for i in range(len(nums)):
            nums[i]=p[i]*s[i]
        return nums

