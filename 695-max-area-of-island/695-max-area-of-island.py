class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        m=len(grid)
        n=len(grid[0])
        visited=[[0 for i in range(n)] for j in range(m)]
        
        def solve(i,j):
            # print(i,j)
            if i<0 or j<0 or i>=m or j>=n or grid[i][j]==0 or visited[i][j]:
                return 0
            
            visited[i][j]=1
            
            
            
            dr=[1,-1,0,0]
            dc=[0,0,1,-1]
            
            area=1
            for d in range(4):
                r=i+dr[d]
                c=j+dc[d]
                area+=solve(r,c)
            
            return area
        
        maxval=0
        for i in range(m):
            for j in range(n):
                maxval=max(maxval,solve(i,j))
                
        return maxval
        