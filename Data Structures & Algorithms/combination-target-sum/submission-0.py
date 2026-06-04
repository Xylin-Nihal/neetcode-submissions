class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res,sol=[],[]
        def comb(n,l):
            if n==0:
                res.append(sol[:])
                return
            elif n<0:
                return
            for i in range(len(l)):
                y=i
                x=n-l[y]
                sol.append(l[y])
                comb(x,l[y:])
                sol.pop()
        comb(target,nums)
        return res
        