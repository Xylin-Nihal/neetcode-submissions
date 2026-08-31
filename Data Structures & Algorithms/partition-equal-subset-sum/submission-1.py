class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        x=sum(nums)/2
        if x!=sum(nums)//2:
            return False
        def find(i,s):
            if s>x:
                return False
            if s==x:
                return True
            
            for j in range(i+1,len(nums)):
                
                
                if find(j,s+nums[j]) or find(j,s):
                    return True
            return False
        return find(0,nums[0])


        