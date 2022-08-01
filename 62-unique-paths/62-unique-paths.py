class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        
        @lru_cache(None)
        def solve(i,j):
            
            if i==m or j==n or i<0 or j<0:
                return 0
            
            
            if i==m-1 and j==n-1:
                return 1
            
            return solve(i+1,j)+solve(i,j+1)
        
        return solve(0,0)
        