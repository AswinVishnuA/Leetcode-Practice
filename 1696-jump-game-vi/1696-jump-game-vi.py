class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
        length=len(nums)
        
#         @lru_cache(None)
#         def solve(n):
#             if n<=0:
#                 return float("-inf")
#             if n==1:
#                 return nums[0]
#             ans=float("-inf")
            
#             for i in range(1,k+1):
#                 ans=max(ans,nums[n-1]+solve(n-i))
            
#             return ans
        
        
        
#         return solve(length)

        
        dp=[0 for i in range(length)]
        dp[0]=nums[0]
        dq=deque([(nums[0],0)])
        
        for i in range(1,length):
            
            dp[i]=nums[i]+dq[0][0]
            
            while(dq and dq[-1][0]<dp[i]):
                dq.pop()
            
            dq.append((dp[i],i))
            
            if i-k==dq[0][1]:
                dq.popleft()
            
        return dp[-1]
            
        
        
        
        
        