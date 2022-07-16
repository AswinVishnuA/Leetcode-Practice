class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        @lru_cache(None)
        def dfs(i,j,moves):
            
            if (i>=m or j>=n or i<0 or j<0) and moves<=maxMove:
                return 1
            
            if moves==maxMove:
                return 0
            
            dr=[1,-1,0,0]
            dc=[0,0,1,-1]
            
            ans=0
            for a in range(4):
                ans+=dfs(i+dr[a],j+dc[a],moves+1)
            
            
            return ans % (7+10**9)
        
        
        return dfs(startRow,startColumn,0)
        