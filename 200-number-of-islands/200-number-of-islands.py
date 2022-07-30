class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        
        m=len(grid)
        n=len(grid[0])
        
        d=[[0,1],[0,-1],[1,0],[-1,0]]
        
        def dfs(i,j):
            
            grid[i][j]="0"
            
            for dx,dy in d:
                r=i+dx
                c=j+dy
                
                if r>=0 and c>=0 and r<m and c<n and grid[r][c]!="0":
                    dfs(r,c)
        
        
        count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]!="0":
                    count+=1
                    dfs(i,j)
        
        return count
                    