class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n=len(nums)
        
#         dp=[[-1 for i in range(20002)] for _ in range(2501)]
        
#         def solve(i,prev=-10001):
#             # print(i,prev)
#             if i==n:
#                 return 0
            
#             if dp[i][prev+10001]!=-1:
#                 return dp[i][prev+10001]
            
#             dp[i][prev+10001]=solve(i+1,prev)
            
#             if nums[i]>prev:
#                 dp[i][prev+10001]=max(dp[i][prev+10001],1+solve(i+1,nums[i]))
            
            
#             return dp[i][prev+10001]        
        
#         return solve(0)


        dp=[1 for i in range(n)]
            
        
        for i in range(n):
            
            for j in range(i):
                # print(dp,i,j)

                if nums[i]>nums[j] and dp[i]<dp[j]+1:
                    dp[i]=dp[j]+1
        return max(dp)
        