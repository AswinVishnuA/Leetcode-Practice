class Solution:
    def maximumScore(self, nums: List[int], mults: List[int]) -> int:
        
        m=len(mults)
        n=len(nums)
        dp = [[0]*(m+1) for y in range(m+1)] 
        
        
        for op in range(m-1,-1,-1):
            for left in range(op,-1,-1):
                right=n-1-op+left
                
                dp[op][left]=max(nums[left]*mults[op]+dp[op+1][left+1],
                                 nums[right]*mults[op]+dp[op+1][left])
                
        
        
        return dp[0][0]
        
        