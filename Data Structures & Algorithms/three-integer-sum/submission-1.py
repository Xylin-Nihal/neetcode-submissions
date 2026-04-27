class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)

        x=[]
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            while j<k:
                if -nums[i]==nums[j]+nums[k]:
                    x.append([nums[i],nums[j],nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                elif -nums[i]<nums[j]+nums[k]:
                    k-=1
                else:
                    j+=1
        return x
