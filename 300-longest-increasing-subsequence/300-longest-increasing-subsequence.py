class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n=len(nums)
        
#         dp=[[-1 for i in range(2502)] for _ in range(2501)]
        
#         def solve(i,prev=-1):
#             # print(i,prev)
#             if i==n:
#                 return 0
            
#             if dp[i][prev+1]!=-1:
#                 return dp[i][prev+1]
            
#             dp[i][prev+1]=solve(i+1,prev)
            
#             if prev==-1 or nums[i]>nums[prev]:
#                 dp[i][prev+1]=max(dp[i][prev+1],1+solve(i+1,i))
            
            
#             return dp[i][prev+1]        
        
#         return solve(0)


#         dp=[1 for i in range(n)]
            
        
#         for i in range(n):
            
#             for j in range(i):
#                 # print(dp,i,j)

#                 if nums[i]>nums[j] and dp[i]<dp[j]+1:
#                     dp[i]=dp[j]+1
#         return max(dp)
        dp=[nums[0]]
        
        for i in range(1,n):
            
            idx = bisect_right(dp,nums[i])
            
            if idx==len(dp):
                if nums[i]==dp[idx-1]:
                    continue
                else:
                    dp.append(nums[i])
            else:
                if nums[i]==dp[idx-1]:
                    continue
                else:
                    dp[idx]=nums[i]
        
        return len(dp)
                
            
            
            
        