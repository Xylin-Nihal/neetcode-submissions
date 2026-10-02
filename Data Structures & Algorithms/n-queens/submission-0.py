class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        board=[["."]*n for i in range(n)]
        col=set()
        negd=set()
        posd=set()

        def back(r):
            if r==n:
                copy=["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in col or r+c in negd or r-c in posd:
                    continue
                board[r][c]="Q"
                col.add(c)
                negd.add(r+c)
                posd.add(r-c)
                back(r+1)
                board[r][c]="."
                col.remove(c)
                negd.remove(r+c)
                posd.remove(r-c)
        back(0)
        return res