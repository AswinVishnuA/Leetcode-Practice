class Solution:
    def reverse(self, x: int) -> int:
        sign=1
        if x<0:
            sign=-1
        x=abs(x)
        new_num=0
        while x:
            
            new_num = new_num * 10 + x % 10
            
            x= x // 10
            
        if new_num < 2147483648 or (new_num == 2147483648 and sign==-1):
            return sign*new_num
        else:
            return 0
        
            
            
            
        
        