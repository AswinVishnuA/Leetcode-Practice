class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minval=float("inf")
        ans=0
        for p in prices:
            
            if p<minval:
                minval=p
            else:
                ans=max(ans,p-minval)
                
        return ans
                