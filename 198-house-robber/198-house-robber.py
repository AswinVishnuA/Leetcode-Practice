class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n=len(nums)
        
        a=0
        b=nums[0]
        c=b
        for i in range(2,n+1):
            c=max(a+nums[i-1],b)
            a=b
            b=c
        
        return c