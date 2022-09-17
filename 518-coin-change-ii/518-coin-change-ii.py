class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n=len(coins)
        # coins.sort()
        @lru_cache(None)
        def solve(i,tar):
            
            if tar==0:
                return 1
            
            if i==0:
                return 0
            
            if coins[i-1]>tar:
                return solve(i-1,tar)
            
            return solve(i,tar-coins[i-1]) + solve(i-1,tar)
        
        return solve(n,amount)
            
        