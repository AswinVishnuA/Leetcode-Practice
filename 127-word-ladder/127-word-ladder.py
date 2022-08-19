class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordSet=set(wordList)
        
        if endWord not in wordSet:
            return 0
        
        
        q=deque([beginWord])
        
        vis=set()
        ans=1
        while len(q):
            
            size=len(q)
            
            while size:

                curWord=q.popleft()
                if curWord==endWord:
                    return ans
                # print(curWord)
                
                for i in range(len(curWord)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        newWord=curWord[:i]+c+curWord[i+1:]
                        if newWord in wordSet:
                            wordSet.remove(newWord)    
                            q.append(newWord)
                size-=1
            ans+=1
        
        return 0
            
        
        
        
        
        
        
        
        
        
        
        
                    
                    
        