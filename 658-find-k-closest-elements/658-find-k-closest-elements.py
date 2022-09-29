class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        pq=[]
        
        
        for val in arr:
            heappush(pq,(abs(val-x),val))
            
        ans=[]
        for i in range(k):
            ans.append(heappop(pq)[-1])
            
        return sorted(ans)
            
        