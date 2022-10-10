class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        nums.sort()
        
        n=len(nums)
        
        if n<=4:
            return 0
        
        ans=float("inf")
        for i in range(4):
            curMin=nums[i]
            curMax=nums[n-1-(3-i)]
            ans=min(ans,abs(curMax-curMin))
        
        return ans
            
            
        