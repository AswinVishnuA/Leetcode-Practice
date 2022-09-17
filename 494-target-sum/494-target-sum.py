class Solution:
    def findTargetSumWays(self, nums: List[int], tar: int) -> int:
        
        
#         @lru_cache(None)
#         def solve(i,tar):
            
#             if i==0 and tar==0:
#                 return 1
#             if i==0:
#                 return 0
            
#             return solve(i-1,tar-nums[i-1])+solve(i-1,tar+nums[i-1])
        
#         return solve(len(nums),tar) 
        n=len(nums)
        
        total=sum(nums)
        
        tar=abs(tar)
        
        if (tar+total) % 2 !=0 or tar>total:
            return 0
        # print("1")
        sumval=(tar+total)//2
        
        dp=[0]*(sumval+1)
        
        dp[0]=1
        
        for i in range(1,n+1):
            preRow=dp.copy()
            for j in range(sumval+1):
                if nums[i-1]<=j:
                    dp[j]=preRow[j]+preRow[j-nums[i-1]]
                else:
                    dp[j]=preRow[j]
        
        return dp[sumval]
                
                
    
    
    
    
                 
        