class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        
#         @lru_cache(None)
#         def solve(i,j):
            
#             if i==m or j==n or i<0 or j<0:
#                 return 0
            
            
#             if i==m-1 and j==n-1:
#                 return 1
            
#             return solve(i+1,j)+solve(i,j+1)
        
#         return solve(0,0)
        
        dp=[[0 for i in range(n)] for _ in range(m)]
        
        
        
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    dp[i][j]=1
                    continue
                dp[i][j]=dp[i][j-1]+dp[i-1][j]
        
        return dp[m-1][n-1]