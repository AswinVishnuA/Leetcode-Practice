class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        
        nr=len(grid)
        nc=len(grid[0])
        
        for i in range(nr):
            for j in range(nc):
                
                if (i==j or i+j+1==nc):
                    if grid[i][j]==0:
                        print(i,j)
                        return False
                else:
                    if grid[i][j]!=0:
                        print(i,j)
                        return False
        return True
                
                    
        