class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
#         dp=[[0,0] for i in range(n)]
        
#         dp[0][0]=0
#         dp[0][1]=-prices[0]
        
#         for i in range(1,n):
            
#             dp[i][0]=max(dp[i-1][0],dp[i-1][1]+prices[i])
#             if i>=2:
#                 dp[i][1]=max(dp[i-1][1],dp[i-2][0]-prices[i])
#             else:
#                 dp[i][1]=max(dp[i-1][1],-prices[i])
        
#         return dp[n-1][0]

        noStock=0
        oneStock=float("-inf")
        preProfit=0
        
        for price in prices:
            temp=noStock
            noStock=max(noStock,oneStock+price)
            oneStock=max(oneStock,preProfit-price)
            preProfit=temp
        
        return noStock 
        