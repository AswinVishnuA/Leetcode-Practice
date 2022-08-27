class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        n=len(nums)
        
        if n==1:
            return nums[0]
        
        
        dp=[[-1 for _ in range(n)] for i in range(2)]
        
        def solve(i,one):
            
            if i==n:
                return 0
            
            if i==n-1:
                
                if one:
                    return 0
                else:
                    return nums[n-1]
            if dp[one][i]!=-1:
                return dp[one][i]
            
            dp[one][i]=max(solve(i+2,one)+nums[i],solve(i+1,one))
            return dp[one][i]
        
        return max(nums[0]+solve(2,True),solve(1,False))
                
            
            
        