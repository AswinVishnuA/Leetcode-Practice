class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        
        imin,imax=-1,-1
        j=0
        res=0
        for i,val in enumerate(nums):
            
            if not (minK<=val<=maxK):
                j=i+1
                imin=-1
                imax=-1
            
            if val==minK:
                imin=i
            
            if val==maxK:
                imax=i
            
            res+=max(0,min(imax,imin)-j+1)
        
        return res
                
        