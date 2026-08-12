class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h={}
        c=1
        mc=1
        if len(nums)==0:
            return 0
        minn=min(nums)
        for i in nums:
            if i not in h:
                h[i]=1
        for i in range(len(nums)):
            if nums[i]-1 not in h:
                c=1
                x=nums[i]
                while (x+c) in h:
                    c+=1
                mc=max(c,mc)
        return mc
        


        