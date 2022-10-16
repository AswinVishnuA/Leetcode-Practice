class Solution:
    def minDifficulty(self, job: List[int], d: int) -> int:
        
        n=len(job)
        
        @lru_cache(None)
        def solve(n,d,curMax):
            # print(n,d)
            if n==0 :
                
                if d==0:
                    # print(n,d,0)
                    return 0
                else:
                    # print(n,d,"inf")
                    return float(inf)
            
            if d==0:
                return float(inf)
            
            curMax=max(job[n-1],curMax)
            include=curMax+solve(n-1,d-1,-1)
            notinclude=solve(n-1,d,curMax)
            
            
            ans= min(include,notinclude)
            # print(n,d,curMax,ans)
            return ans
        
        ans=solve(n,d,-1)
        return ans if ans!=float(inf) else -1
                
        
        