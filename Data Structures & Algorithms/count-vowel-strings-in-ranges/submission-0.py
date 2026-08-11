class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        s={"a","e","i","o","u"}
        res=[]
        for l,r in queries:
            c=0
            for i in range(l,r+1):
                if words[i][0] in s and words[i][-1] in s:
                    c+=1
            res.append(c)

        return res