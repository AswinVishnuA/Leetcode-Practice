class Solution:
    def countAndSay(self, n: int) -> str:
        
        cur="1"
        for i in range(1,n+1):
            print(cur)
            now=1
            prev=cur[0]
            new=""
            for c in cur[1:]:
                if c==prev:
                    now+=1
                else:
                    new+=str(now)+prev
                    now=1
                    prev=c
            if i!=1:
                new+=str(now)+prev
            else:
                new=cur
            cur= new
        
        return cur
            
                
        