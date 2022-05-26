class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d=dict()
        
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
            
        for j in t:      
            if j not in d:
                return False
            d[j]-=1
        
        for i in d:
            if d[i]!=0:
                return False
        
        return True
        