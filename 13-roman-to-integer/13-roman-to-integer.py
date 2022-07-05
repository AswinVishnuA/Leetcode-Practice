class Solution:
    def romanToInt(self, s: str) -> int:
        
        d={"I":1,"V":5,
"X":10,
"L":50,
"C":100,
"D":500,
"M":1000}
        ans=0
        n=len(s)
        for i in range(n):
            if i!=n-1 and s[i]=="I" and s[i+1] in ["V","X"]:
                ans-=2
            if i!=n-1 and s[i]=="X" and s[i+1] in ["L","C"]:
                ans-=20
            if i!=n-1 and s[i]=="C" and s[i+1] in ["D","M"]:
                ans-=200
            
            ans+=d[s[i]]
            
        return ans
        