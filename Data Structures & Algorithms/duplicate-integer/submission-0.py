class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x={}
        for i in nums:
            if i in x:
                return True
            else:
                x[i]=1
        return False
        