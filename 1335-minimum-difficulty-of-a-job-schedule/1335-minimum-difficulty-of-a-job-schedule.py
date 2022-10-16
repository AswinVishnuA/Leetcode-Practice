class Solution:
    def minDifficulty(self, job: List[int], d: int) -> int:
        
        n=len(job)
        
        @lru_cache(None)
        def solve(n,d):
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
            
            ans=float(inf)
            curmax=float(-inf)
            for i in range(n-1,-1,-1):
                curmax=max(job[i],curmax)
                
                ans=min(ans,curmax+solve(i,d-1))
            
            # print(n,d,ans)
            return ans
        
        ans=solve(n,d)
        return ans if ans!=float(inf) else -1
                
        
        