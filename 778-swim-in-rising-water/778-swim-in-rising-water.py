class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        n=len(grid)
        
        pq=[[grid[0][0],0,0]]
        
        vis=set()
        
        d=[[0,1],[1,0],[0,-1],[-1,0]]
        
        while len(pq)!=0:
            
            cur,i,j=heappop(pq)
            
            if i==n-1 and j==n-1:
                return cur
            
            for dx,dy in d:
                
                r,c=i+dx,j+dy
                
                if n>r>=0 and n>c>=0 and (r,c) not in vis:
                    
                    vis.add((r,c))
                    
                    heappush(pq,[max(grid[r][c],cur),r,c])
        
        return -1
                
            
            
        