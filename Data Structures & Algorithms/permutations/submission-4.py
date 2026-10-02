class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        sol=[]
        h={}
        for i in nums:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
        def perm(sol,nums,h):
            if len(sol)==len(nums) and sol not in res:
                res.append(sol[:])
                return
            elif sol in res:
                sol.pop()
                h[nums[i]]+=1
                return
            for i in range(len(nums)):
                if h[nums[i]]>0:
                    h[nums[i]]-=1
                    sol.append(nums[i])
                    perm(sol,nums,h)
                    sol.pop()
                    h[nums[i]]+=1
        perm(sol,nums,h)
        return res

        