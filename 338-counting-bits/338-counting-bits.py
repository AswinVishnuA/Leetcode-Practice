class Solution:
    def countBits(self, n: int) -> List[int]:
        
        ans=[]
        
        for i in range(n+1):
            
            count=0
            
            while i:
                
                if i%2==1:
                    count+=1
                    i=i-1
                
                i=i//2
            
            ans.append(count)
        
        return ans