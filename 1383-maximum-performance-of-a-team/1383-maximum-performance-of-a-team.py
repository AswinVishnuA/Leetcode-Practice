class Solution:
    def maxPerformance(self, n, speed, efficiency, k):
        
        pq=[]
        
        sumval=0
        ans=0
        for e,s in sorted(zip(efficiency,speed), reverse=True):
            print(e,s,sumval,ans)
            sumval+=s
            heappush(pq,s)
            
            if len(pq)>k:
                sumval-=heappop(pq)
            
            ans=max(ans,sumval*e)
            
            
        
        return ans%(10**9 + 7)
           