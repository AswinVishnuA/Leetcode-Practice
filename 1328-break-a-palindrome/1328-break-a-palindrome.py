class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        
        
        l=len(palindrome)
        
        
        if l==1:
            return ""
        
        if palindrome=="a"*l:
            return "a"*(l-1)+"b"
        
        if l%2==1 and palindrome[:(l//2)]=="a"*(l//2):
            return palindrome[:-1]+"b"
        
        
        ans=""
        flag=True
        for c in palindrome:
            
            if c=="a":
                ans+="a"
            elif flag:
                ans+="a"
                flag=False
            else:
                ans+=c
                
        
        return ans
        
        
        
        