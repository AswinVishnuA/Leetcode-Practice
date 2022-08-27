class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        n=len(nums)
        
        if n==1:
            return nums[0]
        
        
        dp=[[-1 for _ in range(n+1)] for i in range(2)]
        
        dp[0][0]=0
        dp[1][0]=0
        dp[0][1]=0
        dp[1][1]=nums[0]
        
        for i in range(2,n+1):
            if i==n:
                dp[0][i]=max(dp[0][i-2]+nums[i-1],dp[0][i-1])
                dp[1][i]=max(dp[1][i-2],dp[1][i-1])    
            else:
                dp[0][i]=max(dp[0][i-2]+nums[i-1],dp[0][i-1])
                dp[1][i]=max(dp[1][i-2]+nums[i-1],dp[1][i-1])

        # print(dp)    
        return max(dp[0][n],dp[1][n])
            
            
            
        