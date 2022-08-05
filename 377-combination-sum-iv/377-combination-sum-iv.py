class Solution:
    
    
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        
        
        @lru_cache(None)
        def solve(target):
            if target==0:
                return 1


            res=0

            for i in range(len(nums)):
                if target>=nums[i]:
                    res+=solve(target-nums[i])

            return res
        
        return solve(target)
        
    
    
    
        
        