class Solution:
    def minimumLines(self, sp: List[List[int]]) -> int:
        
        sp.sort()
        # print(sp)
        n=len(sp)
        p=0
        count=0
        if n==1 or n==0:
            return 0
        ca=(sp[p][1]-sp[1][1])
        cb=(sp[p][0]-sp[1][0])
        gc=gcd(ca,cb)
        ca,cb=ca/gc,cb/gc
        for i in range(1,n):
            sa=(sp[p][1]-sp[i][1])
            sb=(sp[p][0]-sp[i][0])
            gs=gcd(sa,sb)
            sa,sb=sa/gs,sb/gs
            if not (sa==ca and sb==cb):
                # print(i,p,cur,slp)
                p=i-1
                ca=(sp[p][1]-sp[i][1])
                cb=(sp[p][0]-sp[i][0])
                gc=gcd(ca,cb)
                ca,cb=ca/gc,cb/gc
                
                count+=1
        
        return count+1
                
                
                
            
        