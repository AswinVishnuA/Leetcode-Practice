class Solution:
    def maxEnvelopes(self, env: List[List[int]]) -> int:
        
        env.sort(key= lambda x:(x[0],-x[1]))
        n=len(env)
        dp=[]
        
        for i in range(n):
            if not dp or dp[-1]< env[i][1]:
                dp.append(env[i][1])
            else:
                l=0
                r=len(dp)
                
                while l<r:
                    m=l + (r-l)//2
                    if dp[m]<env[i][1]:
                        l=m+1
                    else:
                        r=m
                dp[l]=env[i][1]
                
        
        return len(dp)
        
        
        
        