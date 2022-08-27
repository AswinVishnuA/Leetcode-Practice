class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        n=len(nums)
        
        if n==1:
            return nums[0]
        
        def solve(i):
            
            preMax=0
            curMax=0
            for j in range(i,n-1+i):
                t=curMax
                curMax=max(preMax+nums[j],curMax)
                preMax=t
            # print(curMax)
            return curMax
        
        return max(solve(0),solve(1))
            
            
            
        