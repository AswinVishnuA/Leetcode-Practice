class Solution:
    def findTargetSumWays(self, nums: List[int], tar: int) -> int:
        dp=dict()
        def solve(idx,csum):
            if csum==tar and idx==len(nums):
                return 1
            if idx==len(nums):
                return 0
            
            if (csum,idx) in dp:
                return dp[(csum,idx)]
            
            dp[(csum,idx)]=solve(idx+1,csum-nums[idx])+solve(idx+1,csum+nums[idx])
            return dp[(csum,idx)]
                
        return solve(0,0)      
        