class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            x={}
            y={}
            for j in range(9):
                if board[i][j] in x:
                    return False
                if board[i][j]!=".":
                    x[board[i][j]]=1
                if board[j][i] in y:
                    return False
                if board[j][i]!=".":
                    y[board[j][i]]=1
            seen=set()
            for k in range(3):
                for j in range(3):
                    row = (i//3) * 3 + k
                    col = (i % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True
                
