class Solution:
    def climbStairs(self, n: int) -> int:
        
        @lru_cache(None)
        def solve(n):
            
            if n==0:
                return 1
            if n<0:
                return 0
            
            return solve(n-1)+solve(n-2)
        return solve(n)
        

        '''
        f(0)=0
        f(1)=1
        
        
        f(n)=f(n-1)+f(n-2)
        '''
        