class Solution:
    def minRefuelStops(self, tar: int, sF: int, stns: List[List[int]]) -> int:
        
        
        pq=[-sF]
        
        ans=0
        i=0
        curDist=0
        while len(pq):
            
            curDist+= -heappop(pq)
            
            if tar<=curDist:
                return ans
            
            while i<len(stns) and stns[i][0]<=curDist:
                heappush(pq,-stns[i][1])
                i+=1
            
            ans+=1
        
        return -1
            
                
            
            
            
        
        '''
        
        dp[i]=min
        
        '''
                
            
            
            
            
                
            
        