class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n=len(coins)
        # coins.sort()
#         @lru_cache(None)
#         def solve(i,tar):
            
#             if tar==0:
#                 return 1
            
#             if i==0:
#                 return 0
            
#             if coins[i-1]>tar:
#                 return solve(i-1,tar)
            
#             return solve(i,tar-coins[i-1]) + solve(i-1,tar)
        
#         return solve(n,amount)
        
        dp=[[0]*(amount+1) for i in range(n+1)]
        
        for i in range(n+1):
            dp[i][0]=1
        
        
        for i in range(1,n+1):
            for tar in range(1,amount+1):
                
                if coins[i-1]>tar:
                    dp[i][tar]=dp[i-1][tar]
                else:
                    dp[i][tar]=dp[i-1][tar]+dp[i][tar-coins[i-1]]
        
        return dp[n][amount]
                
            
        