class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        len1=len(word1)
        len2=len(word2)
        
        @lru_cache(None)
        def solve(n1,n2):
            
            if n2==0 and n1==0:
                return 0
            
            if n1==0:
                return n2
            
            if n2==0:
                return n1
            
            if word1[n1-1]!=word2[n2-1]:
                
                ans=1+min(solve(n1-1,n2),solve(n1-1,n2-1),solve(n1,n2-1))
            
            else:
                
                ans=solve(n1-1,n2-1)
                
                
            return ans
        
        
        
        return solve(len1,len2)
        
            
        
        
        
        
        
        