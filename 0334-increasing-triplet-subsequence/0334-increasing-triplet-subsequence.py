class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        n=len(nums)
        
        threshold1,threshold2=float("inf"),float("inf")
        
        for val in nums:
            
            if val <=threshold1:
                threshold1=val
            elif val<=threshold2:
                threshold2=val
            else:
                return True
        
        
        return False
            
        
        
        