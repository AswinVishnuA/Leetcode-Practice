class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        n=len(nums)
        
        maxvals=[0 for i in range(n)]
        minvals=[0 for i in range(n)]
        
        maxvals[0]=nums[0]
        minvals[0]=nums[0]
        
        for i in range(1,n):
            maxvals[i]=max(maxvals[i-1]*nums[i],minvals[i-1]*nums[i],nums[i])
            minvals[i]=min(maxvals[i-1]*nums[i],minvals[i-1]*nums[i],nums[i])
        
        return max(maxvals)
                
            