class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        n=len(prices)
        
        dp=[[0 for i in range(n+1)] for _ in range(k+1)]
        
        if n<1:
            return 0
        
        for i in range(1,k+1):
            maxval=-prices[0]
            for j in range(1,n):
                
                dp[i][j]=max(dp[i][j-1],prices[j]+maxval)
                maxval=max(maxval,dp[i-1][j-1]-prices[j])
                
        
        return dp[k][n-1]
                
        