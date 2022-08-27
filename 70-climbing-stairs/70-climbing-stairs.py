class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp=[0 for i in range(n+1)]
        
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1):
            
            dp[i]=dp[i-1]+dp[i-2]
        
        return dp[n]
        

        '''
        f(0)=0
        f(1)=1
        
        
        f(n)=f(n-1)+f(n-2)
        '''
        