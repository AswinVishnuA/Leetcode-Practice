class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        length=len(cost)
        
        @lru_cache(None)
        def solve(n):
            if n==1 or n==0:
                return 0
            
            
            return min(cost[n-1]+solve(n-1),cost[n-2]+solve(n-2))
        
        
        return solve(length)
        