class Solution:
    def numDecodings(self, s: str) -> int:
        
        
#         dp=[-1 for i in range(len(s)+1)]
        
#         def solve(i):
            
#             if i == len(s):
#                 return 1
            
#             if s[i]=='0':
#                 return 0
            
#             if dp[i]!=-1:
#                 return dp[i]
            
#             dp[i]=solve(i+1)
            
#             if (i!=len(s)-1 and s[i]=='1') or ( i!=len(s)-1 and s[i]=='2' and s[i+1] in {"0","1","2","3","4","5","6"}):
#                 dp[i]+=solve(i+2)
            
#             return dp[i]
        
        n=len(s)
        dp=[0 for i in range(n+1)]
        dp[0]=1
        
        for i in range(1,n+1):
            
            if i==1:
                dp[i]=int((s[i-1]!="0"))
                continue
            
            if s[i-2]=='1' or (s[i-2]=='2' and s[i-1] in {"0","1","2","3","4","5","6"}) :
                dp[i]+=dp[i-2]
            
            if s[i-1]!='0': 
                dp[i]+=dp[i-1]
            
        # print(dp)    
        
        return dp[n]
            
            
        
        
        