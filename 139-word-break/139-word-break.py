class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordSet=set(wordDict)
        
        @lru_cache(None)
        def solve(string):
            
            
            if string=="" or string in wordSet:
                return True
            # print(string)
            for i in range(1,len(string)):
                if string[:i] in wordSet and  solve(string[i:]):
                    return True
            
            return False
        
        return solve(s)
        
        