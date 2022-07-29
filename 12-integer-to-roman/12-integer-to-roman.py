class Solution:
    def intToRoman(self, num: int) -> str:
        
        mp={
            1000:"M",500:"D",100:"C",50:"L",10:"X",5:"V",1:"I"
        }
        
        sp={900,400,90,40,}
        
        res=""       
        for div in mp:
            
            ans=num//div
            
            rem=num%div
            
            if 1000>num>=900:
                res=res+"CM"
                num-=900
            elif 100>num>=90:
                res=res+"XC"
                num-=90
            elif num==9:
                res+="IX"
                num-=9
            elif 500>num>=400:
                res+="CD"
                num-=400
            elif 50>num>=40:
                res+="XL"
                num-=40
            elif num==4:
                res+="IV"
                num-=4
            else:            
                res=res+mp[div]*ans        
                num=rem
            
        return res
            
            
            
            
            
        