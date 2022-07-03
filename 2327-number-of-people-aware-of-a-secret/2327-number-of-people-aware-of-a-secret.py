class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        
        
        dp = [0,1] + [0]* (n-1)
        mod=10**9 +7
        share=0
        for i in range(2,n+1):
            
            dp[i]=share=(share+dp[max(i-delay,0)]-dp[max(0,i-forget)]) %mod
            
            
        return sum(dp[-forget:]) % mod
        