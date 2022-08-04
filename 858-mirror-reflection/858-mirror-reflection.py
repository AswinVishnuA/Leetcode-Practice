class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        
        m=q
        n=p
        
        while m%2==0 and n%2==0:
            m=m//2
            n=n//2
        
        if n%2==0:
            return 2
        elif m%2==0:
            return 0
        else:
            return 1
        
        