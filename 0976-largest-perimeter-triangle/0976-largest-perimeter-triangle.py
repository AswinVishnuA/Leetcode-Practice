class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        
        nums.sort()
        n=len(nums)
        for j in range(n-1,1,-1):
            a=nums[j]
            b=nums[j-1]
            for i in range(j-2,-1,-1):
                if nums[i]+b>a:
                    return a+b+nums[i]
        
        return 0
        