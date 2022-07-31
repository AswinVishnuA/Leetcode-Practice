class Solution:
    def maxAverageRatio(self, cs: List[List[int]], es: int) -> float:
        
        n=len(cs)

        arr=[]
        
        def delta(i):
            
            fut=(cs[i][0]+1)/(cs[i][1]+1)
            
            cur=cs[i][0]/cs[i][1]
        
            return fut-cur
        
        for i in range(n):
            arr.append([-delta(i),i])
            
        heapify(arr)
        
        while es:
            
            cur,i=heappop(arr)
            
            cs[i][0]+=1
            cs[i][1]+=1
            
            heappush(arr,[-delta(i),i])
            
            es-=1
        
        ans=0
        for i in range(n):
            ans+=cs[i][0]/cs[i][1]
        
        return ans/n
            
            
            
            
            
            
        
        
    
                
                
        
        
        