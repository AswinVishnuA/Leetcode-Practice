class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        count=[1] + [0]*(k-1)
        
        prefix=0
        res=0
        for v in nums:
            prefix=(prefix+v) % k
            
            res+=count[prefix]
            
            count[prefix]+=1
            
        return res
        
        
        
        