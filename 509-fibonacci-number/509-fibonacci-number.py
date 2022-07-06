class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        prev=0
        ans=1
        for i in range(n-1):
            temp=ans
            ans+=prev
            prev=temp
        return ans
        
            
        
        
        