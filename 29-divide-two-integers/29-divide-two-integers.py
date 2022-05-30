class Solution:
    def divide(self, dvd: int, dvr: int) -> int:
        ans=0
        
        sign = (dvd<0) == (dvr<0)
        
        dvd,dvr= abs(dvd),abs(dvr)

        while dvd>=dvr:
            temp,i=dvr,1
            
            while dvd>=temp:
                
                dvd-=temp
                ans+=i
                i=i<<1
                temp=temp<<1
        print(ans,sign)
        if not sign:
            ans=-ans
        
        return min(2147483647,ans)
        