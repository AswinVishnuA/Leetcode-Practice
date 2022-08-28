class Solution:
    def countSubstrings(self, s: str) -> int:
        
        n=len(s)
        
        dp=[[0]*n for i in range(n)]
        
        for i in range(n):
            dp[i][i]=1
        
        for j in range(n):
            for i in range(j):
                
                if s[i]==s[j]:
                    
                    dp[i][j]=(j-i==1) or dp[i+1][j-1]
        
        ans=0
        for i in range(n):
            for j in range(n):
                ans+=dp[i][j]
        
        return ans
        
        