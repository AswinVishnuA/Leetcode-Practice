class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d=defaultdict(int)
        
        for i in s:
            d[i]+=1
            
        for j in t:      
            if j not in d:
                return False
            d[j]-=1
        
        for i in d:
            if d[i]!=0:
                return False
        
        return True
        