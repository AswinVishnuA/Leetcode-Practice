class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        ans=[]
        count=Counter(changed)
        
        if count[0]%2:
            return []
            
        
        for val in sorted(count):
            # print(val,count[val],count[val*2])
            
            if count[val]>count[val*2]:
                return []
            
            count[2*val]-=count[val] if val else count[val]//2
            
        return list(count.elements())
        
        
        