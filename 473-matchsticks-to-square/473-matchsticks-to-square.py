# from datetime import datetime

class Solution:
    def makesquare(self, ms: List[int]) -> bool:
        
        # start=datetime.now()

        summs=sum(ms)
        
        if summs % 4 != 0:
            return False
        length=len(ms)
        
        ms.sort(reverse=True)
        # print(ms)
        
        s_lens=[0,0,0,0]
        tar=summs//4
        
        if ms[0]>tar:
            return False
        
        def dfs(slens,n):
            
            if n==length:
                return slens[0]==slens[1] and slens[1]==slens[2] and slens[2]==slens[3]
                
            for i in range(4):
                
                if slens[i]+ms[n]>tar:
                    continue
                
                j=i-1
                
                while(j>=0):
                    
                    if slens[i]==slens[j]:
                        break
                    j-=1
                
                if j!=-1:
                    continue
                slens[i]+=ms[n]
                if dfs(slens,n+1):
                    return True
                slens[i]-=ms[n]
            
            return False
        
        ans=dfs(s_lens,0)
        
        # print(datetime.now()-start)
        
        return ans
        