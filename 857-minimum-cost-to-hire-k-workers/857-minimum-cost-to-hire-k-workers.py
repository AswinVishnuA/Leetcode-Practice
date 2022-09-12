class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        
        
        arr=[[w/q,q] for q,w in zip(quality,wage)]
        
        pq=[]
        ans=float("inf")
        sumq=0
        for r,q in sorted(arr):
            sumq+=q
            heappush(pq,-q)
            
            if len(pq)>k:
                sumq+=heappop(pq)
            
            if len(pq)==k:
                ans=min(ans,r*sumq)
                
            
            
        return ans
                
                    
                    
                
            
                