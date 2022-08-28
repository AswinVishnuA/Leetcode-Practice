class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n=len(coins)
        dp=[[float("inf") for _ in range(amount+1)] for i in range(n+1)]
        
        for i in range(n+1):
            dp[i][0]=0
        
        
        for i in range(n):
            for j in range(1,amount+1):
                
                if coins[i]>j:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=min(1+dp[i][j-coins[i]],dp[i-1][j])
        
        ans= dp[n-1][amount]
        
        return -1 if ans==float("inf") else ans