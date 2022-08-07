class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        d=[[0,1],[0,-1],[1,0],[-1,0]]
        
        m=len(board)
        n=len(board[0])
        
        def dfs(i,j):
            
            board[i][j]=-1
            
            for dx,dy in d:
                r=i+dx
                c=j+dy
                if r>=0 and c>=0 and r<m and c<n and board[r][c]!=-1 and board[r][c]!="X":
                    dfs(r,c)
        
            
        
        
        for i in range(m):
            if board[i][0]!=-1 and board[i][0]!="X":
                    dfs(i,0)
            if board[i][n-1]!=-1 and board[i][n-1]!="X":
                    dfs(i,n-1)
        
        
        for j in range(n):
            if board[0][j]!=-1 and board[0][j]!="X":
                    dfs(0,j)
            if board[m-1][j]!=-1 and board[m-1][j]!="X":
                    dfs(m-1,j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j]==-1:
                    board[i][j]="O"
                else:
                    board[i][j]="X"
        
            
            
        