
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m=len(grid)
        n=len(grid[0])
        
        l=[]
        empty=0
        good=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    l.append([i,j])
                elif grid[i][j]==0:
                    empty+=1
                else:
                    good+=1
                    
                
        
        q=deque(l)
        rot=len(l)
        
        if empty+rot==m*n:
            return 0
        
#         if empty+good==m*n:
#             return -1
        
        vis=set()
        
        minutes=0
            
        d=[[1,0],[0,1],[-1,0],[0,-1]]
        
        while len(q):
            size=len(q)
            # print(size)
            while size:
                
                i,j= q.popleft()
                
                # print(i,j)
                
                if grid[i][j]==1:
                    good-=1
                
                grid[i][j]=2
                
                if good==0:
                    q=[]
                    break
                
                
                for dx,dy in d:
                    r=i+dx
                    c=j+dy
                    if r>=0 and c>=0 and r<m and c<n and grid[r][c]!=2  and grid[r][c]!=0:
                        q.append([r,c])
                
                size-=1
            minutes+=1
            print("min:",minutes)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    return -1
        
        return minutes-1
        
        
        