class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n=len(coins)
        dp=[[-1 for i in range(amount+1)] for i in range(n)]
        
        def solve(i,curSum):
            
            
            
            if curSum==amount:
                return 0
            
            if i==len(coins):
                return float("inf")
            
            if dp[i][curSum]!=-1:
                return dp[i][curSum]
            
            if coins[i]+curSum>amount:
                dp[i][curSum]= solve(i+1,curSum)
                return dp[i][curSum]
            
            dp[i][curSum]=min(1+solve(i,curSum+coins[i]),solve(i+1,curSum))
            return dp[i][curSum]
            
            
        ans=solve(0,0)
        return -1 if ans==float("inf") else ans
        