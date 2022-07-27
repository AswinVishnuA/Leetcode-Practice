class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        n=len(startTime)
        pairs=[]
        for i in  range(n):
            pairs.append([startTime[i],endTime[i],profit[i]])
        
        pairs.sort()
        
#         starts=[]
#         for i in range(n):
#             starts.append(pairs[i][0])    
            
            
        
        @lru_cache(None)
        def solve(i):
            
            if i==n:
                return 0
            
            ans=solve(i+1)
            
            for j in range(i+1,n+1):
                if j==n or pairs[i][1]<=pairs[j][0]:
                    ans=max(ans,pairs[i][-1]+solve(j))
                    break
                    
            
            return ans
                
        
        
        return solve(0)