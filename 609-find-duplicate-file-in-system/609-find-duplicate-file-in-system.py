class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        d=defaultdict(list)
        
        for path in paths:
            
            s=path.split()
            
            direc=s[0]
            
            for file in s[1:]:
                cur=file.split('(')
                content=cur[-1][:-1]
                
                curPath=direc+"/"+ cur[0]
                
                d[content].append(curPath)
        
        ans=[]
        for key,val in d.items():
            
            if len(val)<=1:
                continue
            
            ans.append(val)
        
        return ans
                
                
        