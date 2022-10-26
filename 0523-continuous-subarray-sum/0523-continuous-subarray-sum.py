class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        d={0:-1}
        
        sumval=0
        for i,val in enumerate(nums):
            
            if k==0:
                sumval+=val
            else:
                sumval=(sumval+val)%k
            
            if sumval in d:
                
                if i-d[sumval]>=2:
                    return True
            else:
                d[sumval]=i
            
        return False