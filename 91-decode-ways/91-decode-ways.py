class Solution:
    def numDecodings(self, s: str) -> int:
        
        
        @lru_cache(None)
        def solve(i):
            
            if i == len(s):
                return 1
            
            if s[i]=='0':
                return 0
            
            ans=solve(i+1)
            
            if (i!=len(s)-1 and s[i]=='1') or ( i!=len(s)-1 and s[i]=='2' and s[i+1] in {"0","1","2","3","4","5","6"}):
                ans+=solve(i+2)
            
            return ans
        
        return solve(0)
            
            
        
        
        