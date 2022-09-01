class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordSet=set(wordDict)
        
        trueSet=set()
        
        n=len(s)
        
        dp=[0 for i in range(n+1)]
        
        dp[0]=1
        
        
        for i in range(n+1):
            for j  in range(i):
                # print(i,j,s[j:i])
                if dp[j] and s[j:i] in wordSet:
                    dp[i]=1
                    
        
        # print(dp)
        return dp[n]
                    
                
        
        # print(dp)
        return solve(0,len(s))
        
        