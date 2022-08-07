class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        
        n=len(nums)
        @lru_cache(None)
        def solve(i):
            if i==n:
                return True
            ans=False
            if i+2<n:
                
                if nums[i]==nums[i+1]==nums[i+2] or nums[i]==nums[i+1]-1==nums[i+2]-2:
                    ans=ans or solve(i+3)
                
            if i+1<n:
                
                if nums[i]==nums[i+1]:
                    ans=ans or solve(i+2)
            
            return ans
        
        
        
        
        
        return solve(0)
            
        
        
        