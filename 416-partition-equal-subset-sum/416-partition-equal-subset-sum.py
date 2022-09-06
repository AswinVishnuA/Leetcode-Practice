class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        sumVal=sum(nums)
        
        if sumVal%2==1:
            return False
        
        n=len(nums)
        
        tar=sumVal//2
        
        dp=[[0]*(n+1) for i in range(tar+1) ]
        
        for i in range(n+1):
            dp[0][i]=1
        
        
        for i in range(1,n+1):
            for j in range(1,tar+1):
                
                if nums[i-1]>j:
                    dp[j][i]=dp[j][i-1]
                else:
                    dp[j][i]=max(dp[j-nums[i-1]][i-1],dp[j][i-1])
        
        return dp[tar][n]