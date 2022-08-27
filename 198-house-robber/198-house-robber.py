class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n=len(nums)
        
        if n==1:
            return nums[0]
        
        a=nums[0]
        b=max(nums[1],nums[0])
        c=b
        for i in range(2,n):
            c=max(a+nums[i],b)
            a=b
            b=c
        
        return c