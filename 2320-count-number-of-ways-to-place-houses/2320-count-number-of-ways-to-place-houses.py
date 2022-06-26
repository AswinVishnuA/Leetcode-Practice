class Solution:
    def countHousePlacements(self, n: int) -> int:
        
        ans=1
        prev=1
        for i in range(n):
            temp=ans
            ans+=prev
            prev=temp
            
            
        return (ans*ans)%(7+10**9)
            
    