class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        n=len(s)
        lidx={}
        for i in range(n):
            lidx[s[i]]=i
            
        idx=0
        ans=[]
        while idx<n:
            cur=lidx[s[idx]]
            
            i=idx
            while i<cur:
                
                last=lidx[s[i]]
                
                if last>cur:
                    cur=last
                i+=1
            
            # print(cur,idx)
            length=cur-idx+1
            ans.append(length)
            idx=cur+1
        
        return ans
            
                
                
            
            
            
        