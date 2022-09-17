class Solution:
    def findTargetSumWays(self, nums: List[int], tar: int) -> int:
        
        
        @lru_cache(None)
        def solve(i,tar):
            
            if i==0 and tar==0:
                return 1
            if i==0:
                return 0
            
            return solve(i-1,tar-nums[i-1])+solve(i-1,tar+nums[i-1])
        
        return solve(len(nums),tar)                 
                 
        