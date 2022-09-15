class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        n=len(prices)
        
        dp=[[-1,-1] for _ in range(n+1)]
        
        
        def solve(i,toSell):
            
            if i>=n:
                return 0
            
            if dp[i][toSell]!=-1:
                return dp[i][toSell]
            
            if toSell:
                
                sell=solve(i+2,False)+prices[i]
                noSell=solve(i+1,True)
                dp[i][toSell]= max(sell,noSell)
                return dp[i][toSell]
            else:
                buy=solve(i+1,True)-prices[i]
                noBuy=solve(i+1,False)
                dp[i][toSell]=max(buy,noBuy)
                return dp[i][toSell]
            
        return solve(0,False)
        