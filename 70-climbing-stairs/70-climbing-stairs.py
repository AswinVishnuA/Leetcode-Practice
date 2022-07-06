class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n==0:
            return 0
        
        
        
        prev=0
        ans=1
        for i in range(n):
            temp=ans
            ans+=prev
            prev=temp
        
        return ans
        
        

        '''
        f(0)=0
        f(1)=1
        
        
        f(n)=f(n-1)+f(n-2)
        '''
        