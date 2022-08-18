class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        
        count=Counter(arr)
        
        pq=[]
        
        heapify(pq)
        
        for key in count:    
            heappush(pq,-count[key])
        
        n=len(arr)
        curCount=n
        ans=0
        while curCount>n//2:
            
            curCount+=heappop(pq)
            ans+=1
        
        return ans
        
        
            
        
        