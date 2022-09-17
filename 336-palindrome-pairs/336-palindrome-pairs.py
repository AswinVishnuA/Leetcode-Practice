class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        n=len(words)
        
        wordDict={word:i for i,word in enumerate(words)}
        ans=[]
        
        for word,i in wordDict.items():
            wordSize=len(word)
            
            for j in range(wordSize+1):
                
                prefix=word[:j]
                suffix=word[j:]
                
                
                
                if self.isPalindrome(prefix):
                    revSuffix=suffix[::-1]
                    if revSuffix!=word and revSuffix in wordDict:
                        ans.append([wordDict[revSuffix],i])
                
                if j!=wordSize and self.isPalindrome(suffix):
                    revPrefix=prefix[::-1]
                    if revPrefix!=word and revPrefix in wordDict:
                        ans.append([i,wordDict[revPrefix]])
                
        return ans
    
    def isPalindrome(self,word):
        
        return word==word[::-1]
                        
        