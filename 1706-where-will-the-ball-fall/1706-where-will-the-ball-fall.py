class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        
        m,n=len(grid),len(grid[0])
        
        def solve(i):
            
            for j in range(m):
                
                nextcol=i+ grid[j][i]
                
                if nextcol<0 or nextcol>=n or grid[j][i]!=grid[j][nextcol]:
                    return -1
                
                i=nextcol
            
            return i
        ans=[]
        for i in range(n):
            ans.append(solve(i))
        return ans