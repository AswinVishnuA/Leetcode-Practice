class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n=len(s)
        
        dp=[[False]*n for _ in range(n)]
        
        for i in range(n):
            dp[i][i]=True
        
        longest=s[0]
        curMax=1
        for j in range(n):
            for i in range(j):
                if s[i]==s[j]:
                    dp[i][j]= (j-i==1) or dp[i+1][j-1]
                    
                    if dp[i][j] and j-i+1>curMax:
                        curMax=j-i+1
                        longest=s[i:j+1]
        return longest
                    
                    
                
        