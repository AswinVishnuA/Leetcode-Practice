from collections import OrderedDict
class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        
        stampLen=len(stamp)
        
        tarLen=len(target)
        
        target=list(target)
        final=["?"]*tarLen
        
        ans=[]
        
        while target!=final:
            
            change=False
            for i in range(tarLen-stampLen+1):
                
                flag=True
                for j in range(stampLen):
                    
                    if target[i+j]=='?':
                        continue
                    
                    if target[i+j]!=stamp[j]:
                        flag=False
                        break
                    
                if flag and target[i:i+stampLen]!=["?"]*stampLen:
                    change=True
                    target[i:i+stampLen]=["?"]*stampLen
                    ans.append(i)
                    if target==final:
                        break
            
            if not change:
                return []
        
        return ans[::-1]
                
                        
        
        
        
        
        