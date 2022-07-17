class Solution:
    @lru_cache(None)
    def kInversePairs(self, n: int, k: int) -> int:
        
        if n==0:
            return 0
        if k==0:
            return 1
        
        dp=[[0 for i in range(k+1)] for j in range(n+1)]
        
        for N in range(1,n+1):
            for K in range(k+1):
                if K==0:
                    dp[N][K]=1
                else:
                    if K-N<0:#min(K,N)==K:
                        dp[N][K]=(dp[N][K-1]+dp[N-1][K])%(10**9 +7)
                    else:
                        dp[N][K]=(dp[N][K-1]+dp[N-1][K]-dp[N-1][K-N]) %(10**9 +7)
        
        return (dp[n][k]-dp[n][k-1])%(10**9 +7)
        