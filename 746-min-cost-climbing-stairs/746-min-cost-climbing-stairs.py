class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n=len(cost)
        a=0
        b=0
        c=0
        for i in range(2,n+1):
            c=min(a+cost[i-1],b+cost[i-2])
            b=a
            a=c
            
            
        return c
        