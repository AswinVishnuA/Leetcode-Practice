class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        len1=len(text1)
        len2=len(text2)
        
        @lru_cache(None)
        def solve(m,n):
            
            if m==0 or n==0:
                return 0
            
            ans=0
            
            if text1[m-1]==text2[n-1]:
                ans=1+solve(m-1,n-1)
            
            ans=max(ans,solve(m-1,n),solve(m,n-1))
            
            return ans
        
        
        return solve(len1,len2)
        