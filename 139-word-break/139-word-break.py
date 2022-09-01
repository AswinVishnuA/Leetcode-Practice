class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordSet=set(wordDict)
        
        trueSet=set()
        
        dp=[[-1]*(len(s)+1) for _ in range(len(s)+1)]
        
        def solve(i,j):
            
            
            if s[i:j]=="":
                return True
            
            # print(i,j)
            if dp[i][j]!=-1:
                return dp[i][j]
            
            for k in range(i+1,j+1):
                if s[i:k] in wordSet and  solve(k,j):
                    dp[i][j]= 1
                    return True
            
            dp[i][j]= 0
            
            return False
        
        # print(dp)
        return solve(0,len(s))
        
        