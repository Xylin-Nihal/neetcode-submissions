class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited=set()
        def dfs(i,j):
            if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j]=="X" or (i,j) in visited:
                return
            visited.add((i,j))
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i-1,j)
            dfs(i,j+1)
        for i in range(len(board)):
            dfs(i,len(board[0])-1)
            dfs(i,0)
        for i in range(len(board[0])):
            dfs(0,i)
            dfs(len(board)-1,i)
        for i in range(len((board))):
            for j in range(len(board[0])):
                if board[i][j]=="O" and (i,j) not in visited:
                    board[i][j]="X"