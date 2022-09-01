class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        sumVal=sum(nums)
        
        if sumVal%2==1:
            return False
        
        n=len(nums)
        
        dp=[[-1]*n for i in range((sumVal//2)+1) ]
        
        def solve(i,tar):
            
            if i == n:
                return tar==0
            
            if tar==0:
                return True
            
            if dp[tar][i]!=-1:
                return dp[tar][i]
            
            if nums[i]>tar:
                dp[tar][i]= solve(i+1,tar)
                return dp[tar][i]
            
            dp[tar][i]= solve(i+1,tar-nums[i]) or solve(i+1,tar)
            
            return dp[tar][i]
            
            
        
        return solve(0,sumVal//2)
        