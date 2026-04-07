class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        for i in range(len(nums)):
            x=target-nums[i]
            if x in h and h[x]!=i:
                l=[h[x],i]
                return l
            else:
                h[nums[i]]=i