class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
#         len1=len(text1)
#         len2=len(text2)
        
#         @lru_cache(None)
#         def solve(m,n):
            
#             if m==0 or n==0:
#                 return 0
            
#             ans=0
            
#             if text1[m-1]==text2[n-1]:
#                 ans=1+solve(m-1,n-1)
            
#             ans=max(ans,solve(m-1,n),solve(m,n-1))
            
#             return ans
        
        
#         return solve(len1,len2)
        
        m=len(text1)
        n=len(text2)
        
        dp=[0]*(n+1)
        
        for i in range(1,m+1):
            prevRow=dp.copy()
            for j in range(1,n+1):
                
                if text1[i-1]==text2[j-1]:
                    dp[j]=1+prevRow[j-1]
                
                dp[j]=max(dp[j],prevRow[j],dp[j-1])
        
        return dp[n]
                    
        
        