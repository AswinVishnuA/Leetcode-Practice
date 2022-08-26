class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        
        nstr=str(n)
        
        for i in range(30):
            
            num=2**i
            
            numstr=str(num)
            
            if len(numstr)!=len(nstr):
                continue
            
            c1=Counter(numstr)
            c2=Counter(nstr)
            
            if c1==c2:
                return True
        
        return False
            