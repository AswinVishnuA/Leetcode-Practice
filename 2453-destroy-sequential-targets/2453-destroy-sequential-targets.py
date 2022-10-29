class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        
        c=Counter()
        maxval=0
        val=float("inf")
        for num in nums:
            c[num%space]+=1
        
        for num in nums:
            a=c[num%space]
            
            if a>maxval:
                val=num
                maxval=a
            elif a==maxval:
                val=min(num,val)
            
            
        return val
            
        