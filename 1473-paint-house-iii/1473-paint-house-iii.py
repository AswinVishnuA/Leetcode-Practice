class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @lru_cache(None)
        def solve(mval,tar,prev):
            # print(mval,tar,prev)
            if mval==0 and tar==0:
                return 0
            if (tar==0 and (houses[mval-1]!=0 and houses[mval-1]!=prev)) or mval==0:
                return float("inf")
                
            ans=float("inf")
            
                
            if houses[mval-1]!=0:
                if houses[mval-1]==prev:
                    ans=min(ans,solve(mval-1,tar,houses[mval-1]))
                else:
                    ans=min(ans,solve(mval-1,tar-1,houses[mval-1]))
            else:
                for i in range(n):
                    if i+1==prev:
                        ans=min(ans,cost[mval-1][i]+solve(mval-1,tar,i+1))
                    else:
                        ans=min(ans,cost[mval-1][i]+solve(mval-1,tar-1,i+1))

            return ans


        
        ans=solve(m,target,-1)
        return -1 if ans>10**6 else ans 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        