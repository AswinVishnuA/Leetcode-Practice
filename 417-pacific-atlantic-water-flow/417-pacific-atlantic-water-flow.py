class Solution:
    def pacificAtlantic(self, h: List[List[int]]) -> List[List[int]]:
        
        m=len(h)
        n=len(h[0])
        ans=[]
        d=[[1,0],[-1,0],[0,1],[0,-1]]
        alt=set()
        pac=set()
        
        def dfs(i,j,vis):
            if (i,j) in vis:
                return
            vis.add((i,j))
            
            for dx,dy in d:
                r=i+dx
                c=j+dy
                if 0<=r<m and 0<=c<n:
                    if h[r][c]>=h[i][j]:
                        dfs(r,c,vis)
                
            
        
        
        for i in range(m):
            dfs(i,0,pac)
            dfs(i,n-1,alt)
            
        for i in range(n):
            dfs(0,i,pac)
            dfs(m-1,i,alt)
            
        return list(pac & alt)
        