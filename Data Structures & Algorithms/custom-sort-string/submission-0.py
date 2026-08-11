class Solution:
    def customSortString(self, order: str, s: str) -> str:
        h=set()
        res=""
        for i in order:
            h.add(i)
            for j in s:
                if i==j:
                    res+=i
        for i in s:
            if i not in h:
                res+=i
        return res