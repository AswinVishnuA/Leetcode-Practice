class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        n=len(prices)
        
        @lru_cache(None)
        def solve(i,isSell):
            
            if i==n:
                return 0
            
            if isSell:
                
                sell=solve(i+1,False)+prices[i]-fee
                noSell=solve(i+1,True)
                return max(sell,noSell)
            else:
                
                buy=solve(i+1,True)-prices[i]
                noBuy=solve(i+1,False)
                return max(buy,noBuy)
        
        return solve(0,False)
        