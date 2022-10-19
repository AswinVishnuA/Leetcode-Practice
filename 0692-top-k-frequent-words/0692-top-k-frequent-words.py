class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        c=Counter(words)
        
        pq=[]
        
        for word in c:
            print(word,c[word])
            heappush(pq,[-c[word],word])
        
        ans=[]
        for i in range(k):
            _,word=heappop(pq)
            ans.append(word)
        
        return ans
            
            
        