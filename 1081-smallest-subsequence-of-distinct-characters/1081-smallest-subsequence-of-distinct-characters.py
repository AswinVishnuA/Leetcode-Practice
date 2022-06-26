class Solution:
    def smallestSubsequence(self, s: str) -> str:
        
        cnd=defaultdict(lambda :0)
        ans=""
        for i in s:
            cnd[i]+=1
        
        used=defaultdict(lambda :0)
        
        for c in s:
            cnd[c]-=1
            
            if used[c]>0:
                continue
            used[c]+=1
            while ans!="" and ans[-1]>c and cnd[ans[-1]]>0:
                used[ans[-1]]=0
                ans=ans[:-1]
            
            ans=ans+c
            
        return ans
                
        