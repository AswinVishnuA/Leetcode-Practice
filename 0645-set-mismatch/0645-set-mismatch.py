class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        n=len(nums)
        s=set(range(1,n+1))
        s2=set(nums)
        
        val=(s-s2).pop()
        
        c=Counter(nums)
        
        for val2 in c:
            if c[val2]==2:
                return [val2,val]
        
        return None
        