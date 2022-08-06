class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        
        
        n=len(nums)
        count=0
        for i in range(n-2,-1,-1):
            if nums[i]<=nums[i+1]:
                continue
            
            q=math.ceil(nums[i]/nums[i+1])
            count+=q-1
            nums[i]=nums[i]//q
        
        return count
            
            
            
            
        