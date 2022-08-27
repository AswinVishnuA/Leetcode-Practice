class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        s1=queryIP.split('.')
        
        s2=queryIP.split(':')
        print(s1,s2)
        ans=False
        if len(s1)==4:
            
            ans=True
            for val in s1:
                
                if (len(val)>1 and val[0]=='0'):
                    ans=False
                    break
                if len(val)>3:
                    ans=False
                    break
                if val=='':
                    ans=False
                    break
                
                for c in val:
                    if c not in set(list("1234567890")):
                        ans=False
                        break
                
                if not ans:
                    break
                
                if  not (0<=int(val)<=255):
                    ans=False
                    break
                    
                
        
        if ans:
            return "IPv4"
        
        if len(s2)==8:
            
            pos=set(list("1234567890abcdefABCDEF"))
            
            for val in s2:
                
                if (not (1<=len(val)<=4)):
                    # print(len(val))
                    return "Neither"
                
                for c in val:
                    if c not in pos:
                        # print(c)
                        return "Neither"
            return "IPv6"
        return "Neither"
        