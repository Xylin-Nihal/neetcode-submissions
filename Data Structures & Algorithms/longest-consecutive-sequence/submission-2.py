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
            x=nums[i]
            while True:
                x+=1
                if x in h:
                    c+=1
                else:

                    break
            mc=max(mc,c)
            c=1
        return mc
        


        