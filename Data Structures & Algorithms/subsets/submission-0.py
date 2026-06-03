class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        x=[]
        for num in nums:
            for subset in res:
                x.append(subset + [num]) 
            res+=x
            x=[]

        return res