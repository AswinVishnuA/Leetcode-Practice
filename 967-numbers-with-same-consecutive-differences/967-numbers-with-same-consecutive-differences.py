class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        
        ans=[]
        
        def solve(cur):
            
            if len(cur)==n:
                ans.append(cur)
                return 
            
            lastNum=int(cur[-1])
            
            if lastNum+k<10:
                solve(cur+str(lastNum+k))
            
            if lastNum-k>=0 and k!=0:
                solve(cur+str(lastNum-k))
            
            return
                
            
            
        
        
        for i in range(1,10):
            solve(str(i))
        
        return ans
        