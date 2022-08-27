class Solution:
    def climbStairs(self, n: int) -> int:
        
        c=1
        a=1
        b=1
        for i in range(2,n+1):
            c=a+b
            a=b
            b=c
        
        return c
        

        '''
        f(0)=0
        f(1)=1
        
        
        f(n)=f(n-1)+f(n-2)
        '''
        