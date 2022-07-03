class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        
        m=len(grid)
        n=len(grid[0])
        mod =(10**9) +7
        @cache
        def solve(i,j):
            
            dirs=[[1,0],[0,1],[0,-1],[-1,0]]
            ans=1
            for x,y in dirs:
                if 0<=i+x<m and 0<=j+y<n and grid[i+x][j+y]<grid[i][j]:
                    ans+=solve(i+x,j+y) 
            
            return ans
        
        return sum(solve(i,j) for j in range(n) for i in range(m)) % mod
                    


                        
                        
                        
                        
        