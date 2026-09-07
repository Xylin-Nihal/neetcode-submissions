class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        res=[]
        s=[]
        h={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxzy"}
        def dfs(i):
            if i==len(digits):
                res.append("".join(s))
                return
            for j in h[int(digits[i])]:
                s.append(j)
                dfs(i+1)
                s.pop()
            return
        dfs(0)
        return res
                