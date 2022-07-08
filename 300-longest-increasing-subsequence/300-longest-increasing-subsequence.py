class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
#         n=len(nums)
#         # @lru_cache(None)
#         def solve(n):
#             if n==0 or n==1:
#                 return n
            
#             ans =solve(n-1)
            
#             for i in range(n-1):
                
#                 if nums[i]<nums[n-1]:
#                     ans=max(ans,1+solve(i+1))
            
#             print(n,"____")
#             print(ans)
            
#             return ans        
        
#         return solve(n)


        n=len(nums)
        dp=[1 for i in range(n)]
            
        
        for i in range(n):
            
            for j in range(i):
                # print(dp,i,j)

                if nums[i]>nums[j] and dp[i]<dp[j]+1:
                    dp[i]=dp[j]+1
        return max(dp)
        