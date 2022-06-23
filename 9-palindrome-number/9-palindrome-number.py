class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x>0 and x%10==0):
            return False
        
        new_num=0
        old_num=x
        while x:
            
            new_num = new_num*10 + x%10
            
            x=x//10
        return new_num==old_num
        
        
        