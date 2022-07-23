class Solution:
    def checkValidString(self, s: str) -> bool:
#         a=0
#         b=0
#         for i in s:
#             if i=="(":
#                 a+=1
#             elif i==")":
#                 a-=1
#             else:
#                 b+=1
            
#             if a<0:
#                 if b<-a:
#                     return False
#                 else:
#                     b=b+a
#                     a=0
                
#         print(a,b)
#         if a==0:
#             return True

        n=len(s)
        @lru_cache(None)
        def solve(i,presum):
            
            if i==n:
                if presum==0:
                    return True
                else:
                    return False
            if presum<0:
                return False
            
            if s[i]=='(':
                return solve(i+1,presum+1)
            
            elif s[i]==')':
                return solve(i+1,presum-1)
            else:
                return solve(i+1,presum+1) or solve(i+1,presum-1) or solve(i+1,presum)
            
                
        
         
        return solve(0,0)
        
                
        